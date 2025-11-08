---
title: "The app chrome"
source: https://docs.streamlit.io/develop/concepts/architecture/app-chrome
section: 21
---

# The app chrome

Source: https://docs.streamlit.io/develop/concepts/architecture/app-chrome


Your Streamlit app has a few widgets in the top right to help you as you develop. These widgets also help your viewers as they use your app. We call this things “the app chrome”. The chrome includes a status area, toolbar, and app menu.

Your app menu is configurable. By default, you can access developer options from the app menu when viewing an app locally or on Streamlit Community Cloud while logged into an account with administrative access. While viewing an app, click the icon in the upper-right corner to access the menu.

![App menu](/images/app-menu/app-menu-developer.png)

## Menu options

The menu is split into two sections. The upper section contains options available to all viewers and the lower section contains options for developers. Read more about [customizing this menu](#customize-the-menu) at the end of this page.

### Rerun

You can manually trigger a rerun of your app by clicking "**Rerun**" from the app menu. This rerun will not reset your session. Your widget states and values stored in [`st.session_state`](/develop/concepts/architecture/session-state) will be preserved. As a shortcut, without opening the app menu, you can rerun your app by pressing "**R**" on your keyboard (if you aren't currently focused on an input element).

### Settings

With the "**Settings**" option, you can control the appearance of your app while it is running. If viewing the app locally, you can set how your app responds to changes in your source code. See more about development flow in [Basic concepts](/get-started/fundamentals/main-concepts#development-flow). You can also force your app to appear in wide mode, even if not set within the script using [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

#### Theme settings

After clicking "**Settings**" from the app menu, you can choose between "**Light**", "**Dark**", or "**Use system setting**" for the app's base theme. Click "**Edit active theme**" to modify the theme, color-by-color.

<div>{{ maxWidth: '90%', margin: '0 2em 0 2em' }}&gt;
    <Image alt="Settings" src="/images/app-menu/app-menu-settings-modal.png"/>
</div>

---

[← Previous](20-understanding-streamlits-client-server-architecture.md) | [Index](index.md) | [Next →](index.md)
