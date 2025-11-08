---
title: "AI Code Tracking API"
source: "https://docs.cursor.com/ko/account/teams/ai-code-tracking-api"
language: "ko"
language_name: "Korean"
---

# AI Code Tracking API
Source: https://docs.cursor.com/ko/account/teams/ai-code-tracking-api

팀 리포지토리에 대한 AI 생성 코드 분석에 액세스

팀 리포지토리에 대한 AI 생성 코드 분석에 액세스해. 커밋별 AI 사용량과 세밀한 승인된 AI 변경 사항이 포함돼.

<Note>
  API는 첫 릴리스야. 피드백을 바탕으로 기능을 확장하고 있어 — 어떤 엔드포인트가 필요한지 알려줘!
</Note>

* **Availability**: 엔터프라이즈 팀 전용
* **Status**: 알파(응답 구조와 필드가 변경될 수 있음)

<div id="authentication">
  ## 인증
</div>

모든 API 요청은 API 키로 인증해야 해. 이 API는 다른 엔드포인트와 같은 Admin API 인증을 사용해.

자세한 인증 방법은 [Admin API authentication](/ko/account/teams/admin-api#authentication)을 참고해.

<div id="base-url">
  ## 기본 URL
</div>

모든 API 엔드포인트는 다음을 사용해:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## 요청 제한
</div>

* 팀 및 엔드포인트별 분당 5회 요청

<div id="query-parameters">
  ## 쿼리 매개변수
</div>

아래의 모든 엔드포인트는 동일한 쿼리 매개변수를 쿼리 문자열로 받아:

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                                                                                                                     |                                                                  |
  | :---------- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
  | `startDate` | string | date     | No                                                                                                                              | ISO 날짜 문자열, 리터럴 "now", 또는 "7d"처럼 상대 일수(지금 - 7일 의미). 기본값: 지금 - 7일 |
  | `endDate`   | string | date     | No                                                                                                                              | ISO 날짜 문자열, 리터럴 "now", 또는 "0d"처럼 상대 일수. 기본값: 지금                  |
  | `page`      | number | No       | 페이지 번호(1부터 시작). 기본값: 1                                                                                                          |                                                                  |
  | `pageSize`  | number | No       | 페이지당 결과 수. 기본값: 100, 최대: 1000                                                                                                   |                                                                  |
  | `user`      | string | No       | 단일 사용자로 필터링(선택). 이메일(예: [developer@company.com](mailto:developer@company.com)), 인코딩된 ID(예: user\_abc123...), 또는 숫자 ID(예: 42) 허용 |                                                                  |
</div>

<Note>
  응답의 userId는 접두사 user\_가 붙은 인코딩된 외부 ID로 반환돼. API에서 안정적으로 사용할 수 있어.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## 시맨틱과 메트릭 계산 방식
</div>

* **Sources**: "TAB"은 수락된 인라인 자동완성을 의미하고, "COMPOSER"는 Composer에서 수락된 diff를 의미해
* **Lines metrics**: tabLinesAdded/Deleted와 composerLinesAdded/Deleted는 각각 별도로 집계돼; nonAiLinesAdded/Deleted는 max(0, totalLines - AI lines)로 계산돼
* **Privacy mode**: 클라이언트에서 활성화된 경우, 일부 메타데이터(예: fileName)가 생략될 수 있어
* **Branch info**: 현재 브랜치가 저장소의 기본 브랜치와 같으면 isPrimaryBranch는 true야; 저장소 정보를 가져올 수 없으면 undefined일 수 있어

그 파일을 확인해 커밋과 변경 사항이 어떻게 감지되고 보고되는지 파악해봐.

<div id="endpoints">
  ## 엔드포인트
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI 커밋 메트릭 가져오기 (JSON, 페이지네이션)
</div>

커밋별로 집계된 메트릭을 가져오고, 각 라인을 TAB, COMPOSER, 비(非) AI로 분류해.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### 응답
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric 필드
</div>

<div className="full-width-table">
  | Field                  | Type    | Description                   |                  |
  | :--------------------- | :------ | :---------------------------- | ---------------- |
  | `commitHash`           | string  | Git 커밋 해시                     |                  |
  | `userId`               | string  | 인코딩된 사용자 ID (예: user\_abc123) |                  |
  | `userEmail`            | string  | 사용자 이메일 주소                    |                  |
  | `repoName`             | string  | null                          | 저장소 이름           |
  | `branchName`           | string  | null                          | 브랜치 이름           |
  | `isPrimaryBranch`      | boolean | null                          | 기본 브랜치 여부        |
  | `totalLinesAdded`      | number  | 커밋에서 추가된 총 줄 수                |                  |
  | `totalLinesDeleted`    | number  | 커밋에서 삭제된 총 줄 수                |                  |
  | `tabLinesAdded`        | number  | TAB 자동 완성으로 추가된 줄 수           |                  |
  | `tabLinesDeleted`      | number  | TAB 자동 완성으로 삭제된 줄 수           |                  |
  | `composerLinesAdded`   | number  | Composer로 추가된 줄 수             |                  |
  | `composerLinesDeleted` | number  | Composer로 삭제된 줄 수             |                  |
  | `nonAiLinesAdded`      | number  | null                          | 비 AI 추가 줄 수      |
  | `nonAiLinesDeleted`    | number  | null                          | 비 AI 삭제 줄 수      |
  | `message`              | string  | null                          | 커밋 메시지           |
  | `commitTs`             | string  | null                          | 커밋 타임스탬프(ISO 형식) |
  | `createdAt`            | string  | 수집 타임스탬프(ISO 형식)              |                  |
</div>

<div id="example-response">
  #### 예시 응답
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "리팩터링: 분석 클라이언트 분리",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### 예시 요청
</div>

**기본 예시:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u YOUR_API_KEY:
```

**사용자(이메일)로 필터:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI 커밋 메트릭 다운로드 (CSV, 스트리밍)
</div>

대용량 데이터 추출용 커밋 메트릭 데이터를 CSV 형식으로 다운로드해.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### 응답
</div>

헤더:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 컬럼
</div>

<div className="full-width-table">
  | Column                   | Type    | Description        |
  | :----------------------- | :------ | :----------------- |
  | `commit_hash`            | string  | Git 커밋 해시          |
  | `user_id`                | string  | 인코딩된 사용자 ID        |
  | `user_email`             | string  | 사용자 이메일 주소         |
  | `repo_name`              | string  | 리포지토리 이름           |
  | `branch_name`            | string  | 브랜치 이름             |
  | `is_primary_branch`      | boolean | 기본 브랜치인지 여부        |
  | `total_lines_added`      | number  | 커밋에서 추가된 총 줄 수     |
  | `total_lines_deleted`    | number  | 커밋에서 삭제된 총 줄 수     |
  | `tab_lines_added`        | number  | TAB 자동완성으로 추가된 줄 수 |
  | `tab_lines_deleted`      | number  | TAB 자동완성으로 삭제된 줄 수 |
  | `composer_lines_added`   | number  | Composer로 추가된 줄 수  |
  | `composer_lines_deleted` | number  | Composer로 삭제된 줄 수  |
  | `non_ai_lines_added`     | number  | 비 AI 추가 줄 수        |
  | `non_ai_lines_deleted`   | number  | 비 AI 삭제 줄 수        |
  | `message`                | string  | 커밋 메시지             |
  | `commit_ts`              | string  | 커밋 타임스탬프(ISO 형식)   |
  | `created_at`             | string  | 수집 타임스탬프(ISO 형식)   |
</div>

<div id="sample-csv-output">
  #### CSV 출력 예시
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"리팩터링: 애널리틱스 클라이언트 분리",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"에러 처리 추가",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-requests">
  #### 예시 요청
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AI 코드 변경 지표 가져오기 (JSON, 페이지네이션)
</div>

결정적 changeId로 그룹화된 세밀한 승인된 AI 변경 내역을 가져와. 커밋과 상관없이 승인된 AI 이벤트를 분석하는 데 유용해.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### 응답
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric 필드
</div>

<div className="full-width-table">
  | Field               | Type   | Description                              |           |
  | :------------------ | :----- | :--------------------------------------- | --------- |
  | `changeId`          | string | 변경의 결정적 ID                               |           |
  | `userId`            | string | 인코딩된 사용자 ID (예: user\_abc123)            |           |
  | `userEmail`         | string | 사용자 이메일 주소                               |           |
  | `source`            | "TAB"  | "COMPOSER"                               | AI 변경의 원본 |
  | `model`             | string | null                                     | 사용된 AI 모델 |
  | `totalLinesAdded`   | number | 추가된 총 줄 수                                |           |
  | `totalLinesDeleted` | number | 삭제된 총 줄 수                                |           |
  | `createdAt`         | string | 수집 타임스탬프(ISO 형식)                         |           |
  | `metadata`          | Array  | 파일 메타데이터(프라이버시 모드에서는 fileName이 생략될 수 있음) |           |
</div>

<div id="example-response">
  #### 예시 응답
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

#### 요청 예시

**기본 요청:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u YOUR_API_KEY:
```

**사용자(인코딩된 ID)로 필터링:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**사용자(이메일)로 필터링:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AI 코드 변경 메트릭 다운로드(CSV, 스트리밍)
</div>

대량 데이터 추출을 위해 변경 메트릭 데이터를 CSV 형식으로 다운로드해.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### 응답
</div>

헤더:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 컬럼
</div>

<div className="full-width-table">
  | 컬럼                    | 타입     | 설명                             |
  | :-------------------- | :----- | :----------------------------- |
  | `change_id`           | string | 변경에 대한 결정적 ID                  |
  | `user_id`             | string | 인코딩된 사용자 ID                    |
  | `user_email`          | string | 사용자의 이메일 주소                    |
  | `source`              | string | AI 변경의 소스(탭 또는 컴포저)            |
  | `model`               | string | 사용한 AI 모델                      |
  | `total_lines_added`   | number | 추가된 총 줄 수                      |
  | `total_lines_deleted` | number | 삭제된 총 줄 수                      |
  | `created_at`          | string | 수집 타임스탬프(ISO 형식)               |
  | `metadata_json`       | string | 메타데이터 엔트리 배열을 JSON 문자열로 직렬화한 값 |
</div>

<div id="notes">
  #### 참고
</div>

* metadata\_json은 메타데이터 엔트리 배열을 JSON 문자열로 직렬화한 값임(프라이버시 모드에선 fileName이 생략될 수 있음)
* CSV를 읽을 때 따옴표로 감싼 필드는 꼭 파싱하기

<div id="sample-csv-output">
  #### CSV 출력 예시
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-requests">
  #### 예시 요청
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## 팁
</div>

* 모든 엔드포인트에서 특정 사용자만 빨리 걸러보려면 `user` 파라미터 써
* 대용량 데이터 추출엔 CSV 엔드포인트를 추천—서버 측에서 한 번에 10,000건씩 스트리밍돼
* 클라이언트가 기본 브랜치를 확인하지 못하면 `isPrimaryBranch` 는 정의되지 않을 수 있어
* `commitTs` 는 커밋 타임스탬프고, `createdAt` 는 우리 서버로 들어온 시각이야
* 클라이언트에서 프라이버시 모드가 켜져 있으면 일부 필드가 없을 수 있어

<div id="changelog">
  ## 변경 로그
</div>

* **알파 릴리스**: 커밋과 변경 사항용 초기 엔드포인트. 피드백에 따라 응답 스키마가 변경될 수 있음

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →