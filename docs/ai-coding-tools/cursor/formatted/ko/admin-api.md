---
title: "Admin API"
source: "https://docs.cursor.com/ko/account/teams/admin-api"
language: "ko"
language_name: "Korean"
---

# Admin API
Source: https://docs.cursor.com/ko/account/teams/admin-api

API를 통해 팀 지표, 사용량 데이터, 지출 정보를 조회하기

Admin API는 멤버 정보, 사용 지표, 지출 내역을 포함한 팀 데이터를 코드로 액세스할 수 있게 해줘. 커스텀 대시보드나 모니터링 도구를 만들거나 기존 워크플로우에 통합해봐.

<Note>
  API는 첫 릴리스야. 피드백을 바탕으로 기능을 확장하는 중—필요한 엔드포인트를 알려줘!
</Note>

<div id="authentication">
  ## 인증
</div>

모든 API 요청에는 API 키 인증이 필요해. 팀 관리자만 API 키를 만들고 관리할 수 있어.

API 키는 조직에 귀속돼 있고, 모든 관리자에게 보이며, 원래 생성자의 계정 상태와 무관해.

<div id="creating-an-api-key">
  ### API 키 만들기
</div>

1. **cursor.com/dashboard** → **Settings** 탭 → **Cursor Admin API Keys**로 가
2. **Create New API Key** 클릭
3. 키에 알아보기 쉬운 이름 붙여 (예: "Usage Dashboard Integration")
4. 생성된 키를 바로 복사해—다시는 확인할 수 없어

형식: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### API 키 사용하기
</div>

기본 인증에서 API 키를 사용자 이름으로 사용해:

**기본 인증으로 curl 사용:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**또는 Authorization 헤더를 직접 설정하기:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## 기본 URL
</div>

모든 API 엔드포인트는 다음을 사용해:

```
https://api.cursor.com
```

<div id="endpoints">
  ## 엔드포인트
</div>

<div id="get-team-members">
  ### 팀 멤버 가져오기
</div>

모든 팀 멤버와 상세 정보를 가져와.

```
GET /teams/members
```

#### 응답

팀 멤버 객체 배열을 반환:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### 예시 답변

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "구성원"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "소유자"
    }
  ]
}

