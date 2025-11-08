---
title: "Admin API"
source: "https://docs.cursor.com/tr/account/teams/admin-api"
language: "tr"
language_name: "Turkish"
---

# Admin API
Source: https://docs.cursor.com/tr/account/teams/admin-api

API aracılığıyla ekip metriklerine, kullanım verilerine ve harcama bilgilerine eriş

Admin API, üye bilgileri, kullanım metrikleri ve harcama detayları dahil olmak üzere ekibinin verilerine programatik olarak erişmeni sağlar. Özel panolar, izleme araçları oluştur ya da mevcut iş akışlarınla entegre et.

<Note>
  API ilk sürümünde. Yetenekleri geri bildirimlere göre genişletiyoruz — hangi endpoint’lere ihtiyacın olduğunu bize söyle!
</Note>

<div id="authentication">
  ## Kimlik doğrulama
</div>

Tüm API istekleri bir API anahtarıyla kimlik doğrulamayı gerektirir. API anahtarlarını yalnızca ekip yöneticileri oluşturabilir ve yönetebilir.

API anahtarları kuruluşa bağlıdır, tüm yöneticiler tarafından görüntülenebilir ve ilk oluşturanın hesap durumundan etkilenmez.

<div id="creating-an-api-key">
  ### Bir API Anahtarı Oluşturma
</div>

1. **cursor.com/dashboard** → **Settings** sekmesi → **Cursor Admin API Keys** bölümüne git
2. **Create New API Key**’e tıkla
3. Anahtarına açıklayıcı bir ad ver (ör. “Usage Dashboard Integration”)
4. Oluşturulan anahtarı hemen kopyala — bir daha gösterilmeyecek

Biçim: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### API Anahtarını Kullanma
</div>

API anahtarını temel kimlik doğrulamada kullanıcı adı olarak kullan:

**Temel kimlik doğrulamayla curl kullanma:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**Ya da Authorization başlığını doğrudan ayarla:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## Temel URL
</div>

Tüm API uç noktaları şu adresi kullanır:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Uç Noktalar
</div>

<div id="get-team-members">
  ### Ekip Üyelerini Getir
</div>

Tüm ekip üyelerini ve ayrıntılarını al.

```
GET /teams/members
```

#### Yanıt

Ekip üyesi nesnelerinden oluşan bir dizi döndürür:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Örnek Yanıt

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "üye"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "sahip"
    }
  ]
}

```

#### Örnek İstek

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u API_ANAHTARIN:
```

<div id="get-daily-usage-data">
  ### Günlük Kullanım Verilerini Al
</div>

Belirli bir tarih aralığında ekibin için ayrıntılı günlük kullanım metriklerini getir. Kod düzenlemeleri, yapay zeka yardımı kullanımı ve kabul oranları hakkında içgörüler sunar.

```
POST /teams/daily-usage-data
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre   | Tür    | Gerekli | Açıklama                                    |
  | :---------- | :----- | :------ | :------------------------------------------ |
  | `startDate` | number | Evet    | Epoch milisaniye cinsinden başlangıç tarihi |
  | `endDate`   | number | Evet    | Epoch milisaniye cinsinden bitiş tarihi     |
</div>

<Note>
  Tarih aralığı 90 günü geçemez. Daha uzun dönemler için birden fazla istek gönder.
</Note>

#### Yanıt

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
  #### Yanıt Alanları
</div>

<div className="full-width-table">
  | Field                      | Description                                 |
  | :------------------------- | :------------------------------------------ |
  | `date`                     | Epoch milisaniye cinsinden tarih            |
  | `isActive`                 | Kullanıcı bu gün aktif mi                   |
  | `totalLinesAdded`          | Eklenen kod satırı                          |
  | `totalLinesDeleted`        | Silinen kod satırı                          |
  | `acceptedLinesAdded`       | Kabul edilen AI önerilerinden eklenen satır |
  | `acceptedLinesDeleted`     | Kabul edilen AI önerilerinden silinen satır |
  | `totalApplies`             | Apply işlemleri                             |
  | `totalAccepts`             | Kabul edilen öneriler                       |
  | `totalRejects`             | Reddedilen öneriler                         |
  | `totalTabsShown`           | Gösterilen sekme tamamlama sayısı           |
  | `totalTabsAccepted`        | Kabul edilen sekme tamamlama sayısı         |
  | `composerRequests`         | Composer istekleri                          |
  | `chatRequests`             | Sohbet istekleri                            |
  | `agentRequests`            | Agent istekleri                             |
  | `cmdkUsages`               | Komut paleti (Cmd+K) kullanımı              |
  | `subscriptionIncludedReqs` | Abonelik kapsamındaki istekler              |
  | `apiKeyReqs`               | API anahtarı istekleri                      |
  | `usageBasedReqs`           | Kullanım başına ödeme istekleri             |
  | `bugbotUsages`             | Hata bulma kullanımları                     |
  | `mostUsedModel`            | En sık kullanılan yapay zeka modeli         |
  | `applyMostUsedExtension`   | Apply için en çok kullanılan dosya uzantısı |
  | `tabMostUsedExtension`     | Sekme için en çok kullanılan dosya uzantısı |
  | `clientVersion`            | Cursor sürümü                               |
  | `email`                    | Kullanıcı e-postası                         |
</div>

#### Örnek Yanıt

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
      "enCokKullanilanModel": "gpt-4",
      "applyEnCokKullanilanUzanti": ".tsx",
      "tabEnCokKullanilanUzanti": ".ts",
      "istemciSurumu": "0.25.1",
      "ePosta": "developer@company.com"
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
      "enCokKullanilanModel": "claude-3-opus",
      "applyEnCokKullanilanUzanti": ".py",
      "tabEnCokKullanilanUzanti": ".py",
      "istemciSurumu": "0.25.1",
      "ePosta": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Örnek İstek

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u API_ANAHTARIN: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Harcama Verilerini Al
</div>

Geçerli takvim ayı için arama, sıralama ve sayfalama ile harcama bilgilerini getir.

```
POST /teams/spend
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre       | Tür    | Gerekli | Açıklama                                                       |
  | :-------------- | :----- | :------ | :------------------------------------------------------------- |
  | `searchTerm`    | string | Hayır   | Kullanıcı adları ve e-postalarda ara                           |
  | `sortBy`        | string | Hayır   | Şuna göre sırala: `amount`, `date`, `user`. Varsayılan: `date` |
  | `sortDirection` | string | Hayır   | Sıralama yönü: `asc`, `desc`. Varsayılan: `desc`               |
  | `page`          | number | Hayır   | Sayfa numarası (1’den başlayarak). Varsayılan: `1`             |
  | `pageSize`      | number | Hayır   | Sayfa başına sonuç sayısı                                      |
</div>

#### Yanıt

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
  #### Yanıt Alanları
</div>

<div className="full-width-table">
  | Alan                       | Açıklama                                       |
  | :------------------------- | :--------------------------------------------- |
  | `spendCents`               | Toplam harcama (sent)                          |
  | `fastPremiumRequests`      | Hızlı premium model istekleri                  |
  | `name`                     | Üye adı                                        |
  | `email`                    | Üye e-postası                                  |
  | `role`                     | Ekipteki rol                                   |
  | `hardLimitOverrideDollars` | Özel harcama sınırı geçersiz kılma             |
  | `subscriptionCycleStart`   | Abonelik döngüsü başlangıcı (epoch milisaniye) |
  | `totalMembers`             | Toplam ekip üyesi sayısı                       |
  | `totalPages`               | Toplam sayfa sayısı                            |
</div>

#### Örnek Yanıt

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
  #### Örnek istekler
</div>

**Temel harcama verileri:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u API_ANAHTARIN: \
  -H "İçerik Türü: application/json" \
  -d '{}'
