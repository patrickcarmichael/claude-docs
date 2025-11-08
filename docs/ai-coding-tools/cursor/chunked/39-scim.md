# SCIM

**Navigation:** [← Previous](./38-geliştiriciler.md) | [Index](./index.md) | [Next →](./40-recent-changes.md)

---

# SCIM
Source: https://docs.cursor.com/zh-Hant/account/teams/scim

設定 SCIM 佈建，自動化管理使用者與群組

<div id="overview">
  ## 概覽
</div>

SCIM 2.0 佈建可透過你的身分識別提供者自動管理團隊成員與目錄群組。適用於已啟用 SSO 的 Enterprise 方案。

<product_visual type="screenshot">
  SCIM 設定儀表板，顯示 Active Directory 管理設定
</product_visual>

<div id="prerequisites">
  ## 先決條件
</div>

* Cursor Enterprise 方案
* 必須先完成 SSO 設定 — **SCIM 需要一個已啟用的 SSO 連線**
* 你的身分識別提供者（Okta、Azure AD 等）的管理員存取權
* 你的 Cursor 組織的管理員存取權

<div id="how-it-works">
  ## 運作方式
</div>

<div id="user-provisioning">
  ### 使用者佈建
</div>

當使用者在身分識別供應商的 SCIM 應用被指派時，會自動加入 Cursor；解除指派時會被移除。變更會即時同步。

<div id="directory-groups">
  ### 目錄群組
</div>

目錄群組及其成員會從你的身分識別供應商同步。群組與使用者的管理必須透過你的身分識別供應商進行，Cursor 只會以唯讀方式顯示這些資訊。

<div id="spend-management">
  ### 支出管理
</div>

為每個目錄群組設定不同的每位使用者支出上限。目錄群組的上限優先於團隊層級的上限。同時屬於多個群組的使用者會套用最高的支出上限。

<div id="setup">
  ## 設定
</div>

<Steps>
  <Step title="確認已設定 SSO">
    SCIM 需要先完成 SSO 設定。若還沒設定 SSO，
    繼續之前先依照 [SSO 設定指南](/zh-Hant/account/teams/sso) 操作。
  </Step>

  <Step title="前往 Active Directory 管理">
    用管理員帳號前往
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)，
    或到你的儀表板設定並選擇
    「Active Directory Management」分頁。
  </Step>

  <Step title="開始設定 SCIM">
    SSO 驗證完成後，你會看到逐步的 SCIM 設定連結。點一下
    即可啟動設定精靈。
  </Step>

  <Step title="在身分提供者中設定 SCIM">
    在你的身分提供者中：- 建立或設定 SCIM 應用程式 - 使用
    Cursor 提供的 SCIM 端點與 Token - 啟用使用者與群組推送
    佈建 - 測試連線
  </Step>

  <Step title="設定支出上限（選填）">
    回到 Cursor 的 Active Directory 管理頁：- 檢視已同步的
    目錄群組 - 視需要為特定群組設定每位使用者的支出上限 -
    檢視同時屬於多個群組的使用者會套用哪些上限
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### 身分提供者設定
</div>

各提供者的設定指引：

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace 等的設定指南。
</Card>

<div id="managing-users-and-groups">
  ## 管理使用者與群組
</div>

<Warning>
  所有使用者與群組的管理都必須透過你的身分識別提供者進行。
  在身分識別提供者中所做的變更會自動同步到 Cursor，但
  你無法在 Cursor 內直接修改使用者或群組。
</Warning>

<div id="user-management">
  ### 使用者管理
</div>

* 在身分識別提供者中把使用者指派到你的 SCIM 應用程式即可新增使用者
* 在身分識別提供者中取消指派該 SCIM 應用程式即可移除使用者
* 使用者的個人資料變更（名稱、電子郵件）會自動從身分識別提供者同步

<div id="group-management">
  ### 群組管理
</div>

* 目錄群組會自動從你的身分識別提供者同步
* 群組成員變更會即時反映
* 用群組來組織使用者並設定不同的支出上限

<div id="spend-limits">
  ### 支出上限
</div>

* 可為每個目錄群組設定不同的每位使用者上限
* 使用者會從其所屬群組繼承最高的支出上限
* 群組上限會覆蓋預設的整個團隊每位使用者上限

<div id="faq">
  ## 常見問題
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### 為什麼我的儀表板沒有顯示 SCIM 管理？
</div>

在設定 SCIM 之前，先確認 SSO 已正確設定並正常運作。SCIM 需要有效的 SSO 連線才能運作。

<div id="why-arent-users-syncing">
  ### 為什麼使用者沒有同步？
</div>

確認使用者已在身分識別提供者中被指派到 SCIM 應用程式。使用者必須被明確指派，才會出現在 Cursor 中。

<div id="why-arent-groups-appearing">
  ### 為什麼群組沒有出現？
</div>

檢查身分識別提供者的 SCIM 設定中是否啟用了群組推送佈建。群組同步需要與使用者同步分開設定。

<div id="why-arent-spend-limits-applying">
  ### 為什麼花費上限沒有套用？
</div>

確認使用者在身分識別提供者中已正確被指派到預期的群組。群組成員身分會決定哪些花費上限會套用。

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### 我可以直接在 Cursor 管理 SCIM 使用者和群組嗎？
</div>

不行。所有使用者與群組的管理都必須透過身分識別提供者進行。Cursor 只會以唯讀方式顯示這些資訊。

<div id="how-quickly-do-changes-sync">
  ### 變更會多快同步？
</div>

在身分識別提供者中進行的變更會即時同步到 Cursor。大量批次作業可能會有短暫延遲。



# 快速上手
Source: https://docs.cursor.com/zh-Hant/account/teams/setup

建立並設定 Cursor 團隊

<div id="cursor-for-teams">
  ## Cursor for Teams
</div>

Cursor 適用於個人和團隊。Teams 方案為組織提供工具：SSO、團隊管理、存取控制，以及使用分析。

<div id="creating-a-team">
  ## 建立團隊
</div>

照著以下步驟建立團隊：