```

#### 요청 예시

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

<div id="get-daily-usage-data">
  ### 일일 사용량 데이터 가져오기
</div>

지정된 날짜 범위에서 팀의 일일 사용량 지표를 자세히 조회해. 코드 편집, AI 지원 사용량, 수락률에 대한 인사이트를 제공해.

```
POST /teams/daily-usage-data
```

#### 요청 본문

<div className="full-width-table">
  | 매개변수        | 타입     | 필수 | 설명               |
  | :---------- | :----- | :- | :--------------- |
  | `startDate` | number | 예  | 에포크 밀리초 기준 시작 날짜 |
  | `endDate`   | number | 예  | 에포크 밀리초 기준 종료 날짜 |
</div>

<Note>
  날짜 범위는 최대 90일이야. 더 긴 기간은 여러 번 나눠서 요청해 줘.
</Note>

#### 응답

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### 응답 필드
</div>

<div className="full-width-table">
  | Field                      | Description                  |
  | :------------------------- | :--------------------------- |
  | `date`                     | 에포크 밀리초 기준 날짜                |
  | `isActive`                 | 해당 날짜에 활성 사용자 여부             |
  | `totalLinesAdded`          | 추가된 코드 라인 수                  |
  | `totalLinesDeleted`        | 삭제된 코드 라인 수                  |
  | `acceptedLinesAdded`       | 승인된 AI 제안으로 추가된 라인 수         |
  | `acceptedLinesDeleted`     | 승인된 AI 제안으로 삭제된 라인 수         |
  | `totalApplies`             | 적용(Apply) 작업 수               |
  | `totalAccepts`             | 승인된 제안 수                     |
  | `totalRejects`             | 거부된 제안 수                     |
  | `totalTabsShown`           | 표시된 탭 완성 수                   |
  | `totalTabsAccepted`        | 승인된 탭 완성 수                   |
  | `composerRequests`         | Composer 요청 수                |
  | `chatRequests`             | Chat 요청 수                    |
  | `agentRequests`            | Agent 요청 수                   |
  | `cmdkUsages`               | 명령 팔레트(Cmd+K) 사용 횟수          |
  | `subscriptionIncludedReqs` | 구독 포함 요청 수                   |
  | `apiKeyReqs`               | API 키 요청 수                   |
  | `usageBasedReqs`           | 사용량 기반 과금 요청 수               |
  | `bugbotUsages`             | 버그 감지 사용 횟수                  |
  | `mostUsedModel`            | 가장 많이 사용된 AI 모델              |
  | `applyMostUsedExtension`   | 적용(Apply)에서 가장 많이 사용된 파일 확장자 |
  | `tabMostUsedExtension`     | 탭에서 가장 많이 사용된 파일 확장자         |
  | `clientVersion`            | Cursor 버전                    |
  | `email`                    | 사용자 이메일                      |
</div>

#### 예시 답변

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

<div id="example-requests">
  #### 예시 요청
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### 지출 데이터 가져오기
</div>

검색, 정렬, 페이지네이션을 포함해 이번 달 지출 정보를 조회해.

```
POST /teams/spend
```

#### 요청 본문

<div className="full-width-table">
  | 매개변수            | 타입     | 필수  | 설명                                           |
  | :-------------- | :----- | :-- | :------------------------------------------- |
  | `searchTerm`    | string | 아니오 | 사용자 이름과 이메일에서 검색                             |
  | `sortBy`        | string | 아니오 | 정렬 기준: `amount`, `date`, `user`. 기본값: `date` |
  | `sortDirection` | string | 아니오 | 정렬 방향: `asc`, `desc`. 기본값: `desc`            |
  | `page`          | number | 아니오 | 페이지 번호(1부터 시작). 기본값: `1`                     |
  | `pageSize`      | number | 아니오 | 페이지당 결과 수                                    |
</div>

#### 응답

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### 응답 필드
</div>

<div className="full-width-table">
  | 필드                         | 설명                    |
  | :------------------------- | :-------------------- |
  | `spendCents`               | 총 지출액(센트)             |
  | `fastPremiumRequests`      | Fast 프리미엄 모델 요청 수     |
  | `name`                     | 멤버 이름                 |
  | `email`                    | 멤버 이메일                |
  | `role`                     | 팀 내 역할                |
  | `hardLimitOverrideDollars` | 커스텀 지출 한도 오버라이드(달러)   |
  | `subscriptionCycleStart`   | 구독 사이클 시작 시각(에포크 밀리초) |
  | `totalMembers`             | 팀 전체 멤버 수             |
  | `totalPages`               | 총 페이지 수               |
</div>

#### 예시 답변

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### 예시 요청
</div>

**기본 지출 데이터:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**페이지네이션을 사용해 특정 사용자 검색:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### 사용량 이벤트 데이터 가져오기
</div>

강력한 필터링, 검색, 그리고 페이지네이션 옵션으로 팀의 상세한 사용량 이벤트를 조회해. 이 엔드포인트는 개별 API 호출, 모델 사용량, 토큰 사용량, 비용까지 세밀하게 파악할 수 있는 인사이트를 제공해.

```
POST /teams/filtered-usage-events
```

#### 요청 본문

<div className="full-width-table">
  | 매개변수        | 타입     | 필수  | 설명                       |
  | :---------- | :----- | :-- | :----------------------- |
  | `startDate` | number | 아니오 | Epoch 밀리초 기준 시작일         |
  | `endDate`   | number | 아니오 | Epoch 밀리초 기준 종료일         |
  | `userId`    | number | 아니오 | 특정 사용자 ID로 필터            |
  | `page`      | number | 아니오 | 페이지 번호(1부터 시작). 기본값: `1` |
  | `pageSize`  | number | 아니오 | 페이지당 결과 수. 기본값: `10`     |
  | `email`     | string | 아니오 | 사용자 이메일 주소로 필터           |
</div>

#### 응답

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### 응답 필드 설명
</div>

<div className="full-width-table">
  | Field                   | Description                                     |
  | :---------------------- | :---------------------------------------------- |
  | `totalUsageEventsCount` | 쿼리와 일치하는 사용 이벤트의 총 개수                           |
  | `pagination`            | 결과 탐색을 위한 페이지네이션 메타데이터                          |
  | `timestamp`             | 이벤트 타임스탬프(에포크 밀리초)                              |
  | `model`                 | 요청에 사용된 AI 모델                                   |
  | `kind`                  | 사용 유형(예: "Usage-based", "Included in Business") |
  | `maxMode`               | Max Mode가 활성화되었는지                               |
  | `requestsCosts`         | 요청 단위 기준 비용                                     |
  | `isTokenBasedCall`      | 이벤트가 사용량 기반으로 과금되는 경우 true                      |
  | `tokenUsage`            | 토큰 사용량 상세(isTokenBasedCall이 true일 때 제공)         |
  | `isFreeBugbot`          | 무료 Bugbot 사용인지                                  |
  | `userEmail`             | 요청을 보낸 사용자의 이메일                                 |
  | `period`                | 조회한 데이터의 날짜 범위                                  |
</div>

#### 응답 예시

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "사용량 기반",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Business 요금제 포함",
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### 예시 요청
</div>

**기본 페이지네이션으로 모든 사용량 이벤트 가져오기:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**날짜 범위와 특정 사용자로 필터링:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**커스텀 페이지네이션을 사용해 특정 사용자의 사용량 이벤트 가져오기:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### 사용자 지출 한도 설정
</div>

팀 구성원별로 지출 한도를 설정해. 이렇게 하면 팀에서 각 사용자가 AI 사용에 얼마까지 쓸 수 있는지 관리할 수 있어.

```
POST /teams/user-spend-limit
```

<Note>
  **레이트 리미트:** 팀당 분당 60건
</Note>

#### 요청 본문

<div className="full-width-table">
  | 매개변수                | 타입     | 필수 | 설명                        |
  | :------------------ | :----- | :- | :------------------------ |
  | `userEmail`         | string | 예  | 팀 멤버의 이메일 주소              |
  | `spendLimitDollars` | number | 예  | 달러 기준 지출 한도(정수만, 소수점 불가). |
</div>

<Note>
  * 사용자는 이미 네 팀의 멤버여야 해
  * 정수형 값만 받을 수 있어(소수 금액은 안 돼)
  * `spendLimitDollars`를 0으로 설정하면 한도가 \$0으로 설정돼
</Note>

#### Response

성공 또는 실패를 나타내는 표준화된 응답을 반환해:

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### 예시 응답
</div>

**한도 설정 성공:**

```json  theme={null}
{
  "outcome": "success",
  "message": "사용자 developer@company.com의 지출 한도가 $100로 설정됨"
}
```

**오류 응답:**

```json  theme={null}
{
  "outcome": "error",
  "message": "잘못된 이메일 형식"
}
```

<div id="example-requests">
  #### 예시 요청
</div>

**지출 한도 설정:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

리포지토리와 패턴을 추가해 파일이나 디렉터리가 인덱싱되거나 팀 컨텍스트로 사용되지 않게 막아.

<div id="get-team-repo-blocklists">
  #### 팀 리포지토리 차단 목록 가져오기
</div>

팀에 설정된 모든 리포지토리 차단 목록을 가져와.

```
GET /settings/repo-blocklists/repos
```

##### 응답

리포지토리 블록리스트 객체 배열을 반환해:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### 응답 예시
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### 예시 요청
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u YOUR_API_KEY:
```