```

**Belirli bir kullanıcıyı sayfalamayla ara:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u API_ANAHTARIN: \
  -H "İçerik-Tipi: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Kullanım Olayları Verilerini Al
</div>

Takımın için kapsamlı filtreleme, arama ve sayfalama seçenekleriyle ayrıntılı kullanım olaylarını getir. Bu uç nokta, tekil API çağrıları, model kullanımı, token tüketimi ve maliyetler hakkında daha ayrıntılı içgörüler sunar.

```
POST /teams/filtered-usage-events
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre   | Tip    | Gerekli | Açıklama                                       |
  | :---------- | :----- | :------ | :--------------------------------------------- |
  | `startDate` | number | Hayır   | Epoch milisaniye cinsinden başlangıç tarihi    |
  | `endDate`   | number | Hayır   | Epoch milisaniye cinsinden bitiş tarihi        |
  | `userId`    | number | Hayır   | Belirli kullanıcı kimliğine göre filtrele      |
  | `page`      | number | Hayır   | Sayfa numarası (1’den başlar). Varsayılan: `1` |
  | `pageSize`  | number | Hayır   | Sayfa başına sonuç sayısı. Varsayılan: `10`    |
  | `email`     | string | Hayır   | Kullanıcı e-posta adresine göre filtrele       |
</div>

#### Yanıt

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
    zamanDamgasi: string;
    model: string;
    tur: string;
    maxMode: boolean;
    istekMaliyetleri: number;
    isTokenBasedCall: boolean;
    belirteçKullanimi?: {
      girisBelirtecleri: number;
      cikisBelirtecleri: number;
      önbellekYazmaBelirtecleri: number;
      önbellekOkumaBelirtecleri: number;
      toplamSent: number;
    };
    isFreeBugbot: boolean;
    kullaniciEpostasi: string;
  }[];
  period: {
    baslangicTarihi: number;
    bitisTarihi: number;
  };
}
```

<div id="response-fields-explained">
  #### Yanıt Alanlarının Açıklaması
</div>

<div className="full-width-table">
  | Alan                    | Açıklama                                                           |
  | :---------------------- | :----------------------------------------------------------------- |
  | `totalUsageEventsCount` | Sorguyla eşleşen kullanım olaylarının toplam sayısı                |
  | `pagination`            | Sonuçlar arasında gezinmeye yönelik sayfalama üst verisi           |
  | `timestamp`             | Olay zaman damgası (epoch milisaniyeler)                           |
  | `model`                 | İstek için kullanılan yapay zeka modeli                            |
  | `kind`                  | Kullanım kategorisi (ör. "Usage-based", "Included in Business")    |
  | `maxMode`               | Maks modun etkin olup olmadığı                                     |
  | `requestsCosts`         | İstek birimleri cinsinden maliyet                                  |
  | `isTokenBasedCall`      | Olay kullanım bazlı olarak ücretlendirildiğinde true               |
  | `tokenUsage`            | Ayrıntılı token kullanımı (isTokenBasedCall true olduğunda mevcut) |
  | `isFreeBugbot`          | Bunun ücretsiz bugbot kullanımı olup olmadığı                      |
  | `userEmail`             | İsteği yapan kullanıcının e-posta adresi                           |
  | `period`                | Sorgulanan verinin tarih aralığı                                   |
</div>

#### Örnek Yanıt

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
      "kind": "Kullanıma göre",
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
      "kind": "Kullanıma göre",
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
      "kind": "Business’a dahil",
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

#### Örnek İstekler

**Varsayılan sayfalamayla tüm kullanım etkinliklerini getir:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Tarih aralığına ve belirli bir kullanıcıya göre filtrele:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "İçerik-Türü: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Özel sayfalama ile belirli bir kullanıcının kullanım etkinliklerini al:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u API_ANAHTARIN: \
  -H "İçerik Türü: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Kullanıcı Harcama Limitini Ayarla
</div>

Tek tek ekip üyeleri için harcama limitleri belirle. Böylece ekibindeki her kullanıcının AI kullanımı için ne kadar harcayabileceğini kontrol edebilirsin.

```
POST /teams/user-spend-limit
```

<Note>
  **Oran sınırlaması:** ekip başına dakikada 60 istek
</Note>

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre           | Tür    | Gerekli | Açıklama                                                         |
  | :------------------ | :----- | :------ | :--------------------------------------------------------------- |
  | `userEmail`         | string | Evet    | Ekip üyesinin e-posta adresi                                     |
  | `spendLimitDollars` | number | Evet    | Dolar cinsinden harcama limiti (yalnızca tam sayı, ondalık yok). |
</div>

<Note>
  * Kullanıcı zaten senin ekibinin bir üyesi olmalı
  * Yalnızca tam sayı değerleri kabul edilir (ondalık tutar kabul edilmez)
  * `spendLimitDollars` değerini 0 olarak ayarlamak limiti \$0 yapar
</Note>

#### Yanıt

Başarı ya da başarısızlığı belirten standart bir yanıt döndürür:

```typescript  theme={null}
{
  outcome: 'başarılı' | 'hata';
  message: string;
}
```

<div id="example-responses">
  #### Örnek Yanıtlar
</div>

**Limit başarıyla belirlendi:**

```json  theme={null}
{
  "outcome": "başarılı",
  "message": "developer@company.com kullanıcısının harcama limiti $100 olarak ayarlandı"
}
```

**Hata yanıtı:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Geçersiz e-posta formatı"
}
```