<Steps>
  <Step title="設定 Teams 方案">
    要建立 Team，請依這些步驟：

    1. **新用戶**：前往 [cursor.com/team/new-team](https://cursor.com/team/new-team) 建立新帳號與團隊
    2. **既有用戶**：到你的[儀表板](/zh-Hant/account/dashboard)並點擊「Upgrade to Teams」
  </Step>

  <Step title="輸入 Team 詳細資料">
    選擇 Team 名稱與計費週期

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="邀請成員">
    邀請團隊成員。使用者數會按比例計費——只需為成員實際加入的時間付費。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="啟用 SSO（選用）">
    為了安全與自動化導入，啟用 [SSO](/zh-Hant/account/teams/sso)。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="我的團隊使用 Zscaler／代理伺服器／VPN，Cursor 還能用嗎？">
    Cursor 預設使用 HTTP/2。部分代理與 VPN 可能會封鎖這個協定。

    在設定中啟用 HTTP/1.1 備援，以改用 HTTP/1.1。
  </Accordion>

  <Accordion title="要怎麼為公司購買授權？">
    Cursor 依「活躍使用者」計費，不是以席次計。你可以隨時新增或移除使用者——新成員會按剩餘時間比例計費。若被移除的使用者已有使用任何點數，他們的席次會持續占用，直到本計費週期結束。

    你的續約日期會維持不變。
  </Accordion>

  <Accordion title="我現在沒在用 Cursor，要怎麼建立團隊？">
    先把自己設為[未付費管理員](/zh-Hant/account/teams/members)，就能在沒有授權的情況下管理。

    <Warning>
      團隊至少需要一位付費成員。你可以先完成設定、邀請成員，然後在計費前把自己的角色改掉。
    </Warning>
  </Accordion>

  <Accordion title="要怎麼把 Cursor 加入公司 MDM？">
    各平台的下載連結都在 [cursor.com/downloads](https://cursor.com/downloads)。

    MDM 指南：

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html)（原 VMware）
    * [Microsoft Intune（Windows）](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune（Mac）](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



# SSO
Source: https://docs.cursor.com/zh-Hant/account/teams/sso

替你的團隊設定單一登入

<div id="overview">
  ## 概覽
</div>

Business 方案提供 SAML 2.0 SSO，無需額外費用。用現有的身分識別提供者（IdP）來驗證團隊成員，免去另外建立 Cursor 帳號的麻煩。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## 先決條件
</div>

* Cursor Team 計畫
* 身分識別提供者的管理員存取權（例如 Okta）
* Cursor 組織的管理員存取權

<div id="configuration-steps">
  ## 設定步驟
</div>

<Steps>
  <Step title="登入你的 Cursor 帳號">
    使用管理員帳號前往 [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings)。
  </Step>

  <Step title="找到 SSO 設定">
    找到「Single Sign-On (SSO)」區塊並展開。
  </Step>

  <Step title="開始設定流程">
    點擊「SSO Provider Connection settings」按鈕開始設定 SSO，依照精靈流程操作。
  </Step>

  <Step title="設定你的身分提供者">
    在你的身分提供者（例如 Okta）中：

    * 建立新的 SAML 應用程式
    * 使用 Cursor 提供的資訊設定 SAML
    * 設定 Just-in-Time（JIT）即時佈建
  </Step>

  <Step title="驗證網域">
    在 Cursor 中點擊「Domain verification settings」按鈕，驗證你的使用者網域。
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### 身分提供者設定指南
</div>

查看不同提供者的設定說明：

<Card title="身分提供者指南" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace 等的設定教學。
</Card>

<div id="additional-settings">
  ## 其他設定
</div>

* 在管理主控台管理 SSO 強制政策
* 新使用者透過 SSO 登入時會自動加入
* 由你的身分識別提供者（IdP）管理使用者

<div id="troubleshooting">
  ## 疑難排解
</div>

如果遇到問題：

* 確認網域已在 Cursor 完成驗證
* 確保已正確對應 SAML 屬性
* 檢查是否已在管理控制台啟用 SSO
* 確認身分提供者與 Cursor 的名字與姓氏相符
* 參考上方各身分提供者的指南
* 如果問題持續，聯絡 [hi@cursor.com](mailto:hi@cursor.com)



# 更新存取權限
Source: https://docs.cursor.com/zh-Hant/account/update-access

選擇你想接收更新的頻率

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

Cursor 有兩個更新頻道。

<Tabs>
  <Tab title="Default">
    預設的更新頻道，提供經過測試的版本。

    * 穩定版本
    * 來自預發布測試的錯誤修正
    * 所有使用者的預設選項
    * 團隊使用者僅能使用此選項

    <Note>
      Team 與 Business 帳戶使用 Default 模式。
    </Note>
  </Tab>

  <Tab title="Early Access">
    含有新功能的預發布版本。

    <Warning>
      Early Access 構建可能有 bug 或穩定性問題。
    </Warning>

    * 可搶先使用開發中的功能
    * 可能包含 bug
    * 不提供給團隊帳戶
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## 變更更新頻道
</div>

1. **開啟設定**：按下 <Kbd>Cmd+Shift+J</Kbd>
2. **前往 Beta**：在側邊欄選擇 Beta
3. **選擇頻道**：選擇 Default 或 Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

在 [Forum](https://forum.cursor.com) 回報 Early Access 的問題。



# Apply
Source: https://docs.cursor.com/zh-Hant/agent/apply

了解如何使用 Apply 從聊天中套用、接受或拒絕程式碼建議

<div id="how-apply-works">
  ## Apply 的運作方式
</div>

Apply 是一個專用的 Cursor 模型，會把聊天產生的程式碼整合進你的檔案。它會處理聊天對話中的程式碼區塊，並將變更套用到你的程式碼庫。

Apply 本身不會產生程式碼。由聊天模型負責產生程式碼，Apply 則負責把它整合到既有檔案中。它能處理跨多個檔案與大型程式碼庫的變更。

<div id="apply-code-blocks">
  ## 套用程式碼區塊
</div>

想套用某個程式碼區塊的建議，點一下該區塊右上角的播放按鈕就行了。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# 檢查點
Source: https://docs.cursor.com/zh-Hant/agent/chat/checkpoints

在 Agent 變更後儲存並還原先前狀態

檢查點會自動為 Agent 在你程式碼庫中的變更建立快照；需要時，你可以將 Agent 的修改復原。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## 還原檢查點
</div>

有兩種還原方式：

1. **從輸入欄**：在先前的請求上點擊 `Restore Checkpoint` 按鈕
2. **從訊息**：將滑鼠移到訊息上時，點擊 + 按鈕

<Warning>
  檢查點不是版本控制。需要永久記錄請用 Git。
</Warning>

<div id="how-they-work">
  ## 運作方式
</div>

* 本機儲存，與 Git 分離
* 僅追蹤 Agent 的變更（不包含手動編輯）
* 會自動清理

<Note>
  不會追蹤手動編輯。檢查點僅用於 Agent 的變更。
</Note>

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="檢查點會影響 Git 嗎？">
    不會。它們和 Git 的歷史是分開的。
  </Accordion>

  {" "}

  <Accordion title="會保留多久？">
    只在當前工作階段與近期歷史中保留，會自動清除。
  </Accordion>

  <Accordion title="可以手動建立嗎？">
    不行。它們會由 Cursor 自動建立。
  </Accordion>
</AccordionGroup>

{" "}



# 指令
Source: https://docs.cursor.com/zh-Hant/agent/chat/commands

定義指令以打造可重複使用的工作流程

自訂指令能讓你建立可重複使用的工作流程，並可在聊天輸入框中用簡單的「/」前綴觸發。這些指令有助於在團隊內標準化流程，並讓常見任務更有效率。

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  指令目前為測試版。隨著我們持續改進，功能與語法可能會有所變動。
</Info>

<div id="how-commands-work">
  ## 指令如何運作
</div>

指令是以純 Markdown 檔案定義，並可存放在兩個位置：

1. **專案指令**：存放在專案的 `.cursor/commands` 目錄
2. **全域指令**：存放在使用者家目錄的 `~/.cursor/commands` 目錄

當你在聊天輸入框輸入 `/` 時，Cursor 會自動偵測並顯示這兩個目錄中的可用指令，讓你在工作流程中立即存取。

<div id="creating-commands">
  ## 建立指令
</div>

1. 在專案根目錄建立 `.cursor/commands` 資料夾
2. 新增具描述性的 `.md` 檔名（例如：`review-code.md`、`write-tests.md`）
3. 用純 Markdown 撰寫內容，描述這個指令要做什麼
4. 當你輸入 `/` 時，指令會自動出現在聊天中

以下是指令資料夾的範例結構：

```
.cursor/
└── commands/
    ├── 回應-github-pr-評論.md
    ├── 程式碼審查清單.md
    ├── 建立-pr.md
    ├── 輕量檢視-現有差異.md
    ├── 新進開發者-入門.md
    ├── 執行所有測試並修正.md
    ├── 資安稽核.md
    └── 設定新功能.md
```

<div id="examples">
  ## 範例
</div>

在你的專案中試試這些指令，體驗它們的運作方式。

<AccordionGroup>
  <Accordion title="程式碼審查清單">
    ```markdown  theme={null}
    # 程式碼審查清單

    ## 概述
    用於進行詳盡程式碼審查的完整清單，確保品質、安全與可維護性。

    ## 審查類別

    ### 功能
    - [ ] 程式碼能達成預期行為
    - [ ] 已涵蓋邊界案例
    - [ ] 錯誤處理恰當
    - [ ] 無明顯錯誤或邏輯問題

    ### 程式碼品質
    - [ ] 程式碼可讀且結構良好
    - [ ] 函式精簡且聚焦
    - [ ] 變數名稱清楚具描述性
    - [ ] 無重複程式碼
    - [ ] 遵循專案慣例

    ### 安全性
    - [ ] 無明顯安全性弱點
    - [ ] 具備輸入驗證
    - [ ] 妥善處理敏感資料
    - [ ] 無硬編碼的機密
    ```
  </Accordion>

  <Accordion title="安全稽核">
    ```markdown  theme={null}
    # 安全稽核

    ## 概述
    全面性的安全審查，用於識別並修補程式碼庫中的弱點。

    ## 步驟
    1. **相依套件稽核**
       - 檢查已知漏洞
       - 更新過時套件
       - 檢閱第三方相依

    2. **程式碼安全審查**
       - 檢查常見漏洞
       - 檢閱身分驗證／存取授權
       - 稽核資料處理做法

    3. **基礎設施安全**
       - 檢閱環境變數
       - 檢查存取控制
       - 稽核網路安全

    ## 安全檢查清單
    - [ ] 相依套件已更新且安全
    - [ ] 無硬編碼密鑰／秘密
    - [ ] 已實作輸入驗證
    - [ ] 身分驗證安全
    - [ ] 存取授權設定正確
    ```
  </Accordion>

  <Accordion title="設定新功能">
    ```markdown  theme={null}
    # 設定新功能

    ## 概述
    從初始規劃到實作架構，系統化地設定一個新功能。

    ## 步驟
    1. **定義需求**
       - 釐清功能範圍與目標
       - 撰寫使用者故事與驗收標準
       - 規劃技術方案

    2. **建立功能分支**
       - 從 main/develop 分支出來
       - 設定本機開發環境
       - 設定任何新的相依項

    3. **規劃架構**
       - 設計資料模型與 API
       - 規劃 UI 元件與流程
       - 規劃測試策略

    ## 功能設定檢查清單
    - [ ] 需求已完成文件化
    - [ ] 使用者故事已撰寫
    - [ ] 技術方案已規劃
    - [ ] 功能分支已建立
    - [ ] 開發環境已就緒
    ```
  </Accordion>

  <Accordion title="建立 pull request">
    ```markdown  theme={null}
    # 建立 PR

    ## 概述
    建立一個結構完善的 Pull Request，包含清楚的說明、標籤與審查者。

    ## 步驟
    1. **準備分支**
       - 確保所有變更都已提交
       - 將分支推送到遠端
       - 確認分支已與 main 保持最新

    2. **撰寫 PR 說明**
       - 清楚摘要變更內容
       - 說明背景與動機
       - 列出任何破壞性變更
       - 若有 UI 變更請附上截圖

    3. **設定 PR**
       - 以具描述性的標題建立 PR
       - 加上合適的標籤
       - 指派審查者
       - 連結相關議題

    ## PR 範本
    - [ ] 功能 A
    - [ ] 錯誤修正 B
    - [ ] 單元測試通過
    - [ ] 手動測試完成
    ```
  </Accordion>

  <Accordion title="執行測試並修復失敗">
    ```markdown  theme={null}
    # 執行所有測試並修正失敗

    ## 概觀
    執行完整測試套件並有系統地修正任何失敗，確保程式碼品質與功能正確。

    ## 步驟
    1. **執行測試套件**
       - 執行專案中的所有測試
       - 擷取輸出並找出失敗項目
       - 同時檢查單元測試與整合測試

    2. **分析失敗**
       - 依類型分類：不穩定、故障、全新失敗
       - 依影響程度排定修復優先級
       - 檢查失敗是否與近期變更相關

    3. **系統性修正問題**
       - 先處理最嚴重的失敗
       - 一次修正一個問題
       - 每次修正後重新執行測試
    ```
  </Accordion>

  <Accordion title="讓新進開發者完成入職導覽">
    ```markdown  theme={null}
    # 新開發者入門

    ## 概述
    完整的入門流程，幫新開發者快速上手。

    ## 步驟
    1. **環境設定**
       - 安裝必要工具
       - 設定開發環境
       - 設定 IDE 與擴充套件
       - 設定 Git 與 SSH 金鑰

    2. **熟悉專案**
       - 檢視專案結構
       - 理解系統架構
       - 閱讀關鍵文件
       - 設定本機資料庫

    ## 入門檢查清單
    - [ ] 開發環境就緒
    - [ ] 所有測試皆通過
    - [ ] 能在本機執行應用程式
    - [ ] 資料庫已設定並可正常運作
    - [ ] 已提交第一個 PR
    ```
  </Accordion>
</AccordionGroup>



# 精簡
Source: https://docs.cursor.com/zh-Hant/agent/chat/compact

以精簡模式介面在聊天中節省空間

精簡模式透過減少視覺干擾並最大化可用空間，提供更俐落的聊天介面，讓對話更專注。

<div id="overview">
  ## 概覽
</div>

啟用後，精簡模式會將聊天介面調整為：

* **隱藏圖示**，呈現更乾淨、極簡的外觀
* **自動摺疊差異 (diff)**，減少視覺雜訊
* **自動摺疊輸入欄**，最大化對話空間

這個設定在使用小螢幕，或想要更專注、零干擾的聊天體驗時特別實用。

<div id="before-and-after">
  ## 前後對照
</div>

<div id="default-mode">
  ### 預設模式
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="預設模式的聊天介面，顯示所有圖示與展開的項目" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### 精簡模式
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="精簡模式的聊天介面，隱藏圖示並收合項目" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## 啟用精簡模式
</div>

要啟用精簡模式：

1. 打開 Cursor 設定
2. 前往 **Chat** 設定
3. 打開 **Compact Mode** 切換開關

介面會立即更新為更精簡的檢視，讓你有更多空間專注在對話上。



# 複製
Source: https://docs.cursor.com/zh-Hant/agent/chat/duplicate

從對話中的任意節點建立分支

複製或分支對話，探索不同解法，同時保留你目前的對話內容。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## 如何複製
</div>

1. 找到你想要分支的地方
2. 點擊該訊息上的三個點
3. 選擇「Duplicate Chat」

<div id="what-happens">
  ## 會發生什麼
</div>

* 會保留截至該時點的上下文
* 原始對話不會被改動
* 兩個聊天會各自維持獨立的歷史紀錄



# 匯出
Source: https://docs.cursor.com/zh-Hant/agent/chat/export

將對話匯出為 Markdown 格式

將 Agent 對話匯出為 Markdown 檔，方便分享或撰寫文件。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## 匯出內容
</div>

* 所有訊息與回覆
* 具語法高亮顯示的程式碼區塊
* 檔案引用與上下文
* 依時間順序的對話流程

<div id="how-to-export">
  ## 如何匯出
</div>

1. 前往要匯出的聊天
2. 點擊更多選單 →「Export Chat」
3. 將檔案儲存在本機

<Warning>
  匯出前請檢查是否包含敏感資料：API 金鑰、內部 URL、專有程式碼、
  個人資訊
</Warning>



# 歷程
Source: https://docs.cursor.com/zh-Hant/agent/chat/history

檢視與管理聊天記錄

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

在歷史面板中查看先前的 Agent 對話。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="聊天歷史" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## 開啟歷程
</div>

* 在 Agent 側邊欄點擊歷程圖示
* 按下 <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## 管理聊天
</div>

* **編輯標題**：點擊即可重新命名
* **刪除**：移除不需要的聊天
* **開啟**：點擊查看完整對話

聊天歷史會以 SQLite 資料庫的形式儲存在本機。

<Note>
  想保留聊天，請將它們[匯出](/zh-Hant/agent/chats/export)為 Markdown。
</Note>

<div id="background-agents">
  ## 背景代理
</div>

背景代理的對話不會出現在一般的歷史紀錄中，而是會被儲存在遠端資料庫。使用 <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> 查看。

<div id="referencing-past-chats">
  ## 參考過往聊天
</div>

使用 [@Past Chats](/zh-Hant/context/@-symbols/@-past-chats) 把之前聊天的上下文帶進目前的對話。



# 摘要化
Source: https://docs.cursor.com/zh-Hant/agent/chat/summarization

在聊天中管理長對話的上下文

<div id="message-summarization">
  ## 訊息摘要
</div>

隨著對話變長，Cursor 會自動摘要並管理上下文，讓聊天維持高效率。了解如何使用上下文選單，以及檔案如何被壓縮以適配模型的上下文視窗。

<div id="using-the-summarize-command">
  ### 使用 /summarize 指令
</div>

你可以在聊天中手動輸入 `/summarize` 指令來觸發摘要。這個指令能在對話過長時幫你管理上下文，讓你不會漏掉重要資訊，同時持續高效工作。

<Info>
  想更深入了解 Cursor 中上下文的運作方式，看看我們的 [Working with
  Context](/zh-Hant/guides/working-with-context) 指南。
</Info>

<div id="how-summarization-works">
  ### 摘要機制如何運作
</div>

當對話變長時，可能會超出模型的 context window 限制：

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Context window 限制</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

為了處理這件事，Cursor 會將較舊的訊息彙整成摘要，騰出空間給新的對話。

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Context window 限制
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          摘要內容
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## 檔案與資料夾濃縮
</div>

聊天摘要能處理長篇對話，不過 Cursor 在管理大型檔案與資料夾時採用的是另一套策略：**智慧濃縮**。當你在對話中加入檔案時，Cursor 會依據檔案大小與可用的上下文空間來決定最佳呈現方式。

以下是檔案／資料夾可能的各種狀態：

<div id="condensed">
  ### 精簡
</div>

當檔案或資料夾太大、塞不進 context window 時，Cursor 會自動將它們精簡。精簡後會把關鍵結構元素（例如函式簽名、類別、方法）呈現給模型。從這個精簡視圖，模型可以在需要時選擇展開特定檔案。這種做法能把可用的 context window 發揮到最大效益。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Context menu" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### 大幅精簡
</div>

當檔名帶有「大幅精簡」標籤時，表示該檔案過大，連精簡後也無法完整納入。模型只會看到檔名。

<div id="not-included">
  ### 未納入
</div>

當檔案或資料夾旁出現警告圖示時，表示該項目過大，無法納入 context 視窗，即使是經過壓縮/濃縮後也一樣。這有助於你了解程式碼庫中哪些部分是模型可以存取的。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# 分頁
Source: https://docs.cursor.com/zh-Hant/agent/chat/tabs

同時進行多個 Agent 對話

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

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## 概覽
</div>

按 <Kbd>Cmd+T</Kbd> 建立新分頁。每個分頁都會各自保留對話記錄、上下文和模型選擇。

<Tip>
  想並行處理工作流程，試試看 [Background Agents](/zh-Hant/background-agents)
</Tip>

<div id="managing-tabs">
  ## 管理分頁
</div>

* 用 <Kbd>Cmd+T</Kbd> 建立新分頁。每個分頁都會從全新的對話開始，並維持自己的上下文。

* 點擊分頁標題即可切換，或用 <Kbd>Ctrl+Tab</Kbd> 在分頁間循環切換。

* 分頁標題會在第一則訊息後自動產生，但你也可以在分頁標題上按右鍵重新命名。

<Tip>
  一個分頁處理一個任務，先把初始需求描述清楚，完成後記得關閉分頁，
  讓工作空間更有條理。
</Tip>

<div id="conflicts">
  ### 衝突
</div>

Cursor 會避免多個分頁同時編輯相同的檔案。系統會提示你解決衝突。

<div id="reference-other-chats">
  ## 參考其他對話
</div>

使用 [@Past Chats](/zh-Hant/context/@-symbols/@-past-chats) 把其他分頁或先前工作階段的上下文加入進來。



# 模式
Source: https://docs.cursor.com/zh-Hant/agent/modes

依任務選對模式——從自動化編碼到精準編輯

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

Agent 提供多種為特定任務最佳化的模式。每種模式都啟用不同的能力與工具，來符合你的工作流程需求。

<div className="full-width-table">
  | Mode                  | For      | Capabilities | Tools  |
  | :-------------------- | :------- | :----------- | :----- |
  | **[Agent](#agent)**   | 複雜功能、重構  | 自主探索、多檔案編輯   | 全部工具啟用 |
  | **[Ask](#ask)**       | 學習、規劃、提問 | 唯讀探索、不會自動變更  | 只有搜尋工具 |
  | **[Custom](#custom)** | 專業化工作流程  | 使用者自訂能力      | 可配置    |
</div>

<div id="agent">
  ## Agent
</div>

處理複雜程式開發任務的預設模式。Agent 會自主探索你的程式碼庫、編輯多個檔案、執行指令並修正錯誤，以完成你的請求。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

唯讀模式，用於學習與探索。Ask 會搜尋你的程式碼庫並提供答案，不會做任何變更——在修改前先搞懂程式碼再好不過。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## 自訂
</div>

用特定的工具組合和指示打造自己的模式。自由搭配功能，貼合你的工作流程。

<Note>
  自訂模式目前為測試版。到 `Cursor Settings` → `Chat` → `Custom
      Modes` 啟用
</Note>

<div id="examples">
  ### 範例
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **工具：** All Search\
    **指示：** 著重清楚、完整地解釋概念，並提出釐清式問題
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **工具：** Edit & Reapply **指示：** 改善程式碼結構，不新增任何功能
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **工具：** Codebase, Read file, Terminal **指示：** 在 `plan.md` 中撰寫詳細的
    實作計畫
  </Accordion>

  <Accordion title="Debug">
    **工具：** All Search, Terminal, Edit & Reapply\
    **指示：** 在提出修正前，先徹底調查問題
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## 切換模式
</div>

* 在 Agent 裡用模式選擇下拉選單
* 按 <Kbd>Cmd+.</Kbd> 就能快速切換
* 到[設定](#settings)裡自訂鍵盤快捷鍵

<div id="settings">
  ## 設定
</div>

所有模式共享一些設定選項：

<div className="full-width-table">
  | 設定                 | 說明           |
  | :----------------- | :----------- |
  | Model              | 選擇要使用的 AI 模型 |
  | Keyboard shortcuts | 設定在模式間切換的快捷鍵 |
</div>

各模式專屬設定：

<div className="full-width-table">
  | 模式         | 設定                            | 說明                                      |
  | :--------- | :---------------------------- | :-------------------------------------- |
  | **Agent**  | Auto-run 與 Auto-fix Errors    | 自動執行指令並修正錯誤                             |
  | **Ask**    | Search Codebase               | 自動搜尋並找到相關檔案                             |
  | **Custom** | Tool selection & Instructions | 設定 [tools](/zh-Hant/agent/tools) 與自訂提示詞 |
</div>



# 概覽
Source: https://docs.cursor.com/zh-Hant/agent/overview

協助自動化撰寫程式、執行終端指令與編輯程式碼的助理

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

Agent 是 Cursor 的助理，能獨立完成複雜的程式任務、執行終端指令，並編輯程式碼。可在側邊欄使用 <Kbd>Cmd+I</Kbd> 開啟。

<Frame caption="側邊欄中的 Agent">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/modes" className="hover:text-primary transition-colors">
          模式
        </a>
      </h2>

      <p className="text-sm">
        在 Agent、Ask 之間選擇，或建立自訂模式。每種模式都有不同的功能與工具，能配合你的工作流程。
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent 模式" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/tools" className="hover:text-primary transition-colors">
          工具
        </a>
      </h3>

      <p className="text-sm">
        Agent 會使用各種工具進行搜尋、編輯與執行命令。從語義程式碼庫
        搜尋到終端機執行，這些工具能支援自動化完成任務。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/apply" className="hover:text-primary transition-colors">
          套用變更
        </a>
      </h3>

      <p className="text-sm">
        把 AI 建議的程式碼區塊整合進你的程式碼庫。Apply 能在維持精準的同時，高效處理大規模變更。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="套用變更" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/review" className="hover:text-primary transition-colors">
          檢視差異
        </a>
      </h3>

      <p className="text-sm">
        在接受變更前先檢查。審閱介面以色彩標示新增與刪除的行，讓你更精準控管修改。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/chats/tabs" className="hover:text-primary transition-colors">
          聊天分頁
        </a>
      </h3>

      <p className="text-sm">
        用 <Kbd>Cmd+T</Kbd> 同時開多個對話。每個分頁都有自己的語境、歷史紀錄和模型設定。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          檢查點
        </a>
      </h3>

      <p className="text-sm">
        自動快照會追蹤 Agent 的變更。當變更未如預期，或想嘗試不同作法時，可以還原到先前狀態。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/terminal" className="hover:text-primary transition-colors">
          終端機整合
        </a>
      </h3>

      <p className="text-sm">
        Agent 會執行終端機指令、監控輸出，並處理多步驟流程。你可以為信任的工作流程設定自動執行，或要求確認以確保安全。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Terminal integration" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/chats/history" className="hover:text-primary transition-colors">
          聊天歷史
        </a>
      </h3>

      <p className="text-sm">
        按 <Kbd>Opt Cmd '</Kbd> 開啟過往對話。回顧先前的討論、追蹤程式開發工作階段，並參考較早聊天的脈絡。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat history" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/agent/chats/export" className="hover:text-primary transition-colors">
          匯出對話
        </a>
      </h3>

      <p className="text-sm">
        將對話匯出成 Markdown 格式。和團隊成員分享解法、記錄決策，或把開發工作階段整理成知識庫。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh-Hant/context/rules" className="hover:text-primary transition-colors">
          規則
        </a>
      </h3>

      <p className="text-sm">
        設定 Agent 的自訂指令與行為。規則能幫助維持程式碼
        標準、落實既定模式，並客製化 Agent 在你
        專案中的協作方式。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent 規則" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# 規劃
Source: https://docs.cursor.com/zh-Hant/agent/planning

Agent 如何透過待辦事項與佇列來規劃並管理複雜任務

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

Agent 可以透過結構化的待辦清單和訊息佇列來預先規劃並管理複雜任務，讓長期任務更容易理解和追蹤。

<div id="agent-to-dos">
  ## Agent 待辦事項
</div>

Agent 會把較長的任務拆解成可管理、具相依性的步驟，建立一個會隨進度更新的結構化計畫。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### 運作方式
</div>

* Agent 會自動為複雜任務建立待辦清單
* 每個項目都可以設定對其他任務的相依性
* 清單會隨著進度即時更新
* 已完成的任務會自動勾選

<div id="visibility">
  ### 可見性
</div>

* 待辦事項會顯示在聊天介面中
* 如果已設定 [Slack 整合](/zh-Hant/slack)，待辦事項也會顯示在那裡
* 隨時都能檢視完整的任務拆解

<Tip>
  為了更好的規劃，把最終目標描述清楚。Agent 了解完整範圍時，
  會產生更精準的任務拆解。
</Tip>

<Note>目前自動模式不支援規劃與待辦事項。</Note>

<div id="queued-messages">
  ## 佇列中的訊息
</div>

當 Agent 正在處理目前任務時，把後續訊息排進佇列。你的指示會在佇列中等待，並在準備好時自動執行。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### 使用佇列
</div>

1. 當 Agent 工作中時，輸入你的下一個指示
2. 按下 <Kbd>Ctrl+Enter</Kbd> 加入佇列
3. 訊息會依序顯示在目前任務的下方
4. 點擊箭頭重新排序已排隊的訊息
5. Agent 完成後會按序處理它們

<div id="override-the-queue">
  ### 覆寫佇列
</div>

想把訊息加入佇列而不是用預設傳送，就用 <Kbd>Ctrl+Enter</Kbd>。想立即傳送、不進佇列，就用 <Kbd>Cmd+Enter</Kbd>。這會「強制推送」你的訊息，略過佇列並立即執行。

<div id="default-messaging">
  ## 預設訊息傳遞
</div>

在預設情況下，訊息會盡快送出，通常會在 Agent 完成一次工具呼叫後立即出現。這能帶來最即時的互動體驗。

<div id="how-default-messaging-works">
  ### 預設訊息傳遞的運作方式
</div>

* 你的訊息會被附加在聊天室中最近的一則使用者訊息後面
* 訊息通常會附在工具結果之後，並在就緒時立即送出
* 這能在不打斷 Agent 目前工作的情況下，讓對話流程更自然
* 預設情況下，當 Agent 正在工作時按下 Enter，就會採用這種方式送出



# 差異與審查
Source: https://docs.cursor.com/zh-Hant/agent/review

審查並管理由 AI 代理人產生的程式碼變更

當 Agent 產生程式碼變更時，會在審查介面中呈現，並以顏色區分新增與刪除的行。這讓你可以檢視並精確控制要套用到程式碼庫的變更。

審查介面會以熟悉的 diff 格式顯示程式碼變更：

<div id="diffs">
  ## 差異
</div>

<div className="full-width-table">
  | Type              | 意義        | 範例                                                                                                    |
  | :---------------- | :-------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | 新增的程式碼    | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | 刪除的程式碼    | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | 未變更的周邊程式碼 | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## 審查
</div>

產生完成後，會出現提示，讓你在繼續之前先審查所有變更。這能讓你快速掌握哪些內容會被修改。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Review input interface" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### 逐檔審查
</div>

螢幕底部會出現一個浮動審查列，讓你可以：

* 對目前檔案的變更進行**接受**或**拒絕**
* 導覽到有待處理變更的**下一個檔案**
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Your browser does not support the video tag.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### 選擇性接受
</div>

想要更細緻的控制：

* 若要接受大部分變更：先拒絕不要的行，然後點擊**全部接受**
* 若要拒絕大部分變更：先接受想要的行，然後點擊**全部拒絕**

<div id="review-changes">
  ## 檢視變更
</div>

在 agent 回應的最後，點一下 **Review changes** 按鈕就能看到完整的差異（diff）。

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/zh-Hant/agent/terminal

自動在代理執行流程中運行終端機指令

Agent 會在 Cursor 的原生終端機中執行指令並保留指令歷史。點一下「skip」就會送出 <kbd>Ctrl+C</kbd> 來中斷指令。

<div id="troubleshooting">
  ## 疑難排解
</div>

<Info>
  某些 shell 主題（例如 Powerlevel9k/Powerlevel10k）可能會影響
  內嵌終端機輸出。若指令輸出看起來被截斷或
  格式跑版，Agent 執行時請停用該主題或改用更簡單的提示。
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### 在 Agent 工作階段停用高負載的提示
</div>

在 shell 設定中使用 `CURSOR_AGENT` 環境變數來偵測
Agent 是否正在執行，並略過初始化華麗的提示/主題。

```zsh  theme={null}

# ~/.zshrc — 在 Cursor Agent 執行時停用 Powerlevel10k
if [[ -n "$CURSOR_AGENT" ]]; then
  # 為提高相容性，略過主題初始化
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — 在 Agent 工作階段中退回到簡易提示字元
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Tools
Source: https://docs.cursor.com/zh-Hant/agent/tools

可供代理在搜尋、編輯與執行程式碼時使用的工具

列出 [Agent](/zh-Hant/agent/overview) 各模式可用的所有工具。你在建立自己的[自訂模式](/zh-Hant/agent/modes#custom)時，可以啟用或停用它們。

<Note>
  Agent 在執行任務時呼叫工具的次數沒有上限，會視需要持續使用工具來完成你的請求。
</Note>

<div id="search">
  ## 搜尋
</div>

用來在程式碼庫與網路上找出相關資訊的工具。

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    讀取單一檔案最多 250 行（最大模式可到 750 行）。
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    讀取目錄結構，但不讀取檔案內容。
  </Accordion>

  <Accordion title="Codebase" icon="database">
    在已[索引的程式碼庫](/zh-Hant/context/codebase-indexing)內進行語意搜尋。
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    在檔案中搜尋精確關鍵字或樣式。
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    以檔名搭配模糊比對尋找檔案。
  </Accordion>

  <Accordion title="Web" icon="globe">
    產生搜尋字串並執行網路搜尋。
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    依類型與描述擷取特定[規則](/zh-Hant/context/rules)。
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## 編輯
</div>

用來對檔案與程式碼庫做特定修改的工具。

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    提出對檔案的修改建議，並自動[套用](/zh-Hant/agent/apply)。
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    自動刪除檔案（可在設定中停用）。
  </Accordion>
</AccordionGroup>

<div id="run">
  ## 執行
</div>

Chat 可以和你的終端機互動。

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    執行終端機指令並監看輸出。
  </Accordion>
</AccordionGroup>

<Note>預設情況下，Cursor 會使用第一個可用的終端機設定檔。</Note>

設定你偏好的終端機設定檔：

1. 開啟指令選單（Command Palette，`Cmd/Ctrl+Shift+P`）
2. 搜尋「Terminal: Select Default Profile」
3. 選擇你要的設定檔

<div id="mcp">
  ## MCP
</div>

Chat 可以使用已設定的 MCP 伺服器與外部服務互動，例如資料庫或第三方 API。

<AccordionGroup>
  <Accordion title="切換 MCP 伺服器" icon="server">
    切換可用的 MCP 伺服器。會遵循自動執行設定。
  </Accordion>
</AccordionGroup>

進一步了解 [Model Context Protocol](/zh-Hant/context/model-context-protocol)，並在 [MCP 目錄](/zh-Hant/tools) 中探索可用伺服器。

<div id="advanced-options">
  ## 進階選項
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    自動套用編輯，無需手動確認。
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    自動執行終端機指令並套用編輯。適合用來執行測試套件並驗證變更。

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    設定允許清單，指定哪些工具可以自動執行。透過明確定義允許的操作，允許清單能提升安全性。
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Agent 遇到時自動修正 linter 錯誤與警告。
  </Accordion>
</AccordionGroup>



# 背景代理
Source: https://docs.cursor.com/zh-Hant/background-agent

Cursor 中的非同步遠端代理

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

使用 background agents，在遠端環境中啟動非同步代理來編輯和執行程式碼。隨時查看它們的狀態、發送後續指示，或直接接手。

<div id="how-to-use">
  ## 如何使用
</div>

有兩種方式可以使用背景代理：

1. **Background Agent Sidebar**：在原生 Cursor 側邊欄的背景代理分頁中，檢視與你帳號關聯的所有背景代理、搜尋現有代理，並啟動新的代理。
2. **Background Agent Mode**：按下 <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> 以在 UI 中啟用背景代理模式。

提交提示後，從清單中選擇你的代理即可查看狀態並進入機器。

<Note>
  <p className="!mb-0">
    背景代理需要保留數天的資料。
  </p>
</Note>

<div id="setup">
  ## 設定
</div>

Background agents 會在預設的隔離式 Ubuntu 基礎機器上執行。這些代理具備網路連線能力，並可安裝套件。

<div id="github-connection">
  #### GitHub 連線
</div>

背景代理會從 GitHub 取得並 clone 你的 repo，然後在獨立分支上作業，並將變更 push 回你的 repo，方便交接。

請授予你的 repo（以及任何相依的 repo 或子模組）讀寫權限。未來我們也會支援其他供應商（GitLab、Bitbucket 等）。

<div id="ip-allow-list-configuration">
  ##### IP 允許清單設定
</div>

如果你的組織有使用 GitHub 的 IP 允許清單功能，你需要為背景代理程式設定存取權限。請參考 [GitHub 整合文件](/zh-Hant/integrations/github#ip-allow-list-configuration) 以取得完整的設定說明，包括聯絡資訊與 IP 位址。

<div id="base-environment-setup">
  #### 基礎環境設定
</div>

進階情境下，自己動手設定環境。先準備一個連到遠端機器的 IDE 執行個體。把你的機器設好、安裝工具和套件，然後建立快照。接著設定執行階段參數：

* Install 指令會在代理啟動前執行，用來安裝執行階段相依項。這可能是跑 `npm install` 或 `bazel build`。
* Terminals 會在代理運作時執行背景程序——例如啟動網頁伺服器或編譯 protobuf 檔案。

在最進階的情境，使用 Dockerfile 來做機器設定。Dockerfile 讓你設定系統層級相依：安裝特定版本的編譯器、除錯器，或更換基底作業系統映像。不要 `COPY` 整個專案——我們會管理工作區並檢出正確的 commit。相依安裝還是放在 install 指令的腳本裡處理。

輸入開發環境需要的任何機密——這些會以靜態加密（使用 KMS）儲存在我們的資料庫中，並在背景代理環境中提供。

機器設定位於 `.cursor/environment.json`，可以提交到你的 repo（建議）或私下儲存。設定流程會引導你建立 `environment.json`。

<div id="maintenance-commands">
  #### 維護指令
</div>

在設定新機器時，我們會從基礎環境開始，接著執行你 `environment.json` 中的 `install` 指令。這個指令等同於開發者在切換分支時會執行的動作—安裝任何新的相依套件。

對大多數人來說，`install` 指令就是 `npm install` 或 `bazel build`。

為了讓機器能快速啟動，我們會在 `install` 指令執行後快取磁碟狀態。請把它設計成可重複執行。只有 `install` 指令產生的磁碟狀態會被保留—在這裡啟動的行程在代理程式啟動時不會存在。

<div id="startup-commands">
  #### 啟動指令
</div>

執行 `install` 之後，機器會啟動，接著我們會執行 `start` 指令，然後啟動所有 `terminals`。這會啟動在代理執行期間應該保持運行的程序。

`start` 指令通常可以略過。只有在你的開發環境依賴 Docker 時才使用它——在 `start` 指令中放入 `sudo service docker start`。

`terminals` 是用來跑應用程式的程式碼。這些終端機會在一個 `tmux` 工作階段中執行，供你和代理使用。比如，很多網站的 repo 會把 `npm run watch` 放在一個 terminal 裡。

<div id="the-environmentjson-spec">
  #### `environment.json` 規格
</div>

`environment.json` 檔案可能長這樣：

```json  theme={null}
{
  "snapshot": "從設定載入"
  "install": "npm install"
  "terminals": [
    {
      "name": "執行 Next.js"
      "command": "npm run dev"
    }
  ]
}
```

正式來說，這份規格[定義在這裡](https://www.cursor.com/schemas/environment.schema.json)。

<div id="models">
  ## 模型
</div>

只有支援 [Max Mode](/zh-Hant/context/max-mode) 的模型能用於背景代理。

<div id="pricing">
  ## 價格
</div>

進一步了解 [Background Agent 的價格](/zh-Hant/account/pricing#background-agent)。

<div id="security">
  ## 安全性
</div>

Background Agents 可在隱私模式中使用。我們絕不會用你的程式碼進行訓練，且只會為了執行 agent 而暫存程式碼。[進一步了解隱私模式](https://www.cursor.com/privacy-overview)。

你應該知道：

1. 為想編輯的 repo 授予我們的 GitHub 應用程式讀寫權限。我們會用這個權限來 clone 該 repo 並進行修改。
2. 你的程式碼會在我們的 AWS 基礎設施中、彼此隔離的 VM 內執行，並在 agent 可存取期間儲存在 VM 磁碟上。
3. agent 可存取網際網路。
4. agent 會自動執行所有終端機指令，讓它能反覆跑測試。這和前景 agent 不同，後者每個指令都需要使用者核准。自動執行會帶來資料外洩風險：攻擊者可能發動提示注入攻擊，誘使 agent 將程式碼上傳到惡意網站。參見 [OpenAI 對背景 agent 提示注入風險的說明](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access)。
5. 如果關閉隱私模式，我們會收集提示與開發環境資料以改進產品。
6. 如果在啟動背景 agent 時關閉隱私模式，之後在 agent 執行期間再啟用，agent 仍會以關閉的隱私模式持續執行直到完成。

<div id="dashboard-settings">
  ## 儀表板設定
</div>

Workspace 管理員可以在儀表板的 Background Agents 分頁中設定其他選項。

<div id="defaults-settings">
  ### 預設設定
</div>

* **預設模型** – 在執行未指定模型時會使用的模型。選擇任何支援 Max 模式的模型。
* **預設儲存庫** – 留空時，代理會請你選擇儲存庫。在這裡先指定就能跳過這個步驟。
* **基礎分支** – 代理在建立 Pull Request 時要從哪個分支分岔。留空則使用該儲存庫的預設分支。

<div id="security-settings">
  ### 安全性設定
</div>

所有安全性選項都需要管理員權限。

* **使用者限制** – 選擇 *None*（所有成員都能啟動背景代理）或 *Allow list*。若設為 *Allow list*，你可以精確指定哪些隊友能建立代理。
* **團隊後續** – 開啟後，工作區內任何人都能為他人啟動的代理新增後續訊息；關閉則僅限代理擁有者與管理員能新增後續。
* **顯示代理摘要** – 控制 Cursor 是否顯示代理的檔案差異圖與程式碼片段。若不想在側邊欄曝光檔案路徑或程式碼，請停用此項。
* **在外部頻道顯示代理摘要** – 將前述切換擴展到 Slack 或你已連結的任何外部頻道。

變更會即時儲存，並立即套用到新建立的代理。



# 新增後續指令
Source: https://docs.cursor.com/zh-Hant/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
向執行中的背景代理傳送額外指令。




# 代理對話
Source: https://docs.cursor.com/zh-Hant/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
取得背景代理的對話記錄。

如果背景代理已被刪除，就無法存取該對話。



# 代理狀態
Source: https://docs.cursor.com/zh-Hant/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
取得特定背景代理的目前狀態與結果。




# API 金鑰資訊
Source: https://docs.cursor.com/zh-Hant/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
取得用於身分驗證的 API 金鑰中繼資料。




# 刪除代理
Source: https://docs.cursor.com/zh-Hant/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
永久刪除背景代理及其相關資源。




# 啟動 Agent
Source: https://docs.cursor.com/zh-Hant/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
啟動新的背景 Agent，在你的儲存庫上開始工作。




# 列出代理
Source: https://docs.cursor.com/zh-Hant/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
取得已驗證使用者的所有背景代理之分頁清單。




# 列出模型
Source: https://docs.cursor.com/zh-Hant/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
取得適用於背景代理的推薦模型清單。

如果想在建立背景代理時指定模型，可以用這個端點查看推薦的模型清單。

同時也建議提供「Auto」選項。這樣在建立端點就不用傳模型名稱，
我們會自動挑選最合適的模型。



# 列出 GitHub 儲存庫
Source: https://docs.cursor.com/zh-Hant/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
取得已驗證使用者可存取的 GitHub 儲存庫清單。

<Warning>
  **此端點有非常嚴格的速率限制。**

  將請求限制為 **1 次 / 使用者 / 分鐘**，以及 **30 次 / 使用者 / 小時。**

  對於可存取許多儲存庫的使用者，此請求可能需要數十秒才會回應。

  務必妥善處理這項資訊暫時無法取得的情況。
</Warning>



# 概覽
Source: https://docs.cursor.com/zh-Hant/background-agent/api/overview

以程式方式建立並管理在你倉庫中運作的背景代理

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">測試版</Badge>

Background Agents API 讓你能以程式方式建立與管理能在你的儲存庫中自動運作的 AI 程式碼代理。
你可以用這個 API 自動回應使用者回饋、修復 bug、更新文件，還有更多！

<Info>
  Background Agents API 目前是測試版，我們很想聽聽你的回饋！
</Info>

<div id="key-features">
  ## 主要功能
</div>

* **自動產生程式碼** - 建立能理解你提示並直接修改程式碼庫的代理
* **儲存庫整合** - 可直接操作 GitHub 儲存庫
* 後續提示 - 替正在執行的代理加入額外指示
* **依使用量計費** - 只為實際使用的權杖付費
* **可擴充** - 每個 API 金鑰最多支援 256 個同時啟用的代理

<div id="quick-start">
  ## 快速開始
</div>

<div id="1-get-your-api-key">
  ### 1. 取得你的 API 金鑰
</div>

**前往** [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) 來建立你的 API 金鑰。

<div id="2-start-using-the-api">
  ### 2. 開始使用 API
</div>

所有 API 端點皆相對於：

```
https://api.cursor.com
```

前往 [API 參考](/zh-Hant/background-agent/api/launch-an-agent) 查看完整的端點列表。

<div id="authentication">
  ## 驗證
</div>

所有 API 請求都必須使用 Bearer 權杖進行驗證：

```
Authorization: Bearer 你的 API 金鑰
```

API 金鑰是在 [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations) 建立的。金鑰會與你的帳號綁定，並授予你建立與管理代理的權限（受限於你的方案與儲存庫存取權）。

<div id="pricing">
  ## 價格
</div>

API 目前為 beta 階段，計費與 Background Agents 相同。隨著我們擴大服務規模，價格可能會調整。請參考 [Background Agents 計費](/zh-Hant/account/pricing#background-agent)。

<div id="next-steps">
  ## 下一步
</div>

* 閱讀主要的 [Background Agents 概覽](/zh-Hant/background-agent)，了解環境、權限與工作流程。
* 從 [網頁與行動裝置](/zh-Hant/background-agent/web-and-mobile) 試用 Background Agents。
* 加入 [Discord #background-agent](https://discord.gg/jfgpZtYpmb) 的討論，或來信 [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com)。



# Webhooks
Source: https://docs.cursor.com/zh-Hant/background-agent/api/webhooks

即時接收背景代理程式狀態變更通知

<div id="webhooks">
  # Webhooks
</div>

當你用 webhook URL 建立 agent 時，Cursor 會送出 HTTP POST 請求來通知狀態變更。目前只支援 `statusChange` 事件，也就是在 agent 進入 `ERROR` 或 `FINISHED` 狀態時。

<div id="webhook-verification">
  ## Webhook 驗證
</div>

為了確保 webhook 請求確實來自 Cursor，驗證每個請求所附帶的簽名：

<div id="headers">
  ### Headers
</div>

每個 webhook 請求都會包含以下標頭：

* **`X-Webhook-Signature`** – 含有 HMAC-SHA256 簽名，格式為 `sha256=<hex_digest>`
* **`X-Webhook-ID`** – 此次投遞的唯一識別碼（用於記錄很實用）
* **`X-Webhook-Event`** – 事件類型（目前僅有 `statusChange`）
* **`User-Agent`** – 固定為 `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### 簽名驗證
</div>

要驗證 webhook 簽名，先計算預期的簽名，然後與收到的簽名比對：

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' +
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

計算簽章時，一律使用原始請求主體（在任何解析之前）。

<div id="payload-format">
  ## 負載格式
</div>

Webhook 會以 JSON 傳送負載，其結構如下：

```json  theme={null}
{
  "event": "狀態變更",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "完成",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "新增含安裝說明的 README.md"
}
```

請注意，部分欄位為選填，僅在有資料時才會包含。

<div id="best-practices">
  ## 最佳實務
</div>

* **驗證簽章** – 一定要驗證 webhook 簽章，確保請求來自 Cursor
* **處理重試** – 如果你的端點回傳錯誤狀態碼，webhook 可能會重試
* **快速回應** – 盡快回傳 2xx 狀態碼
* **使用 HTTPS** – 在正式環境務必為 webhook 端點使用 HTTPS URL
* **儲存原始內容** – 儲存原始 webhook 載荷，用於除錯與後續驗證



# Web 與行動
Source: https://docs.cursor.com/zh-Hant/background-agent/web-and-mobile

從任何裝置啟動程式代理，順暢接續到桌面端

<div id="overview">
  ## 概覽
</div>

Cursor 的網頁版 Agent 把強大的程式輔助帶到每台裝置。無論是散步時用手機，還是在瀏覽器裡工作，現在都能啟動在背景運行的強大程式代理。
等它們完成後，就在 Cursor 裡接手成果、檢視並合併變更，或把連結分享給團隊一起協作。

前往 [cursor.com/agents](https://cursor.com/agents) 開始使用。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor 網頁版 Agent 介面" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## 入門
</div>

<div id="quick-setup">
  ### 快速設定
</div>

1. **開啟網頁版**：在任何裝置上前往 [cursor.com/agents](https://cursor.com/agents)
2. **登入**：用你的 Cursor 帳號登入
3. **連接 GitHub**：連結你的 GitHub 帳號以存取儲存庫
4. **啟動第一個代理**：輸入任務，看看代理怎麼開始動工

<div id="mobile-installation">
  ### 行動裝置安裝
</div>

想要最佳行動體驗，把 Cursor 安裝成漸進式網頁應用程式（PWA）：

* **iOS**：在 Safari 開啟 [cursor.com/agents](https://cursor.com/agents)，點分享按鈕，然後選「加入主畫面」
* **Android**：用 Chrome 開啟該網址，點選單，然後選「加入主畫面」或「安裝應用程式」

<Tip>
  以 PWA 安裝可提供接近原生的使用體驗，包含：- 全螢幕介面 - 更快的啟動速度 - 主畫面的 App 圖示
</Tip>

<div id="working-across-devices">
  ## 跨裝置協作
</div>

Web 與 Mobile Agent 可無縫配合你的桌面工作流程；點擊「Open in Cursor」就能在 IDE 繼續讓 agent 作業。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review and handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### 團隊協作
</div>

* **共享存取**：把連結分享給團隊成員，一起協作執行 agent 任務。
* **審查流程**：協作者可以檢視差異（diffs）並提供回饋。
* **Pull Request 管理**：可直接在網頁介面建立、審查與合併 Pull Requests。

<div id="slack-integration">
  ### Slack 整合
</div>

在 Slack 中提及 `@Cursor` 就能直接觸發 agents；而從網頁或行動端啟動 agents 時，也可以選擇在完成後接收 Slack 通知。

<Card title="在 Slack 中使用 Cursor" icon="slack" href="/zh-Hant/slack">
  進一步了解如何設定與使用 Slack 整合，包括
  觸發 agents 以及接收通知。
</Card>

<div id="pricing">
  ## 定價
</div>

Web 與行動代理的計費模式與 Background Agents 相同。

想了解更多，請參考 [Background Agent 計費](/zh-Hant/account/pricing#background-agent)。

<div id="troubleshooting">
  ## 疑難排解
</div>

<AccordionGroup>
  <Accordion title="無法啟動 Agent 執行">
    * 確保你已登入並已連結 GitHub 帳號。- 檢查你是否擁有必要的儲存庫權限 - 你也需要是 Pro 試用或付費方案，並啟用按使用量計費。要啟用按使用量計費，前往
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) 的設定分頁。
  </Accordion>

  <Accordion title="行動裝置看不到 Agent 執行">
    試著重新整理頁面或清除瀏覽器快取。也請確認你在各裝置使用的是同一個帳號。
  </Accordion>

  <Accordion title="Slack 整合無法使用">
    確認你的工作區管理員已安裝 Cursor 的 Slack 應用，且你具備相應權限。
  </Accordion>
</AccordionGroup>



# Bugbot
Source: https://docs.cursor.com/zh-Hant/bugbot

針對 Pull Request 的 AI 程式碼審查

Bugbot 會審查 Pull Request，找出錯誤、資安風險，以及程式碼品質問題。

<Tip>
  Bugbot 提供免費方案：每位使用者每月可享有一定數量的免費 PR 審查。達到上限後，審查會暫停至下一個計費週期。隨時都能升級為 14 天 Pro 版免費試用，享有無限次審查（受標準濫用防護機制約束）。
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot 在 PR 上留下評論" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## 運作方式
</div>

Bugbot 會分析 PR 差異，並在評論中提供說明與修正建議。它會在每次 PR 更新時自動執行，或在手動觸發時執行。

* 在每次 PR 更新時執行**自動審查**
* 在任何 PR 留下 `cursor review` 或 `bugbot run` 評論即可**手動觸發**
* **在 Cursor 中修復** 連結會直接在 Cursor 中開啟問題
* **在 Web 中修復** 連結會直接在 [cursor.com/agents](https://cursor.com/agents) 開啟問題

<div id="setup">
  ## 設定
</div>

需要 Cursor 管理員權限和 GitHub 組織管理員權限。

1. 前往 [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. 切換到 Bugbot 分頁
3. 點選 `Connect GitHub`（若已連線則為 `Manage Connections`）
4. 依指示完成 GitHub 安裝流程
5. 回到儀表板，在指定的儲存庫啟用 Bugbot

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot 的 GitHub 設定" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="setup">
  ## 設定
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### 儲存庫設定

    從你的安裝清單中為每個儲存庫啟用或停用 Bugbot。Bugbot 只會在你建立的 PR 上執行。

    ### 個人設定

    * 只在被提及時執行，透過留言 `cursor review` 或 `bugbot run`
    * 每個 PR 只執行一次，略過後續提交
  </Tab>

  <Tab title="Team">
    ### 儲存庫設定

    團隊管理員可以為每個儲存庫啟用 Bugbot、設定審查者的允許/拒絕清單，並設定：

    * 每個安裝在每個 PR 上只執行一次，略過後續提交
    * 停用行內審查，避免 Bugbot 直接在程式碼行上留言

    Bugbot 會在已啟用的儲存庫中對所有貢獻者運作，無論是否為團隊成員。

    ### 個人設定

    團隊成員可以覆寫自己 PR 的設定：

    * 只在被提及時執行，透過留言 `cursor review` 或 `bugbot run`
    * 每個 PR 只執行一次，略過後續提交
    * 在草稿 PR 啟用審查，將草稿 PR 納入自動審查
  </Tab>
</Tabs>

<div id="analytics">
  ### 數據分析
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot 儀表板" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## 規則
</div>

建立 `.cursor/BUGBOT.md` 檔案，提供專案層級的審查背景。Bugbot 會自動包含根目錄的 `.cursor/BUGBOT.md`，並在從變更的檔案往上遍歷時，連同找到的其他檔案一併納入。

```
project/
  .cursor/BUGBOT.md          # 一律包含（專案層級規則）
  backend/
    .cursor/BUGBOT.md        # 檢視後端檔案時會包含
    api/
      .cursor/BUGBOT.md      # 檢視 API 檔案時會包含
  frontend/
    .cursor/BUGBOT.md        # 檢視前端檔案時會包含
```

<AccordionGroup>
  <Accordion title="範例 .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # 專案審查準則

    ## 安全性重點

    - 在 API 端點驗證使用者輸入
    - 檢查資料庫查詢是否有 SQL 注入漏洞
    - 確保受保護的路由具備正確的身分驗證

    ## 架構模式

    - 對服務使用相依性注入
    - 在資料存取層採用 Repository 模式
    - 以自訂錯誤類別實作完善的錯誤處理

    ## 常見問題

    - React 元件記憶體洩漏（檢查 useEffect 的清理邏輯）
    - UI 元件缺少錯誤邊界
    - 命名規範不一致（函式使用 camelCase）

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## 計費方案
</div>

Bugbot 提供兩種方案：**Free** 和 **Pro**。

<div id="free-tier">
  ### 免費方案
</div>

每位使用者每月都有一定次數的免費 PR 審查。團隊的話，每位成員都有自己的免費審查額度。達到上限後，審查會暫停，直到下一個計費週期。隨時都能升級為 14 天免費的 Pro 試用，享有不限次數的審查。

<div id="pro-tier">
  ### 專業方案
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### 固定費率

    每月 \$40，可在所有儲存庫中對每月最多 200 個 PR 進行不限次數的 Bugbot 審查。

    ### 開始使用

    透過你的帳戶設定訂閱。
  </Tab>

  <Tab title="Teams">
    ### 依使用者計費

    團隊每位使用者每月支付 \$40，享有不限次數的審查。

    我們將「使用者」定義為當月有撰寫並由 Bugbot 審查之 PR 的作者。

    所有授權會在每個計費週期開始時釋出，並以先到先得的方式重新指派。若某位使用者在某月沒有提交任何由 Bugbot 審查的 PR，該席次可由其他使用者使用。

    ### 席次上限

    團隊管理員可以設定每月 Bugbot 席次上限以控管成本。

    ### 開始使用

    透過你的團隊控制台訂閱以啟用計費。

    ### 濫用防護

    為了防止濫用，我們對每個 Bugbot 授權設定每月 200 個 Pull Request 的共享上限。若你需要每月超過 200 個 Pull Request，請來信 [hi@cursor.com](mailto:hi@cursor.com)，我們很樂意協助。

    例如，如果你的團隊有 100 位使用者，你的組織起初每月可審查 20,000 個 Pull Request。若你自然達到該上限，請與我們聯繫，我們很樂意提高上限。
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## 疑難排解
</div>

如果 Bugbot 沒在工作：

1. 在留言中加入 `cursor review verbose=true` 或 `bugbot run verbose=true` 來**啟用詳細模式**，取得詳細日誌與 request ID
2. **檢查權限**，確認 Bugbot 具有存取該儲存庫的權限
3. **確認安裝**，確保 GitHub 應用程式已安裝並啟用

回報問題時，請附上詳細模式提供的 request ID。

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="Bugbot 是否符合隱私模式？">
    沒錯，Bugbot 遵循與 Cursor 相同的隱私合規標準，並以與其他 Cursor 請求相同的方式處理資料。
  </Accordion>

  <Accordion title="用完免費方案的額度會怎樣？">
    當你達到每月的免費方案額度上限時，Bugbot 的審查會暫停，直到你的下一個帳單週期。你可以升級到 14 天免費的 Pro 試用，享有不限次數的審查（受標準濫用防護規範限制）。
  </Accordion>
</AccordionGroup>

```
```



# 程式碼審查
Source: https://docs.cursor.com/zh-Hant/cli/cookbook/code-review

建立一個使用 Cursor CLI 的 GitHub Actions 工作流程，自動審查 pull request 並提供回饋

這份教學會帶你在 GitHub Actions 中用 Cursor CLI 設定程式碼審查。工作流程會分析 pull request、找出問題，並把回饋以留言方式貼上。

<Tip>
  對大多數使用者，我們建議改用 [Bugbot](/zh-Hant/bugbot)。Bugbot 提供免設定的託管式自動程式碼審查。這種 CLI 作法適合用來探索功能與進行進階自訂。
</Tip>

<div className="space-y-4">
  <Expandable title="完整的 workflow 檔案">
    ```yaml cursor-code-review.yml theme={null}
    name: 程式碼審查

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # 對草稿 PR 略過自動程式碼審查
        if: github.event.pull_request.draft == false
        steps:
          - name: 取出儲存庫
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: 安裝 Cursor CLI
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: 設定 git 身分
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: 執行自動化程式碼審查
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print '你正在 GitHub Actions runner 中執行自動化程式碼審查。gh CLI 已可用並透過 GH_TOKEN 驗證。你可以在 pull request 上留言。

              Context:
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Blocking Review: ${{ env.BLOCKING_REVIEW }}

              Objectives:
              1) 重新檢查既有審查留言，若已處理則回覆 resolved。
              2) 審查目前 PR 的 diff，只標記明確且高嚴重性的問題。
              3) 只在變更行留下非常精簡的行內留言（1-2 句），並在最後附上簡短總結。

              Procedure:
              - 取得既有留言：gh pr view --json comments
              - 取得 diff：gh pr diff
              - 取得含 patch 的變更檔以計算行內位置：gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - 為每個問題計算精準的行內錨點（檔案路徑 + diff 位置）。留言必須放在 diff 中已變更的那一行，而不是頂層留言。
              - 偵測先前由此機器人發出的頂層「無問題」類型留言（比對內文如："✅ no issues", "No issues found", "LGTM"）。
              - 若本次執行發現問題且存在任何先前的「無問題」留言：
                - 優先移除以避免混淆：
                  - 嘗試透過以下方式刪除頂層留言：gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - 若無法刪除，使用 GraphQL（minimizeComment）將其最小化，或編輯為在前綴加上「[Superseded by new findings]」。
                - 若無法刪除或最小化，回覆該留言：「⚠️ Superseded: issues were found in newer commits」。
              - 若先前回報的問題看起來已被附近的變更修正，回覆：✅ This issue appears to be resolved by the recent changes
              - 僅分析以下項目：
                - Null/undefined 反參照
                - 資源洩漏（未關閉的檔案或連線）
                - 注入（SQL/XSS）
                - 併發/競態條件
                - 關鍵操作缺少錯誤處理
                - 明顯導致不正確行為的邏輯錯誤
                - 具可衡量影響的明確效能反模式
                - 明確的安全性漏洞
              - 避免重複：若相近行已有類似意見則略過。

              Commenting rules:
              - 最多 10 則行內留言；優先處理最關鍵的問題
              - 每則留言僅描述一個問題；放在精準的變更行
              - 所有問題留言必須為行內（錨定到 PR diff 中的檔案與行/位置）
              - 語氣自然、具體且可執行；不要提及自動化或信心等級
              - 使用表情符號：🚨 Critical 🔒 Security ⚡ Performance ⚠️ Logic ✅ Resolved ✨ Improvement

              Submission:
              - 若沒有任何問題可回報，且已存在一則表示「無問題」的頂層留言（例如「✅ no issues」、「No issues found」、「LGTM」），不要再提交另一則留言。略過提交以避免重複。
              - 若沒有任何問題可回報，且先前沒有「無問題」留言，提交一則簡短摘要留言說明無問題。
              - 若有問題可回報，且先前存在「無問題」留言，請在提交新的審查前，先確保先前留言已刪除／最小化／標記為已被取代。
              - 若有問題可回報，提交一則審查，只包含行內留言，另可選擇附上一段精簡總結。使用 GitHub Reviews API 以確保留言為行內：
                - 建立一個留言的 JSON 陣列，例如：[{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - 透過以下方式提交：gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - 不要使用：gh pr review --approve 或 --request-changes

              Blocking behavior:
              - 若 BLOCKING_REVIEW 為 true，且張貼了任何 🚨 或 🔒 問題：echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - 否則：echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - 最後一律設定 CRITICAL_ISSUES_FOUND
              '

          - name: 檢查阻擋式審查結果
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "正在檢查關鍵問題..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ 發現關鍵問題且已啟用阻擋式審查。工作流程失敗。"
                exit 1
              else
                echo "✅ 未發現會阻擋的問題。"
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="自動化程式碼審查進行中，在 Pull Request 上顯示內嵌留言" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## 設定驗證
</div>

在 GitHub Actions 中[設定你的 API 金鑰與儲存庫機密](/zh-Hant/cli/github-actions#authentication)，用來讓 Cursor CLI 通過驗證。

<div id="set-up-agent-permissions">
  ## 設定代理權限
</div>

建立一個設定檔，控制代理能執行哪些動作。這能避免非預期的操作，例如推送程式碼或建立 pull request。

在你的儲存庫根目錄建立 `.cursor/cli.json`：

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

這個設定允許代理讀取檔案並使用 GitHub CLI 發佈評論，但會阻止它對你的儲存庫做出任何變更。請參考[權限說明](/zh-Hant/cli/reference/permissions)以取得更多設定選項。

<div id="build-the-github-actions-workflow">
  ## 建立 GitHub Actions 工作流程
</div>

現在我們一步步來建立這個工作流程。

<div id="set-up-the-workflow-trigger">
  ### 設定工作流程觸發器
</div>

建立 `.github/workflows/cursor-code-review.yml`，並設定在 pull request 時執行：

```yaml  theme={null}
name: Cursor 程式碼審閱

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### 取得存放庫
</div>

新增 checkout 步驟以存取 pull request 的程式碼：

```yaml  theme={null}
- name: 檢出存放庫
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### 安裝 Cursor CLI
</div>

加入 CLI 安裝步驟：

```yaml  theme={null}
- name: 安裝 Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### 設定 review 代理
</div>

在實作完整的 review 步驟之前，先來了解我們的 review 提示結構。本節說明我們希望代理的行為：

**目標**：
我們希望代理檢視目前的 PR diff，只標記明確且高嚴重性的問題，並且只在變更的行上留下非常短的行內留言（1–2 句），最後在結尾附上一段簡短總結。這能維持良好的訊噪比。

**格式**：
我們要精簡且到點的留言。會使用表情符號讓掃讀留言更容易，並在最後提供整體 review 的高階總結。

**提交**：
當 review 完成後，我們希望代理根據檢查結果附上一段短評。代理應提交一個包含行內留言與精煉總結的單一 review。

**邊界情況**：
我們需要處理：

* 既有留言已被解決：問題處理後，代理應將其標記為完成
* 避免重複：如果相似回饋已存在於相同或相鄰行，代理應略過留言

**最終提示**：
完整提示會結合以上所有行為要求，產出聚焦且可執行的回饋

現在來實作 review 代理步驟：

```yaml  theme={null}
- name: 執行程式碼審查
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "你正在 GitHub Actions runner 中執行自動化程式碼審查。gh CLI 可用，並已透過 GH_TOKEN 完成驗證。你可以對 pull request 發表評論。
    
    Context:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Objectives:
    1) 重新檢視既有的審查評論，若已處理則回覆已解決
    2) 審查當前 PR 的 diff，只標註明確且高嚴重性的問題
    3) 僅在變更的行上留下非常短的行內評論（1-2 句），並在最後附上一段精要摘要
    
    Procedure:
    - 取得現有評論：gh pr view --json comments
    - 取得 diff：gh pr diff
    - 如果先前回報的問題看起來已被鄰近變更修正，回覆：✅ 這個問題看起來已由最近的變更解決
    - 避免重複：若相似的回饋已存在於相同或相近的行，請略過
    
    Commenting rules:
    - 最多 10 則行內評論；優先處理最關鍵的問題
    - 每則評論只針對一個問題；放在確切變更的那一行
    - 語氣自然、具體且可行；不要提及自動化或高信心
    - 使用表情符號：🚨 關鍵 🔒 安全 ⚡ 效能 ⚠️ 邏輯 ✅ 已解決 ✨ 改進
    
    Submission:
    - 提交一份包含行內評論與精簡摘要的審查
    - 僅使用：gh pr review --comment
    - 不要使用：gh pr review --approve 或 --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## 測試你的審查員
</div>

建立一個測試 pull request，確認工作流程正常運作，並讓代理在審查評論中貼上表情符號回饋，並對特定行提供行內意見。

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull request showing automated review comments with emojis and inline feedback on specific lines" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## 下一步
</div>

你現在已經有一個可運作的自動化程式碼審查系統。可以考慮這些強化：

* 設定額外的工作流程來[修復 CI 失敗](/zh-Hant/cli/cookbook/fix-ci)
* 針對不同分支設定不同的審查等級
* 與你團隊現有的程式碼審查流程整合
* 依不同檔案類型或目錄自訂代理的行為

<Expandable title="進階：阻擋式審查">
  你可以將工作流程設定為在發現關鍵問題時判定失敗，防止 Pull Request 在處理前被合併。

  **將阻擋行為加入提示詞**

  先把審查代理的步驟更新為包含 `BLOCKING_REVIEW` 環境變數，並把以下阻擋行為加入提示詞：

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **加入阻擋檢查步驟**

  接著在程式碼審查步驟之後加入這個新步驟：

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>



# 修復 CI 失敗
Source: https://docs.cursor.com/zh-Hant/cli/cookbook/fix-ci

使用 Cursor CLI 搭配 GitHub Actions 修復儲存庫中的 CI 問題

在 GitHub Actions 中使用 Cursor CLI 修復 CI 失敗。這個 workflow 會分析失敗原因、進行精準修正，並建立修復分支，附上可快速建立 PR 的連結。

這個 workflow 會依名稱監控特定的 workflow。把 `workflows` 清單更新成實際的 CI workflow 名稱。

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Secret Audit
Source: https://docs.cursor.com/zh-Hant/cli/cookbook/secret-audit

使用 Cursor CLI 在 GitHub Actions 中稽核儲存庫的機密

使用 Cursor CLI 稽核你的儲存庫是否存在安全性弱點與機密外洩。此工作流程會掃描潛在機密、偵測高風險的工作流程模式，並提出安全性強化建議。

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# 翻譯鍵
Source: https://docs.cursor.com/zh-Hant/cli/cookbook/translate-keys

在 GitHub Actions 中使用 Cursor CLI 為儲存庫翻譯鍵

使用 Cursor CLI 管理國際化的翻譯鍵。這個 workflow 會在 pull request 中偵測新增或變更的 i18n 鍵，並補齊缺漏的翻譯，同時不會覆寫既有的內容。

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# 更新文件
Source: https://docs.cursor.com/zh-Hant/cli/cookbook/update-docs

使用 Cursor CLI 在 GitHub Actions 中為儲存庫更新文件

在 GitHub Actions 中使用 Cursor CLI 更新文件。有兩種做法：完全由代理自主執行，或採用確定性流程、僅允許代理修改檔案。

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: 更新文件

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: 取出版本庫
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: 安裝 Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: 設定 git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: 更新文件
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "你正在 GitHub Actions 執行器中運作。

            GitHub CLI 可透過 `gh` 使用，並已經由 `GH_TOKEN` 驗證。Git 可用。你對版本庫內容有寫入權限，也能在 PR 上留言，但不得建立或編輯 PR。

            # 背景：
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # 目標：
            - 依原始 PR 的增量變更，實作端到端的文件更新流程。

            # 要求：
            1) 判斷原始 PR 的變更內容；若有多次推送，需自上次成功更新文件以來計算增量差異。
            2) 僅依那些增量變更更新相關文件。
            3) 使用背景中的文件分支前綴，為此 PR 的 head 維護常駐的文件分支；若不存在則建立，否則更新，並將變更推送至 origin。
            4) 你沒有建立 PR 的權限。改為張貼或更新一則自然語言的 PR 留言（1–2 句），簡要說明文件更新，並包含可快速建立 PR 的行內比較連結

            # 輸入與慣例：
            - 使用 `gh pr diff` 與 git 歷史來偵測變更，並自上次文件更新以來推導增量範圍。
            - 不要嘗試直接建立或編輯 PR。請使用上述比較連結格式。
            - 保持變更精簡且符合版本庫風格。若不需更新文件，就不要做任何變更，也不要張貼留言。

            # 有更新時的交付內容：
            - 將提交推送到此 PR head 的常駐文件分支。
            - 在原始 PR 上發佈一則自然語言留言，包含上述的行內比較連結。避免重複張貼；若先前已有機器人留言則予以更新。
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: 更新文件

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: 取出程式庫
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: 安裝 Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: 設定 git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: 產生文件更新（不提交/不推送/不留言）
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "你正在 GitHub Actions 執行器中運作。

            GitHub CLI 可透過 \`gh\` 使用，並已用 \`GH_TOKEN\` 驗證。Git 已可使用。

            重要：不要建立分支、提交、推送，或在 PR 留言。只在需要時修改工作目錄中的檔案。稍後的工作流程步驟會負責發布變更並在 PR 留言。

            # 情境：
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # 目標：
            - 根據此 PR 帶來的增量變更更新程式庫文件。

            # 要求：
            1) 判斷原始 PR 中變更了什麼（視需要使用 \`gh pr diff\` 與 git 歷史）。如果已存在持久性的文件分支 \`${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}\`，可以把它當成唯讀參考點來了解先前的更新。
            2) 只根據那些變更更新相關文件。保持編輯最小化，並符合程式庫的風格。
            3) 不要提交、推送、建立分支，或在 PR 留言。只留下工作樹中的已更新檔案；稍後的步驟會發布。

            # 輸入與慣例：
            - 使用 \`gh pr diff\` 與 git 歷史偵測變更，並據此聚焦文件編輯。
            - 若不需要文件更新，就不要做任何變更，也不要產生輸出。

            # 有更新時的交付物：
            - 只在工作目錄中的已修改文件（無提交/推送/留言）。
            " --force --model "$MODEL" --output-format=text

        - name: 發佈文件分支
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # 確保我們位於可推送的本地分支上
            git fetch origin --prune

            # 建立/切換到持久性的文件分支，並保留目前工作樹的變更
            git checkout -B "$DOCS_BRANCH"

            # 暫存並偵測變更
            git add -A
            if git diff --staged --quiet; then
              echo "沒有可發佈的文件變更。略過提交/推送。"
              exit 0
            fi

            COMMIT_MSG="docs: 更新對應 PR #${PR_NUMBER}（${HEAD_REF} @ $(git rev-parse --short HEAD)）"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: 張貼或更新 PR 留言
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor 已更新文件分支：\`${DOCS_BRANCH}\`"
              echo "現在可以[檢視差異並快速建立 PR 以合併這些文件更新](${COMPARE_URL})。"
              echo
              echo "_此留言會在後續執行時，隨 PR 變更而更新。_"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # 若編輯最後一則機器人留言失敗（較舊的 gh），則改為建立新留言
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "已更新現有的 PR 留言。"
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "已張貼新的 PR 留言。"
            fi
  ```
</CodeGroup>



# GitHub Actions
Source: https://docs.cursor.com/zh-Hant/cli/github-actions

了解如何在 GitHub Actions 與其他持續整合系統中使用 Cursor CLI

在 GitHub Actions 與其他 CI/CD 系統中使用 Cursor CLI，自動化各種開發任務。

<div id="github-actions-integration">
  ## GitHub Actions 整合
</div>

基本設定：

```yaml  theme={null}
- name: 安裝 Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: 執行 Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "在這裡輸入你的指令" --model gpt-5
```

<div id="cookbook-examples">
  ## Cookbook 範例
</div>

看看我們的 cookbook 範例，了解實用的工作流程：[更新文件](/zh-Hant/cli/cookbook/update-docs) 和 [修正 CI 問題](/zh-Hant/cli/cookbook/fix-ci)。

<div id="other-ci-systems">
  ## 其他 CI 系統
</div>

只要符合以下條件，就能在任何 CI/CD 系統中使用 Cursor CLI：

* 可執行 **Shell 腳本**（bash、zsh 等）
* 透過 **環境變數** 設定 API key
* 具備 **網際網路連線** 可連到 Cursor 的 API

<div id="autonomy-levels">
  ## 自主性等級
</div>

選擇 agent 的自主性等級：

<div id="full-autonomy-approach">
  ### 完全自主方案
</div>

讓 agent 對 git 操作、API 呼叫與外部互動擁有完整控制。設定更簡單，但需要更高信任。

**範例：** 在我們的 [Update Documentation](/zh-Hant/cli/cookbook/update-docs) 實作範本中，第一個工作流程讓 agent 可以：

* 分析 PR 變更
* 建立與管理 git 分支
* 建立提交並推送變更
* 在 Pull Request 中發佈留言
* 處理所有錯誤情況

```yaml  theme={null}
- name: 更新文件（完全自主）
  run: |
    cursor-agent -p "你對 git、GitHub CLI 與 PR 操作擁有完整存取權限。 
    全程處理整個文件更新流程，包括 commit、push 與 PR 評論。"
```

<div id="restricted-autonomy-approach">
  ### 受限自主方法
</div>

<Note>
  我們建議在生產環境的 CI 工作流程中，搭配**基於權限的限制**使用這種方法。這能同時滿足兩種需求：代理能智慧處理複雜的分析與檔案變更，而關鍵操作仍維持可預測且可稽核。
</Note>

將關鍵步驟拆分到獨立的工作流程步驟，並限制代理的操作。帶來更好的可控性與可預測性。

**範例：** 同一份範例手冊中的第二個工作流程，將代理限制為只能進行檔案變更：

```yaml  theme={null}
- name: 產生文件更新（受限）
  run: |
    cursor-agent -p "重要：不要建立分支、提交、推送，或發佈 PR 留言。
    只修改工作目錄中的檔案。後續的工作流程步驟會處理發布。"

- name: 發佈文件分支（具決定性）
  run: |
    # 由 CI 處理的具決定性的 git 作業
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: 更新此 PR"
    git push origin "docs/${{ github.head_ref }}"

- name: 發佈 PR 留言（具決定性）  
  run: |
    # 由 CI 處理的具決定性的 PR 留言
    gh pr comment ${{ github.event.pull_request.number }} --body "文件已更新"
```

<div id="permission-based-restrictions">
  ### 以權限為基礎的限制
</div>

使用[權限設定](/zh-Hant/cli/reference/permissions)在 CLI 層級強制套用限制：

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## 驗證
</div>

<div id="generate-your-api-key">
  ### 產生你的 API 金鑰
</div>

先在 Cursor 控制台[產生一組 API 金鑰](/zh-Hant/cli/reference/authentication#api-key-authentication)。

<div id="configure-repository-secrets">
  ### 設定儲存庫機密
</div>

把你的 Cursor API 金鑰安全地存放在儲存庫中：

1. 前往你的 GitHub 儲存庫
2. 點選 **Settings** → **Secrets and variables** → **Actions**
3. 點選 **New repository secret**
4. 將名稱設為 `CURSOR_API_KEY`
5. 貼上你的 API 金鑰作為值
6. 點選 **Add secret**

<div id="use-in-workflows">
  ### 在工作流程中使用
</div>

設定你的 `CURSOR_API_KEY` 環境變數：

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```



# 使用 Headless CLI
Source: https://docs.cursor.com/zh-Hant/cli/headless

了解如何用 Cursor CLI 撰寫腳本，自動化進行程式碼分析、 產生與修改

在腳本與自動化工作流程中使用 Cursor CLI，處理程式碼分析、產生與重構等任務。

<div id="how-it-works">
  ## 運作方式
</div>

在非互動式腳本與自動化情境中使用 [print 模式](/zh-Hant/cli/using#non-interactive-mode)（`-p, --print`）。

<div id="file-modification-in-scripts">
  ### 在腳本中修改檔案
</div>

將 `--print` 搭配 `--force` 一起使用，以在腳本中修改檔案：

```bash  theme={null}

# 在列印模式下允許修改檔案
cursor-agent -p --force "Refactor this code to use modern ES6+ syntax"


# 若未加上 --force，變更只會被建議，不會套用

# 不會修改檔案


# 批次處理並實際變更檔案
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "為 $file 新增完整的 JSDoc 註解"
done
```

<Warning>
  `--force` 旗標允許 agent 在無需確認的情況下直接修改檔案
</Warning>

<div id="setup">
  ## 設定
</div>

完整的設定說明請參考 [Installation](/zh-Hant/cli/installation) 和 [Authentication](/zh-Hant/cli/reference/authentication)。

```bash  theme={null}

# 安裝 Cursor CLI
curl https://cursor.com/install -fsS | bash


# 為腳本設定 API 金鑰  
export CURSOR_API_KEY=your_api_key_here
cursor-agent -p "分析這段程式碼"
```

<div id="example-scripts">
  ## 範例腳本
</div>

依不同腳本需求使用不同的輸出格式。詳情請參閱[輸出格式](/zh-Hant/cli/reference/output-format)。

<div id="searching-the-codebase">
  ### 搜尋程式碼庫
</div>

使用 `--output-format text` 取得易讀的回應：

```bash  theme={null}
#!/bin/bash

# 簡單的程式庫問題

cursor-agent -p --output-format text "這個程式庫是做什麼的？"
```

<div id="automated-code-review">
  ### 自動化程式碼審查
</div>

使用 `--output-format json` 取得結構化分析：

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - 基礎程式碼審查腳本

echo "開始進行程式碼審查..."


# 審查最近的變更
cursor-agent -p --force --output-format text \
  "請審查近期的程式碼變更並提供回饋，內容包含：
  - 程式碼品質與可讀性  
  - 潛在的錯誤或問題
  - 安全性考量
  - 是否遵循最佳實務

  請提供具體的改進建議，並寫入 review.txt"

if [ $? -eq 0 ]; then
  echo "✅ 程式碼審查已順利完成"
else
  echo "❌ 程式碼審查失敗"
  exit 1
fi
```

<div id="real-time-progress-tracking">
  ### 即時進度追蹤
</div>

使用 `--output-format stream-json` 來即時追蹤進度：

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - 即時追蹤進度

echo "🚀 開始處理串流..."


# 即時追蹤進度
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "分析這個專案的結構，並在 analysis.txt 中建立摘要報告" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Using model: $model"
        fi
        ;;
        
      "assistant")
        # 累積串流文字增量
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # 顯示即時進度
        printf "\r📝 產生中：%d 個字元" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # 擷取工具資訊
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 工具 #$tool_count：建立 $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 工具 #$tool_count：讀取 $path"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # 擷取並顯示工具結果
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ 已建立 $lines 行（$size 位元組）"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ 已讀取 $lines 行"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 已完成，耗時 ${duration}ms（總計 ${total_time}s）"
        echo "📊 最終統計：$tool_count 個工具，已產生 ${#accumulated_text} 個字元"
        ;;
    esac
  done
```



# 安裝
Source: https://docs.cursor.com/zh-Hant/cli/installation

安裝與更新 Cursor CLI

<div id="installation">
  ## 安裝
</div>

<div id="macos-linux-and-windows-wsl">
  ### macOS、Linux 和 Windows（WSL）
</div>

用一條指令就能安裝 Cursor CLI：

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

<div id="verification">
  ### 驗證
</div>

安裝完成後，先確認 Cursor CLI 是否正常運作：

```bash  theme={null}
cursor-agent --version
```

<div id="post-installation-setup">
  ## 安裝後設定
</div>

1. **把 \~/.local/bin 加進 PATH：**

   對 bash：

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   對 zsh：

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **開始使用 Cursor Agent：**
   ```bash  theme={null}
   cursor-agent
   ```

<div id="updates">
  ## 更新
</div>

Cursor CLI 預設會自動嘗試更新，確保你隨時使用最新版本。

若要手動將 Cursor CLI 更新到最新版本：

```bash  theme={null}
cursor-agent update

# 或
cursor-agent upgrade
```

這兩個指令都會將 Cursor Agent 更新到最新版本。



# MCP
Source: https://docs.cursor.com/zh-Hant/cli/mcp

使用 MCP 伺服器透過 cursor-agent 串接外部工具與資料來源

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

<div id="overview">
  ## 概述
</div>

Cursor CLI 支援 [Model Context Protocol (MCP)](/zh-Hant/context/mcp) 伺服器，讓你把外部工具與資料來源接到 `cursor-agent`。**CLI 的 MCP 使用與編輯器相同的設定**——你設定過的任何 MCP 伺服器都能在兩者之間無縫運作。

<Card title="認識 MCP" icon="link" href="/zh-Hant/context/mcp">
  第一次接觸 MCP？來看完整的設定、身分驗證與可用伺服器指南
</Card>

<div id="cli-commands">
  ## CLI 指令
</div>

使用 `cursor-agent mcp` 指令管理 MCP 伺服器：

<div id="list-configured-servers">
  ### 列出已設定的伺服器
</div>

查看所有已設定的 MCP 伺服器及其目前狀態：

```bash  theme={null}
cursor-agent mcp list
```

這會顯示：

* 伺服器名稱與識別碼
* 連線狀態（已連線／未連線）
* 設定來源（專案或全域）
* 傳輸方式（stdio、HTTP、SSE）

<div id="list-available-tools">
  ### 列出可用工具
</div>

檢視特定 MCP 伺服器所提供的工具：

```bash  theme={null}
cursor-agent mcp list-tools <識別符>
```

這會顯示：

* 工具名稱與描述
* 必要與選用參數
* 參數型別與限制條件

<div id="login-to-mcp-server">
  ### 登入 MCP 伺服器
</div>

使用在 `mcp.json` 中設定的 MCP 伺服器進行驗證：

```bash  theme={null}
cursor-agent mcp login <identifier>
```

<div id="disable-mcp-server">
  ### 停用 MCP 伺服器
</div>

從本機的已核准清單中移除 MCP 伺服器：

```bash  theme={null}
cursor-agent mcp disable <識別符>
```

<div id="using-mcp-with-agent">
  ## 搭配 Agent 使用 MCP
</div>

當你設定好 MCP 伺服器（請參閱 [MCP 主指南](/zh-Hant/context/mcp) 完成設定）後，`cursor-agent` 會在你的需求相關時，自動發現並使用可用的工具。

```bash  theme={null}

# 檢查有哪些可用的 MCP 伺服器
cursor-agent mcp list


# 查看特定伺服器提供哪些工具
cursor-agent mcp list-tools playwright


# 使用 cursor-agent —— 需要時會自動使用 MCP 工具
cursor-agent --prompt "導航到 google.com，並擷取搜尋頁面的螢幕畫面"
```

CLI 會遵循與編輯器相同的設定優先順序（專案 → 全域 → 巢狀），並會自動從上層目錄偵測設定。

<div id="related">
  ## 相關
</div>

<CardGroup cols={2}>
  <Card title="MCP Overview" icon="link" href="/zh-Hant/context/mcp">
    完整 MCP 指南：安裝、設定與驗證
  </Card>

  <Card title="Available MCP Tools" icon="table" href="/zh-Hant/tools">
    瀏覽可用的預先建置 MCP 伺服器
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/zh-Hant/cli/overview

開始使用 Cursor CLI 在終端機中撰寫程式碼

Cursor CLI 讓你能直接在終端機與 AI 代理互動，用於撰寫、審閱與修改程式碼。無論你偏好互動式終端介面，或在腳本與 CI 流水線中進行輸出式自動化，CLI 都能在你工作的地方提供強大的程式碼輔助功能。

```bash  theme={null}

# 安裝
curl https://cursor.com/install -fsS | bash


# 啟動互動式工作階段
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI 目前處於測試階段，我們很想聽聽你的回饋！
</Info>

<div id="interactive-mode">
  ### 互動模式
</div>

啟動與代理的對話式工作階段，描述你的目標、檢視建議變更，並核准指令：

```bash  theme={null}

# 開始互動式工作階段
cursor-agent


# 以初始提示開始
cursor-agent "將 auth 模組重構為改用 JWT 權杖"
```

<div id="non-interactive-mode">
  ### 非互動模式
</div>

在腳本、CI 管線或自動化等非互動情境中使用印出模式：

```bash  theme={null}

# 以特定提示與模型執行
cursor-agent -p "find and fix performance issues" --model "gpt-5"


# 含納入 git 變更的內容一起審查
cursor-agent -p "review these changes for security issues" --output-format text
```

<div id="sessions">
  ### Sessions
</div>

延續先前的對話，在多次互動間保留脈絡：

```bash  theme={null}

# 列出所有先前的對話
cursor-agent ls


# 繼續最新的對話  
cursor-agent resume


# 繼續特定對話
cursor-agent --resume="chat-id-here"
```



# 驗證
Source: https://docs.cursor.com/zh-Hant/cli/reference/authentication

透過瀏覽器登入流程或 API 金鑰驗證 Cursor CLI

Cursor CLI 支援兩種驗證方式：瀏覽器登入（推薦）或 API 金鑰。

<div id="browser-authentication-recommended">
  ## 瀏覽器驗證（建議）
</div>

使用瀏覽器流程，就能獲得最簡便的驗證體驗：

```bash  theme={null}

# 透過瀏覽器流程登入
cursor-agent login


# 檢查認證狀態
cursor-agent status


# 登出並清除已儲存的認證
cursor-agent logout
```

login 指令會開啟你的預設瀏覽器，並要求你使用 Cursor 帳號進行驗證。完成後，你的認證資訊會安全地儲存在本機。

<div id="api-key-authentication">
  ## API 金鑰驗證
</div>

在自動化、腳本，或 CI/CD 環境中，使用 API 金鑰驗證：

<div id="step-1-generate-an-api-key">
  ### Step 1: 產生 API 金鑰
</div>

到 Cursor 控制台的 Integrations > User API Keys 產生一組 API 金鑰。

<div id="step-2-set-the-api-key">
  ### Step 2: 設定 API 金鑰
</div>

可以用兩種方式提供 API 金鑰：

**選項 1：環境變數（建議）**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "實作使用者身分驗證"
```

**選項 2：命令列參數**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "實作使用者身分驗證"
```

<div id="authentication-status">
  ## 驗證狀態
</div>

查看你目前的驗證狀態：

```bash  theme={null}
cursor-agent status
```

這個指令會顯示：

* 你是否已通過驗證
* 你的帳號資訊
* 目前的端點設定

<div id="troubleshooting">
  ## 疑難排解
</div>

* **「Not authenticated」錯誤：** 執行 `cursor-agent login`，或確認你的 API 金鑰已正確設定
* **SSL 憑證錯誤：** 在開發環境使用 `--insecure` 參數
* **端點問題：** 使用 `--endpoint` 參數來指定自訂 API 端點



# 設定
Source: https://docs.cursor.com/zh-Hant/cli/reference/configuration

適用於 cli-config.json 的 Agent CLI 設定參考

使用 `cli-config.json` 檔案設定 Agent CLI。

<div id="file-location">
  ## 檔案位置
</div>

<div class="full-width-table">
  | 類型 | 平台          | 路徑                                         |
  | :- | :---------- | :----------------------------------------- |
  | 全域 | macOS/Linux | `~/.cursor/cli-config.json`                |
  | 全域 | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | 專案 | 全部          | `<project>/.cursor/cli.json`               |
</div>

<Note>只有權限可以在專案層級調整。其他所有 CLI 設定都必須在全域層級設定。</Note>

可用環境變數覆寫：

* **`CURSOR_CONFIG_DIR`**：自訂目錄路徑
* **`XDG_CONFIG_HOME`**（Linux/BSD）：使用 `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## 結構定義
</div>

<div id="required-fields">
  ### 必填欄位
</div>

<div class="full-width-table">
  | 欄位                  | 型別        | 說明                                                          |
  | :------------------ | :-------- | :---------------------------------------------------------- |
  | `version`           | number    | 設定結構定義版本（目前：`1`）                                            |
  | `editor.vimMode`    | boolean   | 啟用 Vim 鍵盤快捷鍵（預設：`false`）                                    |
  | `permissions.allow` | string\[] | 允許的操作（詳見 [Permissions](/zh-Hant/cli/reference/permissions)） |
  | `permissions.deny`  | string\[] | 禁止的操作（詳見 [Permissions](/zh-Hant/cli/reference/permissions)） |
</div>

<div id="optional-fields">
  ### 選用欄位
</div>

<div class="full-width-table">
  | 欄位                       | 型別      | 說明                |
  | :----------------------- | :------ | :---------------- |
  | `model`                  | object  | 已選定的模型設定          |
  | `hasChangedDefaultModel` | boolean | 由 CLI 管理的預設模型覆寫旗標 |
</div>

<div id="examples">
  ## 範例
</div>

<div id="minimal-config">
  ### 最小化設定
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### 開啟 Vim 模式
</div>

```json  theme={null}
{
  "version": 版本 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### 設定權限
</div>

```json  theme={null}
{
  "version": 版本: 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

參考 [Permissions](/zh-Hant/cli/reference/permissions) 以了解可用的權限類型與範例。

<div id="troubleshooting">
  ## 疑難排解
</div>

**設定錯誤**：先把該檔案移開，然後重新啟動：

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**變更無法保存**：確保 JSON 有效且具備寫入權限。有些欄位由 CLI 管理，可能會被覆寫。

<div id="notes">
  ## 注意事項
</div>

* 純 JSON 格式（不含註解）
* CLI 會自動修復缺失的欄位
* 損毀的檔案會先備份為 `.bad`，再重新建立
* 權限條目必須為精確字串（詳見 [Permissions](/zh-Hant/cli/reference/permissions)）



# 輸出格式
Source: https://docs.cursor.com/zh-Hant/cli/reference/output-format

文字、JSON 與 stream-JSON 格式的輸出結構

Cursor Agent CLI 在搭配 `--print` 使用時，可透過 `--output-format` 選項提供多種輸出格式。這些格式包含供程式化使用的結構化格式（`json`、`stream-json`），以及便於人類閱讀以追蹤進度的精簡文字格式。

<Note>
  預設的 `--output-format` 為 `stream-json`。此選項僅在列印（`--print`）時，或在推斷為列印模式（非 TTY 的 stdout 或透過管線的 stdin）時有效。
</Note>

<div id="json-format">
  ## JSON 格式
</div>

當執行成功完成時，`json` 輸出格式會輸出單一 JSON 物件（後接換行）。不會輸出增量與工具事件；文字會彙整至最終結果。

若失敗，程序會以非零代碼結束，並將錯誤訊息寫到 stderr。失敗時不會輸出任何格式正確的 JSON 物件。

<div id="success-response">
  ### 成功回應
</div>

成功時，CLI 會輸出具有以下結構的 JSON 物件：

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<完整助理內容>",
  "session_id": "<uuid>",
  "request_id": "<選填的請求 ID>"
}
```

<div class="full-width-table">
  | 欄位                | 說明                                |
  | ----------------- | --------------------------------- |
  | `type`            | 終端輸出一律為 `"result"`                |
  | `subtype`         | 成功完成時一律為 `"success"`              |
  | `is_error`        | 成功回應一律為 `false`                   |
  | `duration_ms`     | 總執行時間（毫秒）                         |
  | `duration_api_ms` | API 請求時間（毫秒）（目前等同於 `duration_ms`） |
  | `result`          | 完整的助手回應文字（所有文字增量的串接）              |
  | `session_id`      | 唯一的工作階段識別碼                        |
  | `request_id`      | 選填的請求識別碼（可能省略）                    |
</div>

<div id="stream-json-format">
  ## Stream JSON 格式
</div>

`stream-json` 輸出格式會產生以換行分隔的 JSON（NDJSON）。每一行包含一個 JSON 物件，代表執行期間的即時事件。

成功時，串流會以終止的 `result` 事件結束。若失敗，程序會以非零代碼結束，且串流可能在沒有終止事件的情況下提前結束；錯誤訊息會寫入 stderr。

<div id="event-types">
  ### 事件類型
</div>

<div id="system-initialization">
  #### 系統初始化
</div>

在每個工作階段開始時觸發一次：

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "環境變數|旗標|登入",
  "cwd": "/絕對/路徑",
  "session_id": "<uuid>",
  "model": "<模型顯示名稱>",
  "permissionMode": "預設"
}
```

<Note>
  未來可能會在此事件中新增 `tools` 和 `mcp_servers` 等欄位。
</Note>

<div id="user-message">
  #### 使用者訊息
</div>

包含使用者的輸入提示詞：

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### 助理文字差異
</div>

在助理生成回應的過程中會多次觸發。這些事件包含逐步累積的文字片段：

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<增量分塊>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  依序串接所有 `message.content[].text` 的值，重建完整的助手回應。
</Note>

<div id="tool-call-events">
  #### 工具呼叫事件
</div>

工具呼叫會透過開始與完成事件進行追蹤：

**工具呼叫開始：**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**工具調用完成：**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "檔案內容…",
          "isEmpty": false,
          "exceededLimit": false
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### 工具呼叫類型
</div>

**讀取檔案工具：**

* **已開始**：`tool_call.readToolCall.args` 包含 `{ "path": "file.txt" }`
* **已完成**：`tool_call.readToolCall.result.success` 包含檔案中繼資料與內容

**寫入檔案工具：**

* **已開始**：`tool_call.writeToolCall.args` 包含 `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **已完成**：`tool_call.writeToolCall.result.success` 包含 `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**其他工具：**

* 可能使用 `tool_call.function` 結構，包含 `{ "name": "tool_name", "arguments": "..." }`

<div id="terminal-result">
  #### 終端機結果
</div>

成功完成時所發出的最後一個事件：

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<完整助理內容>",
  "session_id": "<uuid>",
  "request_id": "<選填的 request id>"
}
```

<div id="example-sequence">
  ### 範例序列
</div>

這是一段具有代表性的 NDJSON 序列，用來示範事件的典型流程：

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"讀取 README.md 並建立摘要"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"我會 "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"讀取 README.md 檔案"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# 專案\n\n這是一個範例專案...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" 並產生摘要"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README 摘要\n\n這個專案包含...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README 摘要\n\n這個專案包含...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"我會讀取 README.md 檔案並產生摘要","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## 文字格式
</div>

`text` 輸出格式會以簡化、易讀的方式串流顯示代理的動作。它不是輸出詳細的 JSON 事件，而是以精煉的文字即時描述代理正在做什麼。

這種格式能在不必負擔解析結構化資料的情況下監控代理進度，非常適合拿來記錄、偵錯或做簡單的進度追蹤。

<div id="example-output">
  ### 範例輸出
</div>

```
讀取檔案
已編輯檔案
執行終端機命令
建立新檔案
```

每個動作在代理執行時都會另起一行顯示，讓你即時掌握代理完成任務的進度。

<div id="implementation-notes">
  ## 實作注意事項
</div>

* 每個事件以單行輸出，並以 `\n` 結尾
* 在列印模式中會抑制 `thinking` 事件，且不會出現在任何輸出格式中
* 欄位可能會隨時間以向後相容的方式新增（使用方應忽略未知欄位）
* 串流格式提供即時更新；JSON 格式會在完成後才輸出結果
* 將所有 `assistant` 訊息差量串接以重建完整回應
* 可使用工具呼叫 ID 將開始／完成事件對應起來
* Session ID 在單次代理執行期間保持一致



# 參數
Source: https://docs.cursor.com/zh-Hant/cli/reference/parameters

Cursor Agent CLI 的完整命令參考

<div id="global-options">
  ## 全域選項
</div>

全域選項可搭配任何指令使用：

<div class="full-width-table">
  | Option                     | Description                                                            |
  | -------------------------- | ---------------------------------------------------------------------- |
  | `-v, --version`            | 輸出版本號                                                                  |
  | `-a, --api-key <key>`      | 用於驗證的 API 金鑰（也可使用 `CURSOR_API_KEY` 環境變數）                               |
  | `-p, --print`              | 將回應列印到主控台（適用於腳本或非互動式使用）。可使用所有工具，包括 write 與 bash。                       |
  | `--output-format <format>` | 輸出格式（僅在 `--print` 時有效）：`text`、`json`，或 `stream-json`（預設：`stream-json`） |
  | `-b, --background`         | 以背景模式啟動（啟動時開啟 composer 挑選器）                                            |
  | `--fullscreen`             | 啟用全螢幕模式                                                                |
  | `--resume [chatId]`        | 繼續先前的對話工作階段                                                            |
  | `-m, --model <model>`      | 要使用的模型                                                                 |
  | `-f, --force`              | 強制允許指令，除非明確拒絕                                                          |
  | `-h, --help`               | 顯示指令說明                                                                 |
</div>

<div id="commands">
  ## 指令
</div>

<div class="full-width-table">
  | 指令                | 說明                     | 用法                                             |
  | ----------------- | ---------------------- | ---------------------------------------------- |
  | `login`           | 使用 Cursor 進行身分驗證       | `cursor-agent login`                           |
  | `logout`          | 登出並清除已儲存的驗證資訊          | `cursor-agent logout`                          |
  | `status`          | 檢查驗證狀態                 | `cursor-agent status`                          |
  | `mcp`             | 管理 MCP 伺服器             | `cursor-agent mcp`                             |
  | `update\|upgrade` | 將 Cursor Agent 更新到最新版本 | `cursor-agent update` 或 `cursor-agent upgrade` |
  | `ls`              | 列出聊天工作階段               | `cursor-agent ls`                              |
  | `resume`          | 繼續最近的聊天工作階段            | `cursor-agent resume`                          |
  | `help [command]`  | 顯示該指令的說明               | `cursor-agent help [command]`                  |
</div>

<Note>
  如果沒有指定指令，Cursor Agent 會預設進入互動式聊天模式。
</Note>

<div id="mcp">
  ## MCP
</div>

管理為 Cursor Agent 設定的 MCP 伺服器。

<div class="full-width-table">
  | Subcommand                | Description                           | Usage                                      |
  | ------------------------- | ------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | 向 `.cursor/mcp.json` 中設定的 MCP 伺服器進行驗證 | `cursor-agent mcp login <identifier>`      |
  | `list`                    | 列出已設定的 MCP 伺服器及其狀態                    | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | 列出指定 MCP 可用的工具及其引數名稱                  | `cursor-agent mcp list-tools <identifier>` |
</div>

所有 MCP 指令都支援 `-h, --help` 查看該指令的說明。

<div id="arguments">
  ## 參數
</div>

在以聊天模式啟動時（預設行為），可以提供初始提示：

**參數：**

* `prompt` — 代理的初始提示

<div id="getting-help">
  ## 取得說明
</div>

所有指令都支援全域 `-h, --help` 選項，可顯示該指令的詳細說明。



# 權限
Source: https://docs.cursor.com/zh-Hant/cli/reference/permissions

控制代理對檔案與指令存取的權限類型

在 CLI 設定中用 permission tokens 設定代理可以做的事。權限可在 `~/.cursor/cli-config.json`（全域）或 `<project>/.cursor/cli.json`（專案）中設定。

<div id="permission-types">
  ## 權限類型
</div>

<div id="shell-commands">
  ### Shell 指令
</div>

**格式：** `Shell(commandBase)`

控制對 Shell 指令的存取。`commandBase` 是指令列中的第一個標記（token）。

<div class="full-width-table">
  | 範例           | 說明                       |
  | ------------ | ------------------------ |
  | `Shell(ls)`  | 允許執行 `ls` 指令             |
  | `Shell(git)` | 允許任何 `git` 子指令           |
  | `Shell(npm)` | 允許執行 npm 套件管理工具的指令       |
  | `Shell(rm)`  | 拒絕具有破壞性的檔案刪除（常見於 `deny`） |
</div>

<div id="file-reads">
  ### 檔案讀取
</div>

**格式：** `Read(pathOrGlob)`

控制對檔案與目錄的讀取存取。支援 glob 模式。

<div class="full-width-table">
  | 範例                  | 說明                          |
  | ------------------- | --------------------------- |
  | `Read(src/**/*.ts)` | 允許讀取 `src` 中的 TypeScript 檔案 |
  | `Read(**/*.md)`     | 允許在任何位置讀取 Markdown 檔案       |
  | `Read(.env*)`       | 拒絕讀取環境設定檔                   |
  | `Read(/etc/passwd)` | 拒絕讀取系統檔案                    |
</div>

<div id="file-writes">
  ### 檔案寫入
</div>

**格式：** `Write(pathOrGlob)`

控制對檔案與目錄的寫入存取。支援 glob 模式。在列印模式下使用時，寫入檔案需要 `--force`。

<div class="full-width-table">
  | 範例                    | 說明                 |
  | --------------------- | ------------------ |
  | `Write(src/**)`       | 允許寫入 `src` 底下的任何檔案 |
  | `Write(package.json)` | 允許修改 package.json  |
  | `Write(**/*.key)`     | 拒絕寫入私鑰檔案           |
  | `Write(**/.env*)`     | 拒絕寫入環境設定檔          |
</div>

<div id="configuration">
  ## 設定
</div>

在 CLI 設定檔的 `permissions` 物件中加入權限：

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## 模式比對
</div>

* Glob 模式使用 `**`、`*` 和 `?` 萬用字元
* 相對路徑以目前工作區為範圍
* 絕對路徑可指向專案以外的檔案
* 拒絕規則優先於允許規則



# 斜線指令
Source: https://docs.cursor.com/zh-Hant/cli/reference/slash-commands

Cursor CLI 會話中的快速操作

<div class="full-width-table">
  | Command               | Description                      |
  | --------------------- | -------------------------------- |
  | `/model <model>`      | 設定或列出模型                          |
  | `/auto-run [state]`   | 切換自動執行（預設）或設定 \[on\|off\|status] |
  | `/new-chat`           | 開啟新的聊天會話                         |
  | `/vim`                | 切換 Vim 鍵位                        |
  | `/help [command]`     | 顯示說明（/help \[cmd]）               |
  | `/feedback <message>` | 分享回饋給團隊                          |
  | `/resume <chat>`      | 依資料夾名稱繼續先前的聊天                    |
  | `/copy-req-id`        | 複製上一個請求 ID                       |
  | `/logout`             | 登出 Cursor                        |
  | `/quit`               | 退出                               |
</div>



# Shell 模式
Source: https://docs.cursor.com/zh-Hant/cli/shell-mode

直接在 CLI 中執行 shell 指令，不用離開對話

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

Shell Mode 可直接在 CLI 中執行 shell 指令，無須離開你的對話。用它來執行快速、非互動式的指令，具備安全檢查，且輸出會顯示在對話中。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## 指令執行
</div>

指令會在登入的 shell（`$SHELL`）中執行，並使用 CLI 的工作目錄與環境。把指令串接起來就能在其他目錄執行：

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## 輸出
</div>

<product_visual type="screenshot">
  指令輸出會顯示含結束代碼的標頭、stdout/stderr、以及截斷控制
</product_visual>

大量輸出會自動截斷，長時間執行的程序會逾時以維持效能。

<div id="limitations">
  ## 限制
</div>

* 指令在 30 秒後會逾時
* 不支援長時間執行的程序、伺服器，或互動式提示
* 建議使用簡短、非互動式的指令以獲得最佳效果

<div id="permissions">
  ## 權限
</div>

在執行前，系統會根據你的權限與團隊設定檢查指令。詳見 [Permissions](/zh-Hant/cli/reference/permissions) 了解完整設定方式。

<product_visual type="screenshot">
  決策橫幅顯示核准選項：Run、Reject/Propose、Add to allowlist、Auto-run
</product_visual>

管理員政策可能會封鎖某些指令，且帶有重新導向的指令無法直接加入允許清單。

<div id="usage-guidelines">
  ## 使用指南
</div>

Shell 模式很適合做狀態檢查、快速建置、檔案操作，以及檢視環境。

避免執行長時間運作的伺服器、互動式應用程式，或需要輸入的指令。

每個指令都會獨立執行—若要在其他目錄執行，請使用 `cd <dir> && ...`。

<div id="troubleshooting">
  ## 疑難排解
</div>

* 如果指令卡住，按 <Kbd>Ctrl+C</Kbd> 取消，並加入非互動式旗標
* 出現權限提示時，允許一次或按 <Kbd>Tab</Kbd> 加入允許清單
* 輸出被截斷時，按 <Kbd>Ctrl+O</Kbd> 展開
* 需要在不同目錄執行時，因為變更不會保留，請用 `cd <dir> && ...`
* Shell 模式會依 `$SHELL` 變數支援 zsh 與 bash

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="`cd` 會在不同執行之間保留嗎？">
    不會。每個指令都會獨立執行。請用 `cd <dir> && ...` 在不同目錄中執行指令。
  </Accordion>

  <Accordion title="可以更改逾時嗎？">
    不行。指令上限為 30 秒，且無法調整。
  </Accordion>

  <Accordion title="在哪裡設定權限？">
    權限由 CLI 與團隊設定管理。使用決策橫幅將指令加入允許清單。
  </Accordion>

  <Accordion title="怎麼退出 Shell 模式？">
    當輸入為空時按 <Kbd>Escape</Kbd>、在空輸入時按 <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd>，或按 <Kbd>Ctrl+C</Kbd> 以清除並退出。
  </Accordion>
</AccordionGroup>



# 在 CLI 中使用 Agent
Source: https://docs.cursor.com/zh-Hant/cli/using

使用 Cursor CLI 高效進行提問、審閱與反覆改進

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

<div id="prompting">
  ## 提示設計
</div>

清楚表達意圖能得到更好的結果。比如，你可以用提示「do not write any code」來確保代理不會編輯任何檔案。這在實作前規劃任務時特別有用。

代理目前具備檔案操作、搜尋，以及執行 shell 指令的工具。後續將持續加入更多工具，類似 IDE 代理。

<div id="mcp">
  ## MCP
</div>

Agent 支援 [MCP（Model Context Protocol）](/zh-Hant/tools/mcp) 以擴充功能與整合。CLI 會自動偵測並遵循你的 `mcp.json` 設定檔，啟用你在 IDE 中設定的相同 MCP 伺服器與工具。

<div id="rules">
  ## 規則
</div>

CLI 代理支援與 IDE 相同的[規則系統](/zh-Hant/context/rules)。你可以在 `.cursor/rules` 目錄中建立規則，為代理提供上下文與指引。這些規則會依其設定自動載入並套用，讓你能針對專案的不同部分或特定檔案類型，自訂代理的行為。

<Note>
  CLI 也會讀取專案根目錄（若存在）中的 `AGENTS.md` 與 `CLAUDE.md`，並與 `.cursor/rules` 一併作為規則套用。
</Note>

<div id="working-with-agent">
  ## 使用 Agent
</div>

<div id="navigation">
  ### 導覽
</div>

可以用向上箭頭（<Kbd>ArrowUp</Kbd>）存取先前訊息，並在其中循環瀏覽。

<div id="review">
  ### 審查
</div>

用 <Kbd>Cmd+R</Kbd> 審查變更。按 <Kbd>i</Kbd> 新增後續指示。用 <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> 捲動，用 <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> 切換檔案。

<div id="selecting-context">
  ### 選取上下文
</div>

用 <Kbd>@</Kbd> 選取要包含在上下文中的檔案與資料夾。執行 `/compress` 釋放上下文視窗的空間。詳見 [總結](/zh-Hant/agent/chat/summarization)。

<div id="history">
  ## 歷程
</div>

使用 `--resume [thread id]` 從既有執行緒繼續，載入先前的上下文。

若要繼續最近的一次對話，使用 `cursor-agent resume`。

也可以執行 `cursor-agent ls` 檢視先前對話的清單。

<div id="command-approval">
  ## 指令確認
</div>

在執行終端機指令之前，CLI 會請你確認（<Kbd>y</Kbd>）或拒絕（<Kbd>n</Kbd>）執行。

<div id="non-interactive-mode">
  ## 非互動模式
</div>

使用 `-p` 或 `--print` 以非互動模式執行 Agent。這會把回應輸出到主控台。

在非互動模式下，你可以以非互動的方式呼叫 Agent。這讓你能把它整合進腳本、CI 流程等。

你可以搭配 `--output-format` 來控制輸出格式。比如用 `--output-format json` 取得在腳本中較好解析的結構化輸出，或用 `--output-format text` 取得純文字輸出。

<Note>
  Cursor 在非互動模式下擁有完整寫入權限。
</Note>



# 鍵盤快捷鍵
Source: https://docs.cursor.com/zh-Hant/configuration/kbd

Cursor 的鍵盤快捷鍵與按鍵綁定

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

Cursor 的鍵盤快捷鍵總覽。按下 <Kbd>Cmd R</Kbd> 接著 <Kbd>Cmd S</Kbd> 來查看所有快捷鍵，或開啟指令面板 <Kbd>Cmd Shift P</Kbd> 並搜尋 `Keyboard Shortcuts`。

以 [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) 為基準，進一步了解 Cursor 的鍵盤快捷鍵，這也是 Cursor 的按鍵綁定參考。

所有 Cursor 的按鍵綁定（包含 Cursor 特有功能）都可以在 Keyboard Shortcuts 設定中重新對應。

<div id="general">
  ## 一般
</div>

<div className="full-width-table equal-table-columns">
  | 快捷鍵                    | 動作             |
  | ---------------------- | -------------- |
  | <Kbd>Cmd I</Kbd>       | 切換側邊欄（除非綁定到模式） |
  | <Kbd>Cmd L</Kbd>       | 切換側邊欄（除非綁定到模式） |
  | <Kbd>Cmd E</Kbd>       | 背景代理控制面板       |
  | <Kbd>Cmd .</Kbd>       | 模式選單           |
  | <Kbd>Cmd /</Kbd>       | 在 AI 模型間循環切換   |
  | <Kbd>Cmd Shift J</Kbd> | Cursor 設定      |
  | <Kbd>Cmd ,</Kbd>       | 一般設定           |
  | <Kbd>Cmd Shift P</Kbd> | 指令選單           |
</div>

<div id="chat">
  ## Chat
</div>

聊天輸入框的快捷鍵。

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action       |
  | ---------------------------------------------------- | ------------ |
  | <Kbd>Return</Kbd>                                    | 輕推（預設）       |
  | <Kbd>Ctrl Return</Kbd>                               | 將訊息加入佇列      |
  | <Kbd>Cmd Return</Kbd> when typing                    | 強制送出訊息       |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | 取消生成         |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | 將選取的程式碼加入為脈絡 |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | 將剪貼簿內容加入為脈絡  |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | 將剪貼簿內容加入輸入框  |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | 接受所有變更       |
  | <Kbd>Cmd Backspace</Kbd>                             | 拒絕所有變更       |
  | <Kbd>Tab</Kbd>                                       | 切換到下一則訊息     |
  | <Kbd>Shift Tab</Kbd>                                 | 切換到上一則訊息     |
  | <Kbd>Cmd Opt /</Kbd>                                 | 切換模型         |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | 新增聊天         |
  | <Kbd>Cmd T</Kbd>                                     | 新增聊天分頁       |
  | <Kbd>Cmd \[</Kbd>                                    | 上一個聊天        |
  | <Kbd>Cmd ]</Kbd>                                     | 下一個聊天        |
  | <Kbd>Cmd W</Kbd>                                     | 關閉聊天         |
  | <Kbd>Escape</Kbd>                                    | 取消欄位焦點       |
</div>

<div id="inline-edit">
  ## Inline Edit
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut                       | Action |
  | ------------------------------ | ------ |
  | <Kbd>Cmd K</Kbd>               | 開啟     |
  | <Kbd>Cmd Shift K</Kbd>         | 切換輸入焦點 |
  | <Kbd>Return</Kbd>              | 提交     |
  | <Kbd>Cmd Shift Backspace</Kbd> | 取消     |
  | <Kbd>Opt Return</Kbd>          | 快速提問   |
</div>

<div id="code-selection-context">
  ## 程式碼選取與上下文
</div>

<div className="full-width-table equal-table-columns">
  | 快捷鍵                                           | 動作                                  |
  | --------------------------------------------- | ----------------------------------- |
  | <Kbd>@</Kbd>                                  | [@ 符號](/zh-Hant/context/@-symbols/) |
  | <Kbd>#</Kbd>                                  | 檔案                                  |
  | <Kbd>/</Kbd>                                  | 快捷指令                                |
  | <Kbd>Cmd Shift L</Kbd>                        | 把選取加入 Chat                          |
  | <Kbd>Cmd Shift K</Kbd>                        | 把選取加入 Edit                          |
  | <Kbd>Cmd L</Kbd>                              | 把選取加入新聊天                            |
  | <Kbd>Cmd M</Kbd>                              | 切換檔案讀取策略                            |
  | <Kbd>Cmd →</Kbd>                              | 接受建議的下一個字                           |
  | <Kbd>Cmd Return</Kbd>                         | 在聊天中搜尋程式碼庫                          |
  | 選取程式碼，<Kbd>Cmd C</Kbd>，<Kbd>Cmd V</Kbd>       | 將複製的參考程式碼加入為上下文                     |
  | 選取程式碼，<Kbd>Cmd C</Kbd>，<Kbd>Cmd Shift V</Kbd> | 將複製的程式碼以文字上下文加入                     |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | 快捷鍵              | 動作      |
  | ---------------- | ------- |
  | <Kbd>Tab</Kbd>   | 接受建議    |
  | <Kbd>Cmd →</Kbd> | 接受下一個單字 |
</div>

<div id="terminal">
  ## 終端機
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Action   |
  | --------------------- | -------- |
  | <Kbd>Cmd K</Kbd>      | 開啟終端機提示列 |
  | <Kbd>Cmd Return</Kbd> | 執行產生的指令  |
  | <Kbd>Escape</Kbd>     | 接受指令     |
</div>



# Shell 指令
Source: https://docs.cursor.com/zh-Hant/configuration/shell

安裝並使用 Cursor 的 shell 指令

Cursor 提供命令列工具，讓你可以直接從終端機開啟檔案和資料夾。安裝 `cursor` 和 `code` 兩個指令，把 Cursor 無縫整合進你的開發流程。

<div id="installing-cli-commands">
  ## 安裝 CLI 指令
</div>

透過 Command Palette 安裝 CLI 指令：

1. 開啟 Command Palette（Cmd/Ctrl + P）
2. 輸入「Install」以篩選安裝指令
3. 選取並執行 `Install 'cursor' to shell`
4. 重複並選取 `Install 'code' to shell`

<product_visual type="screenshot">
  Command Palette 顯示 CLI 安裝選項
</product_visual>

<div id="using-the-cli-commands">
  ## 使用 CLI 指令
</div>

安裝完成後，可用以下任一指令在 Cursor 中開啟檔案或資料夾：

```bash  theme={null}

# 使用 cursor 指令
cursor path/to/file.js
cursor path/to/folder/


# 使用 code 指令（與 VS Code 相容）
code path/to/file.js
code path/to/folder/
```

<div id="command-options">
  ## 指令選項
</div>

兩個指令都支援以下選項：

* 開啟檔案：`cursor file.js`
* 開啟資料夾：`cursor ./my-project`
* 同時開啟多個項目：`cursor file1.js file2.js folder1/`
* 在新視窗中開啟：`cursor -n` 或 `cursor --new-window`
* 等待視窗關閉後結束：`cursor -w` 或 `cursor --wait`

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="cursor 跟 code 指令有什麼差別？">
    沒有差別。提供 `code` 指令是為了與 VS Code 相容。
  </Accordion>

  <Accordion title="需要同時安裝這兩個指令嗎？">
    不用，照自己的偏好裝其中一個或兩個都可以。
  </Accordion>

  <Accordion title="指令會安裝在哪裡？">
    指令會安裝到系統預設的 shell 設定檔（例如 `.bashrc`、`.zshrc` 或 `.config/fish/config.fish`）。
  </Accordion>
</AccordionGroup>



# 主題
Source: https://docs.cursor.com/zh-Hant/configuration/themes

自訂 Cursor 的外觀

Cursor 支援淺色與深色主題，讓你的編碼環境更順眼。Cursor 承襲 VS Code 的主題系統 —— 你可以使用任何 VS Code 主題、建立自訂主題，並從 Marketplace 安裝主題擴充套件。

<div id="changing-theme">
  ## 更換主題
</div>

1. 開啟 Command Palette（Cmd/Ctrl + P）
2. 輸入「theme」來篩選指令
3. 選擇「Preferences: Color Theme」
4. 選擇主題

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de83bbba983509af2002e4dfafe703ff" alt="Cursor 的主題選擇選單，顯示可用的色彩主題" data-og-width="3584" width="3584" data-og-height="2072" height="2072" data-path="images/config/themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=85b365baa01a725becb482e69eed6292 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=46eb0bed7d0d98612968135d727ee838 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8629851793f4498e7639ee4347484c88 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ea75113e217cc84f99f8f6d63af34ade 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ec5b85b5a4464d2af801f92b317a7e31 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=54fc29efe263f9935ba3273675ced7be 2500w" />
</Frame>

<div id="faq">
  ## 常見問題
</div>

<AccordionGroup>
  <Accordion title="可以在 Cursor 使用我的 VS Code 主題嗎？">
    可以！Cursor 與 VS Code 主題相容。你可以安裝任何 VS Code Marketplace 上的主題，或是複製自訂主題檔案。
  </Accordion>

  <Accordion title="要怎麼建立自訂主題？">
    和在 VS Code 裡的做法一樣。使用「Developer: Generate Color Theme From Current Settings」從目前設定產生主題，或參考 VS Code 的主題製作指南。
  </Accordion>
</AccordionGroup>



# @Code
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-code

使用 @Code 在 Cursor 中引用特定程式碼片段

使用 `@Code` 符號來引用特定的程式碼區段。相較於 [`@Files & Folders`](/zh-Hant/context/@-symbols/@-files-and-folders)，它提供更細緻的控管，讓你能選取精準的程式碼片段，而不是整個檔案。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fba3d385441084e243cd168eee8c9a9a" data-og-width="1850" width="1850" data-og-height="948" height="948" data-path="images/context/symbols/@-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6337ef4855301fdfef729012783d3cee 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ef348ae46e4a51ee298a6a5fa356eebd 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40ec3857dd21120790037ea409fac80d 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=604bfeb6907e96da64b1f814681232c8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cee1a79d449a4d163f566a6013b69318 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d4bb99b85dfa5ad539e63c3670171abe 2500w" />
</Frame>



# @Cursor 規則
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-cursor-rules

套用專案特定的規則與指引

`@Cursor 規則` 符號可讓你存取你設定的[專案規則](/zh-Hant/context/rules)與指引，並能將它們明確套用到你的情境中。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e2f45682a0b471e5726cd5452ab6bceb" data-og-width="1518" width="1518" data-og-height="973" height="973" data-path="images/context/symbols/@-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6e67889ef0390f9be3c557247469c95b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1c22061fe8c8d000deeabbf404f1650d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a220fd7fbef492c2d523ed9e31324666 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44224ba38fd2a5460963b884c994d178 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=df766d5499d8b54ca4fa2211600515f6 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a06393ddd0d85711ad72d7b8991946a5 2500w" />
</Frame>



# @Files & Folders
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-files-and-folders

在 Chat 與 Inline Edit 中將檔案與資料夾作為參考脈絡

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

<div id="files">
  ## 檔案
</div>

在 Chat 和 Inline Edit 中，選擇 `@Files & Folders`，再輸入要搜尋的檔名，就能引用整個檔案。也可以把側邊欄的檔案直接拖曳到 Agent，作為上下文。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8d46d3c961a3e898fd12c0cc1e1c8dce" data-og-width="2227" width="2227" data-og-height="1414" height="1414" data-path="images/context/symbols/@-files-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a3a78c7a6d2311a31efb941c40fbe11b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bfe1eff4516dce93f789e560e92f14ad 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=462239ebfd0181acfe36d2f937f32ca6 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1a64cd3cc0a07825c51d70c40dfe72fd 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=64ea129f283dd98fd9814820d6684a99 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b40e591d3e500f06eeb32fac49d4f90c 2500w" />
</Frame>

<div id="folders">
  ## 資料夾
</div>

當用 `@Folders` 參照資料夾時，Cursor 會提供資料夾路徑與其內容概覽，幫助 AI 瞭解可用的內容。

<Tip>
  選到資料夾後，輸入「/」即可深入瀏覽並查看所有子資料夾。
</Tip>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a102e1c1cb7180c3ec6a1356273839a" data-og-width="2150" width="2150" data-og-height="1367" height="1367" data-path="images/context/symbols/@-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4b91de3b118c842aec8e1da04ca233d2 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fcba40013ff1349c28382151b52d5853 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=83cc5ac8db19a0d59de9a980c0ea10d7 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b87a80a369b62d48a2363a97a391de2 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29e93d39857f71ba7e00947e209514de 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa9b88463b43fa482c0654a0a0b362ca 2500w" />
</Frame>

<div id="full-folder-content">
  ### 完整資料夾內容
</div>

在設定中啟用 **完整資料夾內容**。啟用後，Cursor 會嘗試將該資料夾中的所有檔案納入上下文。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ee37944a2e874a708b9d8281a063e580" data-og-width="1996" width="1996" data-og-height="296" height="296" data-path="images/context/symbols/folder-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=09520107c0518601c58f099ed119adab 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=748aecb97c43066f0be03416f9ed6ed0 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fd7e7c816092c9eed3182382fa77ff8f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=91baab4860e0f671196607f3c364b4d8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d2450ee2fcd6d8c59ba2412fad11121 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f4690bdb099c27092b9ddb6143bd8068 2500w" />
</Frame>

對於超出上下文視窗的大型資料夾，會出現大綱檢視，並附帶工具提示顯示已納入的檔案數量，同時由 Cursor 管理可用的上下文空間。

<Note>
  在[啟用 Max 模式](/zh-Hant/context/max-mode)下使用完整資料夾內容，
  由於會消耗更多輸入 token，請求成本將顯著增加。
</Note>

<div id="context-management">
  ## 內容管理
</div>

大型檔案與資料夾會自動壓縮摘要，以符合上下文限制。詳情請參考 [檔案與資料夾濃縮](/zh-Hant/agent/chats/summarization#file--folder-condensation)。



# @Git
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-git

參照 Git 的變更與分支差異

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=dba4c696d66e1274b96bf3261c8d927b" data-og-width="1658" width="1658" data-og-height="932" height="932" data-path="images/context/symbols/@-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=69bf90d13f034275fb78ab48e71d25ac 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e8c89a03ebdd5a1c1a576c8555380957 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ec7309f9ec4364c4ac0d237a9977f23 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f2d82f1eb2be6275c8b91ae63e943ee7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4e27a0a13a731fc0fe85a85a327f9884 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa1acf93e5e87b7a81d766a52601960d 2500w" />
</Frame>

* `@Commit`: 參照相較於上一個 commit 的目前工作區變更。會顯示所有尚未提交的已修改、已新增與已刪除檔案。
* `@Branch`: 將目前分支的變更與 main 分支比較。會顯示你分支中所有在 main 中不存在的 commits 與變更。



# @Link
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-link

貼上 URL 就能匯入網頁內容

在 Chat 里貼上 URL 時，Cursor 會自動把它標記為 `@Link`，並擷取內容作為上下文使用。也支援 PDF 文件——只要是可公開存取的 PDF 連結，Cursor 都能擷取並解析其中的文字內容。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d96b384a0480aba7981b6fbebee1fac8" data-og-width="1618" width="1618" data-og-height="1035" height="1035" data-path="images/context/symbols/@-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d251326cc25b2835488b1f25b05f2c4f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d1b64f393d89cfc547c6e12ae7a6adef 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d5a2aa41c6a6affea03379adac5e76c8 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e94e2c0610eafea625996386374e8898 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=404333e65fa1c98e2e92fd941d2e8b92 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=63d9a66571fde75678b6fa0d0cbac44f 2500w" />
</Frame>

<div id="unlink">
  ## 取消連結
</div>

如果想把 URL 當純文字使用，而不抓取其內容：

* 點一下已標記的連結，選擇 `Unlink`
* 或在貼上時按住 `Shift`，避免自動加上標記

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5eca9b93aa4c2ba4f8d0f6a97a34052f" data-og-width="1212" width="1212" data-og-height="408" height="408" data-path="images/context/symbols/@-link-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=be5f171437d0d3c79ded195c7a387741 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ca29084e45c832b6aa9015fcd5cf680 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eb394772d364e392ff794c43ed1fbfcc 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5df343df91b3bf4aed9edb32fc192059 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a35df3274c439984b2072eb758d05fb1 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a20f166b838435ade65084c844cc3c6a 2500w" />
</Frame>



# @Linter Errors
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-linter-errors

存取並參照程式碼庫中的 lint 錯誤

`@Linter Errors` 符號會自動擷取並提供目前作用中文件中的 lint 錯誤與警告脈絡。[Agent](/zh-Hant/agent/overview) 預設就能看到 lint 錯誤。

<Note>
  要讓 linter 錯誤可見，需要為你的程式語言安裝並設定相對應的語言伺服器（Language Server）。Cursor
  會自動偵測並使用已安裝的語言伺服器，不過你可能還是得為特定語言安裝額外的擴充或工具。
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6ef34b3ae96a7d49695035cb5c3ac9f9" data-og-width="1590" width="1590" data-og-height="1017" height="1017" data-path="images/context/symbols/@-linter-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13e682f26536e5cb104142bcc7becbeb 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cf3947376ee2e17f83c08809b23e864c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13d026063f9bc5e61c78740fee8eebc5 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29c834609d2f549b295be53cdbf7eec6 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b2131adda5b89685d7d7a26ed218fee 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9cd3c3e34cbee0f73fe478024018539 2500w" />
</Frame>



# @Past Chats
Source: https://docs.cursor.com/zh-Hant/context/@-symbols/@-past-chats

將歷史對話的重點摘要納入脈絡

在 [Chat](/zh-Hant/chat) 中處理複雜任務時，你可能需要引用先前對話的脈絡或決策。`@Past Chats` 符號會把先前的對話整理成摘要，作為脈絡提供參考。

特別適用於：

* 你有一段需要引用重要脈絡的長 Chat 工作階段
* 你正開始一個相關的新任務，想保持延續性
* 你想分享先前工作階段中的推理或決策

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6839cf571e64e1ed10dd5dc270d4ac45" data-og-width="2340" width="2340" data-og-height="1485" height="1485" data-path="images/context/symbols/@-past-chats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0278e6fdce8d8771ecd6f64faf5048db 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3a2d4722e90c1078c11fcd695993d84a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d46e21680b56820aef7a9baf34891e0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f19f25e6988729059f40731378ce4fab 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=86f9457d09e7dd4578c8609fd3cff6b5 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8efb9e097f9e434d0b7f03cac9b02396 2500w" />
</Frame>




---

**Navigation:** [← Previous](./38-geliştiriciler.md) | [Index](./index.md) | [Next →](./40-recent-changes.md)