<div id="upsert-repo-blocklists">
  #### 레포 블록리스트 업서트
</div>

제공된 레포의 기존 블록리스트를 교체해.
*참고: 이 엔드포인트는 제공된 레포의 패턴만 덮어써. 다른 레포에는 영향 없어.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### 요청 본문
</div>

| 매개변수  | 타입    | 필수 | 설명                |
| ----- | ----- | -- | ----------------- |
| repos | array | 예  | 리포지토리 블록리스트 객체 배열 |

각 리포지토리 객체에는 다음이 포함돼야 해:

| 필드       | 타입        | 필수 | 설명                     |
| -------- | --------- | -- | ---------------------- |
| url      | string    | 예  | 블록리스트에 추가할 리포지토리 URL   |
| patterns | string\[] | 예  | 차단할 파일 패턴 배열(글롭 패턴 지원) |

<div id="response">
  ##### Response
</div>

업데이트된 저장소 차단 목록을 반환해:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

##### 요청 예시

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### 리포지토리 차단 목록 삭제
</div>

차단 목록에서 특정 리포지토리를 제거해.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### 매개변수
</div>

| 매개변수   | 유형     | 필수 | 설명                |
| ------ | ------ | -- | ----------------- |
| repoId | string | 예  | 삭제할 저장소 차단 목록의 ID |

<div id="response">
  ##### Response
</div>

성공적으로 삭제되면 204 No Content를 반환해.

<div id="example-request">
  ##### 예시 요청
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u YOUR_API_KEY:
```

<div id="pattern-examples">
  #### 패턴 예시
</div>

자주 쓰는 블록리스트 패턴:

* `*` - 저장소 전체 차단
* `*.env` - 모든 .env 파일 차단
* `config/*` - config 디렉터리의 모든 파일 차단
* `**/*.secret` - 모든 하위 디렉터리의 .secret 파일 차단
* `src/api/keys.ts` - 특정 파일 차단

---

← Previous: [Pricing](./pricing.md) | [Index](./index.md) | Next: [AI Code Tracking API](./ai-code-tracking-api.md) →