#### Örnek İstekler

**Harcama limiti belirle:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u API_ANAHTARIN: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

Takımın için dosya veya dizinlerin dizine alınmasını ya da bağlam olarak kullanılmasını önlemek üzere depolar ve eşleşme kalıpları ekle.

<div id="get-team-repo-blocklists">
  #### Takım Depo Engelleme Listelerini Al
</div>

Takımın için yapılandırılmış tüm depo engelleme listelerini al.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Yanıt
</div>

Bir dizi depo engelleme listesi (blocklist) nesnesi döndürür:

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
  ##### Örnek Yanıt
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
  ##### Örnek İstek
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u API_ANAHTARIN:
```

<div id="upsert-repo-blocklists">
  #### Repo Engelleme Listelerini (Blocklist) Yükselt/İçer
</div>

Sağlanan repolar için mevcut repo engelleme listelerini (blocklist) yenisiyle değiştir.
*Not: Bu uç nokta yalnızca sağlanan repoların desenlerini (pattern) geçersiz kılar. Diğer tüm repolar etkilenmeden kalır.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### İstek Gövdesi
</div>

| Parametre | Tür   | Gerekli | Açıklama                                     |
| --------- | ----- | ------- | -------------------------------------------- |
| repos     | array | Evet    | Depo engel listesi nesnelerinden oluşan dizi |

Her depo nesnesi şunları içermelidir:

| Alan     | Tür       | Gerekli | Açıklama                                                            |
| -------- | --------- | ------- | ------------------------------------------------------------------- |
| url      | string    | Evet    | Engel listesine eklenecek depo URL’si                               |
| patterns | string\[] | Evet    | Engellenecek dosya kalıplarının dizisi (glob kalıpları desteklenir) |

<div id="response">
  ##### Yanıt
</div>

Güncellenmiş depo engel listelerinin listesini döndürür:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Örnek İstek
</div>

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
  #### Depo Engelleme Listesinden Kaldır
</div>

Engelleme listesinden belirli bir depoyu kaldır.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parametreler
</div>

| Parametre | Tür    | Gerekli | Açıklama                                            |
| --------- | ------ | ------- | --------------------------------------------------- |
| repoId    | string | Evet    | Silinecek depo engel listesinin (blocklist) kimliği |

<div id="response">
  ##### Yanıt
</div>

Başarıyla silindiğinde 204 No Content döndürür.

<div id="example-request">
  ##### Örnek İstek
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u YOUR_API_KEY:
```

<div id="pattern-examples">
  #### Kalıp Örnekleri
</div>

Yaygın blocklist kalıpları:

* `*` - Tüm depoyu engelle
* `*.env` - Tüm .env dosyalarını engelle
* `config/*` - config dizinindeki tüm dosyaları engelle
* `**/*.secret` - Herhangi bir alt dizindeki tüm .secret dosyalarını engelle
* `src/api/keys.ts` - Belirli bir dosyayı engelle

---

← Previous: [Fiyatlandırma](./fiyatlandrma.md) | [Index](./index.md) | Next: [AI Kod Takip API'si](./ai-kod-takip-apisi.md) →