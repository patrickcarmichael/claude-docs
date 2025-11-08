**Navigation:** [← Previous](./09-2025-release-notes.md) | [Index](./index.md) | [Next →](./11-deploy-an-app-from-a-template.md)

---

# 2023 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2023


This page contains release notes for Streamlit versions released in 2023. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## **Version 1.29.0**

_Release date: November 30, 2023_

**Highlights**

- 🔲 [`st.container`](/develop/api-reference/layout/st.container) and [`st.form`](/develop/api-reference/execution-flow/st.form) now have a `border` parameter to show or hide a border.
- 🐍 Streamlit supports Python 3.12!

**Notable Changes**

- ⌛ `st.dataframe`, `st.data_editor`, and `st.table` support `datetime.timedelta` values ([#7689](https://github.com/streamlit/streamlit/pull/7689), [#4489](https://github.com/streamlit/streamlit/issues/4489)).
- 💀 Streamlit apps preload skeleton elements for a smoother appearance when initializing ([#7598](https://github.com/streamlit/streamlit/pull/7598)).
- 🏃 Reduced the overhead of running `AppTest`-simulated apps, especially for fast-running apps ([#7691](https://github.com/streamlit/streamlit/pull/7691)).
- 🛁 String representations of `AppTest` data are improved for a better testing and debugging experience ([#7658](https://github.com/streamlit/streamlit/pull/7658)).
- 🔢 Apps can be configured to identify `Enum` classes as the same if they have matching member names ([#7408](https://github.com/streamlit/streamlit/pull/7408), [#4909](https://github.com/streamlit/streamlit/issues/4909)). Thanks, [Asaurus1](https://github.com/Asaurus1)!
- ❌ The "Made with Streamlit" footer no longer appears at the bottom of apps ([#7583](https://github.com/streamlit/streamlit/pull/7583)).
- 🧹 Unused config options have been deprecated ([#7584](https://github.com/streamlit/streamlit/pull/7584)).
- 🕳️ Query parameters can be empty ([#7601](https://github.com/streamlit/streamlit/pull/7601), [#7416](https://github.com/streamlit/streamlit/issues/7416)).
- 💅 Visual tweaks ([#7592](https://github.com/streamlit/streamlit/pull/7592), [#7630](https://github.com/streamlit/streamlit/pull/7630)).

**Other Changes**

- 🦗 Bug fix: Convert floats to bytes instead of hashing to avoid hashing instability ([#7754](https://github.com/streamlit/streamlit/pull/7754)). Thanks, [BlackHC](https://github.com/BlackHC)!
- 🦎 Bug fix: Corrected broken URLs and typos in error messages ([#7746](https://github.com/streamlit/streamlit/pull/7746), [#7764](https://github.com/streamlit/streamlit/pull/7764), [#7770](https://github.com/streamlit/streamlit/pull/7770)). Thanks, [ObservedObserver](https://github.com/ObservedObserver)!
- 🐌 Bug fix: `st.connection` correctly caches results when using two connections of the same type ([#7730](https://github.com/streamlit/streamlit/pull/7730), [#7709](https://github.com/streamlit/streamlit/issues/7709)).
- 🕸️ Bug fix: Using context managers with multithreading now displays content in the expected order ([#7715](https://github.com/streamlit/streamlit/pull/7715), [#7668](https://github.com/streamlit/streamlit/issues/7668)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
- 🦂 Bug fix: Added https fallback when obtaining the host machine's address ([#7712](https://github.com/streamlit/streamlit/pull/7712), [#7703](https://github.com/streamlit/streamlit/issues/7703)). Thanks, [LarsHill](https://github.com/LarsHill)!
- 🛡️ Bug fix: Added security patch for `pyarrow` vulnerability. Custom components using `pyarrow` table deserialization should require `pyarrow&gt;=14.0.1` ([#7695](https://github.com/streamlit/streamlit/pull/7695), [#7700](https://github.com/streamlit/streamlit/issues/7700)).
- 🦟 Bug fix: Improved typing for `st.connection` ([#7671](https://github.com/streamlit/streamlit/pull/7671)). Thanks, [thezanke](https://github.com/thezanke)!
- 🪰 Bug fix: Retries of `SnowflakeConnection` methods are narrowed to only occur with transient errors to avoid unnecessary repeated errors ([#7645](https://github.com/streamlit/streamlit/pull/7645), [#7637](https://github.com/streamlit/streamlit/issues/7637)).
- 🏗️ Removed the v0 testing framework which was undocumented ([#7657](https://github.com/streamlit/streamlit/pull/7657)).
- 🪳 Bug fix: The navigation expander arrow no longer disappears ([#7634](https://github.com/streamlit/streamlit/pull/7634), [#7547](https://github.com/streamlit/streamlit/issues/7547)).
- ❄️ Improved the error message for `SnowflakeConnection` when a configuration is not found ([#7652](https://github.com/streamlit/streamlit/pull/7652)).
- 🕷️ Bug fix: `st.rerun` no longer causes a `RecursionError` when used with `st.chat_input` ([#7643](https://github.com/streamlit/streamlit/pull/7643), [#7629](https://github.com/streamlit/streamlit/issues/7629)).
- 🐞 Bug fix: `st.file_uploader` no longer causes an extra rerun and therefore doesn't conflict with `st.chat_input` ([#7641](https://github.com/streamlit/streamlit/pull/7641), [#7556](https://github.com/streamlit/streamlit/issues/7556)).
- 🐝 Bug fix: `AppTest` no longer raises an error when encountering `st.container` ([#7644](https://github.com/streamlit/streamlit/pull/7644), [#7636](https://github.com/streamlit/streamlit/issues/7636)).
- 🪲 Bug fix: Graphviz charts scale correctly when exiting fullscreen view ([#7398](https://github.com/streamlit/streamlit/pull/7398), [#7527](https://github.com/streamlit/streamlit/issues/6527)).
- 🎥 Bug fix: "Record a screencast" is hidden when known to be unsupported in a browser ([#7604](https://github.com/streamlit/streamlit/pull/7604)).
- 🐛 Bug fix: Increased the top padding of embedded apps to better display the dataframe toolbar ([#7681](https://github.com/streamlit/streamlit/pull/7681), [#7609](https://github.com/streamlit/streamlit/pull/7609), [#7607](https://github.com/streamlit/streamlit/issues/7607)).
- 🐜 Bug fix: `st.rerun` uses `NoReturn` for improved type checking ([#7422](https://github.com/streamlit/streamlit/pull/7422)) Thanks, [kongzii](https://github.com/kongzii).

## **Version 1.28.0**

_Release date: October 26, 2023_

**Release videos**

- [Introducing `AppTest`](https://www.youtube.com/watch?v=99OEoP5sy0U)

**Highlights**

- 🧪 Introducing a new testing framework for Streamlit apps! Check out our [documentation](/develop/api-reference/app-testing) to learn how to build automated tests for your apps.
- 💻 Announcing the general availability of `st.connection`, a command to conveniently manage connections in Streamlit apps. Check out the [docs](/develop/api-reference/connections/st.connection) to learn more.
- ❄️ `SnowparkConnection` has been upgraded to the new and improved `SnowflakeConnection` — the same, great functionality _plus more_! Check out our [built-in connections](/develop/api-reference/connections#built-in-connections).
- 🛠️ `st.dataframe` and `st.data_editor` have a new toolbar! Users can search and download data in addition to enjoying improved UI for row additions and deletions. See our updated guide on [Dataframes](/develop/concepts/design/dataframes).

**Notable Changes**

- 🌀 When using a spinner with cached functions, the spinner will be overlaid instead of pushing content down ([#7488](https://github.com/streamlit/streamlit/pull/7488)).
- 📅 `st.data_editor` now supports datetime index editing ([#7483](https://github.com/streamlit/streamlit/pull/7483)).
- 🔢 Improved support for `decimal.Decimal` in `st.dataframe` and `st.data_editor` ([#7475](https://github.com/streamlit/streamlit/pull/7475)).
- 🥸 Global kwargs were added for `hashlib` ([#7527](https://github.com/streamlit/streamlit/pull/7527), [#7526](https://github.com/streamlit/streamlit/issues/7526)). Thanks, [DueViktor](https://github.com/DueViktor)!
- 📋 `st.components.v1.iframe` now permits writing to clipboard ([#7487](https://github.com/streamlit/streamlit/pull/7487)). Thanks, [dilipthakkar](https://github.com/dilipthakkar)!
- 📝 `SafeSessionState` disconnect was replaced with script runner yield points for improved efficiency and clarity ([#7373](https://github.com/streamlit/streamlit/pull/7373)).
- 🤖 The Langchain callback handler will show the full input string inside the body of a `st.status` when the input string is too long to show as a label ([#7478](https://github.com/streamlit/streamlit/pull/7478)). Thanks, [pokidyshev](https://github.com/pokidyshev)!
- 📈 `st.graphviz_chart` now supports using different Graphviz layout engines ([#7505](https://github.com/streamlit/streamlit/pull/7505), [#4089](https://github.com/streamlit/streamlit/issues/4089)).
- 🦋 Assorted visual tweaks ([#7486](https://github.com/streamlit/streamlit/pull/7486), [#7592](https://github.com/streamlit/streamlit/pull/7592)).
- 📊 `plotly.js` was upgraded to version 2.26.1 ([#7449](https://github.com/streamlit/streamlit/pull/7449), [#7476](https://github.com/streamlit/streamlit/issues/7476), [#7045](https://github.com/streamlit/streamlit/issues/7045)).
- 💽 Legacy serialization for DataFrames was removed. All DataFrames will be serialized by Apache Arrow ([#7429](https://github.com/streamlit/streamlit/pull/7429)).
- 🖼️ Compatibility for Pillow 10.x was added ([#7442](https://github.com/streamlit/streamlit/pull/7442)).
- 📬 Migrated `_stcore/allowed-message-origins` endpoint to `_stcore/host-config` ([#7342](https://github.com/streamlit/streamlit/pull/7342)).
- 💬 Added `post_parent_message` platform command to send custom messages from a Streamlit app to its parent window ([#7522](https://github.com/streamlit/streamlit/pull/7522)).

**Other Changes**

- ⌨️ Improved string dtype handling for DataFrames ([#7479](https://github.com/streamlit/streamlit/pull/7479)).
- ✒️ `st.write` will avoid using `unsafe_allow_html=True` if possible ([#7432](https://github.com/streamlit/streamlit/pull/7432)).
- 🐛 Bug fix: Implementation of `st.expander` was simplified for improved behavior and consistency ([#7247](https://github.com/streamlit/streamlit/pull/7247), [#2839](https://github.com/streamlit/streamlit/issues/2839), [#4111](https://github.com/streamlit/streamlit/issues/4111), [#4651](https://github.com/streamlit/streamlit/issues/4651), [#5604](https://github.com/streamlit/streamlit/issues/5604)).
- 🪲 Bug fix: Multipage links in the sidebar are now aligned with other sidebar elements ([#7531](https://github.com/streamlit/streamlit/pull/7531)).
- 🐜 Bug fix: `st.chat_input` won't incorrectly prompt for `label` parameter in IDEs ([#7560](https://github.com/streamlit/streamlit/pull/7560)).
- 🐝 Bug fix: Scroll bars correctly overlay `st.dataframe` and `st.data_editor` without adding empty space ([#7090](https://github.com/streamlit/streamlit/pull/7090), [#6888](https://github.com/streamlit/streamlit/issues/6888)).
- 🐞 Bug fix: `st.chat_message` behaves correctly with the removal of AutoSizer ([#7504](https://github.com/streamlit/streamlit/pull/7504), [#7473](https://github.com/streamlit/streamlit/issues/7473)).
- 🕷️ Bug fix: Anchor links are reliably produced for non-English headers ([#7454](https://github.com/streamlit/streamlit/pull/7454), [#5291](https://github.com/streamlit/streamlit/issues/5291)).
- ☃️ Bug fix: `st.connections.SnowparkConnection` more accurately detects when it's running within Streamlit in Snowflake ([#7502](https://github.com/streamlit/streamlit/pull/7502)).
- 🪳 Bug fix: A user-friendly warning is shown when exceeding the size limitations of a pandas `Styler` object ([#7497](https://github.com/streamlit/streamlit/pull/7497), [#5953](https://github.com/streamlit/streamlit/issues/5953)).
- 🪰 Bug fix: `st.data_editor` automatically converts non-string column names to strings ([#7485](https://github.com/streamlit/streamlit/pull/7485), [#6950](https://github.com/streamlit/streamlit/issues/6950)).
- 🦠 Bug fix: `st.data_editor` correctly identifies non-range indices as a required column ([#7481](https://github.com/streamlit/streamlit/pull/7481), [#6995](https://github.com/streamlit/streamlit/issues/6995)).
- 🦟 Bug fix: `st.file_uploader` displays compound file extensions like `csv.gz` correctly ([#7362](https://github.com/streamlit/streamlit/pull/7362)). Thanks, [mo42](https://github.com/mo42)!
- 🦂 Bug fix: Column Configuration no longer uses deprecated type checks ([#7496](https://github.com/streamlit/streamlit/pull/7496), [#7477](https://github.com/streamlit/streamlit/pull/7477), [#7550](https://github.com/streamlit/streamlit/issues/7550)). Thanks, [c-bik](https://github.com/c-bik)!
- 🦗 Bug fix: Additional toolbar items no longer stack vertically ([#7470](https://github.com/streamlit/streamlit/pull/7470), [#7471](https://github.com/streamlit/streamlit/issues/7471)).
- 🕸️ Bug fix: Column Configuration no longer causes a type warning in Mypy ([#7457](https://github.com/streamlit/streamlit/pull/7457)). Thanks, [kopp](https://github.com/kopp)!
- 🐌 Bug fix: Bokeh Sliders no longer cause JavaScript errors ([#7441](https://github.com/streamlit/streamlit/pull/7441), [#7171](https://github.com/streamlit/streamlit/issues/7171)).
- 🦎 Bug fix: Caching now recognizes DataFrames with the same values but different column names as different ([#7331](https://github.com/streamlit/streamlit/pull/7331), [#7086](https://github.com/streamlit/streamlit/issues/7086)).

## **Version 1.27.0**

_Release date: September 21, 2023_

**Highlights**

- ✨ Introducing `st.scatter_chart` — a new, simple chart element to build scatter charts Streamlit-y fast and easy! See our [documentation](/develop/api-reference/charts/st.scatter_chart).
- 🔗 Introducing `st.link_button`! Want to open an external link in a new tab with a bit more pizazz than a plain-text link? Check out our [documentation](/develop/api-reference/widgets/st.link_button) to see how.
- 🏃 Announcing the general availability of [`st.rerun`](/develop/api-reference/execution-flow/st.rerun), a command to interrupt your script and trigger an immediate rerun.

**Notable Changes**

- 👻 You can initialize widgets with an empty state by setting `None` as an initial value for [`st.number_input`](/develop/api-reference/widgets/st.number_input), [`st.selectbox`](/develop/api-reference/widgets/st.selectbox), [`st.date_input`](/develop/api-reference/widgets/st.date_input), [`st.time_input`](/develop/api-reference/widgets/st.time_input), [`st.radio`](/develop/api-reference/widgets/st.radio), [`st.text_input`](/develop/api-reference/widgets/st.text_input), and [`st.text_area`](/develop/api-reference/widgets/st.text_area)!
- 📤 [`st.download_button`](/develop/api-reference/widgets/st.download_button) now uses `target="_self"` instead of opening a new tab ([#7151](https://github.com/streamlit/streamlit/pull/7151), [#7132](https://github.com/streamlit/streamlit/issues/7132)).
- 🧟 Removed unmaintained `pympler` dependency ([#7193](https://github.com/streamlit/streamlit/pull/7193), [#7131](https://github.com/streamlit/streamlit/issues/7131)). Thanks, [rudyardrichter](https://github.com/rudyardrichter)!

**Other Changes**

- 🐛 Bug fix: `st.multiselect` now shows a correct message when no result matches a user's search ([#7205](https://github.com/streamlit/streamlit/pull/7205), [#7116](https://github.com/streamlit/streamlit/issues/7116)).
- 🪲 Bug fix: `st.experimental_user` now defaults to `test@example.com` ([#7219](https://github.com/streamlit/streamlit/pull/7219), [#7215](https://github.com/streamlit/streamlit/issues/7215)).
- 🐜 Bug fix: `st.slider` labels don't overlap when small ranges are selected ([#7221](https://github.com/streamlit/streamlit/pull/7221), [#3385](https://github.com/streamlit/streamlit/issues/3385)).
- 🐝 Bug fix: Type-checking correctly identifies all string types to avoid hashing errors ([#7255](https://github.com/streamlit/streamlit/pull/7255), [#6455](https://github.com/streamlit/streamlit/issues/6455)).
- 🐞 Bug fix: JSON is parsed with JSON5 to avoid errors from null values when using `st.pydeck_chart` ([#7256](https://github.com/streamlit/streamlit/pull/7256), [#5799](https://github.com/streamlit/streamlit/issues/5799)).
- 🕷️ Bug fix: Identical widgets on different pages are correctly interpreted by Streamlit as distinct ([#7264](https://github.com/streamlit/streamlit/pull/7264), [#6146](https://github.com/streamlit/streamlit/issues/6146)).
- 🦋 Bug fix: Visual tweaks to widgets for responsive behavior ([#7145](https://github.com/streamlit/streamlit/pull/7145)).
- 🪳 Bug fix: SVGs are accurately displayed ([#7183](https://github.com/streamlit/streamlit/pull/7183), [#3882](https://github.com/streamlit/streamlit/issues/3882)).
- 🪰 Bug fix: `st.video` correctly updates with changes to `start_time` ([#7257](https://github.com/streamlit/streamlit/pull/7257), [#7126](https://github.com/streamlit/streamlit/issues/7126)).
- 🦠 Bug fix: Additional error handling was added to `st.session_state` ([#7280](https://github.com/streamlit/streamlit/pull/7280), [#7206](https://github.com/streamlit/streamlit/issues/7206)).
- 🦟 Bug fix: `st.map` correctly refreshes with new data ([#7307](https://github.com/streamlit/streamlit/pull/7307), [#7294](https://github.com/streamlit/streamlit/issues/7294)).
- 🦂 Bug fix: The decorative app header line is no longer covered by the sidebar ([#7297](https://github.com/streamlit/streamlit/pull/7297), [#6264](https://github.com/streamlit/streamlit/issues/6264)).
- 🦗 Bug fix: `st.code` no longer triggers a `CachedStFunctionWarning` ([#7306](https://github.com/streamlit/streamlit/pull/7306), [#7055](https://github.com/streamlit/streamlit/issues/7055)).
- 🕸️ Bug fix: `st.download_button` no longer resets with different `data` ([#7316](https://github.com/streamlit/streamlit/pull/7316), [#7308](https://github.com/streamlit/streamlit/issues/7308)).
- 🐌 Bug fix: Widgets consistently recognize user interaction while a page is still running, with or without `fastRerun` enabled ([#7283](https://github.com/streamlit/streamlit/pull/7283), [#6643](https://github.com/streamlit/streamlit/issues/6643)).
- 🦎 Bug fix: `st.tabs` was improved to better handle and render conditionally appearing tabs ([#7287](https://github.com/streamlit/streamlit/pull/7287), [#7310](https://github.com/streamlit/streamlit/pull/7310), [#5454](https://github.com/streamlit/streamlit/issues/5454), [#7040](https://github.com/streamlit/streamlit/issues/7040)).

## **Version 1.26.0**

_Release date: August 24, 2023_

**Highlights**

- 🤖 Introducing `st.status` to display output from long-running processes and external API calls ([#7140](https://github.com/streamlit/streamlit/pull/7140)). Works great with `st.chat_message`! See our [documentation](/develop/api-reference/status/st.status) for how to use this feature.
- 🚥 Introducing [`st.toggle`](/develop/api-reference/widgets/st.toggle) — an alternative to `st.checkbox` when you need an on/off switch.

**Notable Changes**

- 🎨 Simple [chart elements](/develop/api-reference/charts) have a `color` parameter to set the color of your data points or series ([#7022](https://github.com/streamlit/streamlit/pull/7022)).
- 🌈 [Markdown](/develop/api-reference/text/st.markdown) supports rainbow and gray colors ([#7106](https://github.com/streamlit/streamlit/pull/7106), [#7179](https://github.com/streamlit/streamlit/pull/7179)).
- 📏 [`st.header`](/develop/api-reference/text/st.header) and [`st.subheader`](/develop/api-reference/text/st.subheader) have optional, colored dividers ([#7133](https://github.com/streamlit/streamlit/pull/7133)).
- 🚀 Deploying to Community Cloud is even easier—locally running apps have a [deploy button](/develop/concepts/architecture/app-chrome#deploy-this-app) in their toolbars ([#7085](https://github.com/streamlit/streamlit/pull/7085), [#6935](https://github.com/streamlit/streamlit/issues/6935)).
- 🖌️ [`st.download_button`](/develop/api-reference/widgets/st.download_button) has a new parameter `type` for theming ([#7056](https://github.com/streamlit/streamlit/pull/7056), [#7038](https://github.com/streamlit/streamlit/issues/7038)).
- 🤖 [`st.chat_message`](/develop/api-reference/chat/st.chat_message) has ai and human presets for messages ([#7094](https://github.com/streamlit/streamlit/pull/7094)).
- 💅 [`st.radio`](/develop/api-reference/widgets/st.radio) options support markdown and have captions ([#7018](https://github.com/streamlit/streamlit/pull/7018), [#7105](https://github.com/streamlit/streamlit/pull/7105), [#6085](https://github.com/streamlit/streamlit/issues/6085)).
- 🧼 Assorted visual tweaks ([#7050](https://github.com/streamlit/streamlit/pull/7050), [#894](https://github.com/streamlit/streamlit/issues/894)).
- 🛏️ Replaced deprecated `imghdr` dependency with `pillow` ([#7081](https://github.com/streamlit/streamlit/pull/7081), [#7027](https://github.com/streamlit/streamlit/issues/7027)).
- 🔢 [`st.number_input`](/develop/api-reference/widgets/st.number_input)'s step buttons (+/-) are ignored during tabbing navigation ([#7154](https://github.com/streamlit/streamlit/pull/7154)). Thanks [@denck007](https://github.com/denck007)!

**Other Changes**

- 🍞 Bug fix: Toast messages are no longer blocked by `st.chat_input` ([#7204](https://github.com/streamlit/streamlit/pull/7204), [#7115](https://github.com/streamlit/streamlit/issues/7115)).
- 🕸️ Bug fix: Widget IDs are now stable to prevent inconsistent statefulness ([#7003](https://github.com/streamlit/streamlit/pull/7003)).
- 🦟 Bug fix: Browser autofill is correctly recognized within forms now ([#7150](https://github.com/streamlit/streamlit/pull/7150), [#7101](https://github.com/streamlit/streamlit/issues/7101), [#7084](https://github.com/streamlit/streamlit/issues/7084)).
- 🪱 Bug fix: `st.file_uploader` no longer causes session state to reset when a websocket connection is dropped and reconnected ([#7149](https://github.com/streamlit/streamlit/pull/7149), [#7025](https://github.com/streamlit/streamlit/pull/7025)).
- 🏎️ Bug fix: Pydeck JSON data is cached for improved performance ([#7113](https://github.com/streamlit/streamlit/pull/7113), [#5532](https://github.com/streamlit/streamlit/issues/5532)).
- 🦋 Bug fix: `st.chat_input` no longer submits prematurely while typing with an input method editor ([#6993](https://github.com/streamlit/streamlit/pull/6993)).
- 🐞 Bug fix: Label backgrounds for `st.tabs` are now transparent ([#7070](https://github.com/streamlit/streamlit/pull/7070), [#5707](https://github.com/streamlit/streamlit/issues/5707)).
- 🐝 Bug fix: Page width is no longer ignored when using the `help` parameter in `st.button` ([#7033](https://github.com/streamlit/streamlit/pull/7033), [#6161](https://github.com/streamlit/streamlit/issues/6161)).
- 🐜 Bug fix: Tweaked Altair color specification for improved visibility in dark mode ([#7061](https://github.com/streamlit/streamlit/pull/7061), [#3343](https://github.com/streamlit/streamlit/issues/3343)).
- 🪲 Bug fix: `st.chat_message` can correctly use local images as avatars ([#7130](https://github.com/streamlit/streamlit/pull/7130)).
- 🐛 Bug fix: Specified that MD5 is not used for security ([#7122](https://github.com/streamlit/streamlit/pull/7122), [#7120](https://github.com/streamlit/streamlit/issues/7120)).
- 🪄 Bug fix: Async function docstrings are ignored by [Streamlit magic](/develop/api-reference/write-magic/magic) ([#7143](https://github.com/streamlit/streamlit/pull/7143), [#7137](https://github.com/streamlit/streamlit/issues/7137)).

## **Version 1.25.0**

_Release date: July 20, 2023_

**Highlights**

- 🍞 Introducing `st.toast` — a command to briefly show toast messages to users in the bottom-right corner of apps. See [our documentation](/develop/api-reference/status/st.toast) on how to use this feature.

**Notable Changes**

- 🗺️ [`st.map`](/develop/api-reference/charts/st.map) now has parameters for `latitude`, `longitude`, `color`, and `size` to customize data points ([#6896](https://github.com/streamlit/streamlit/pull/6896)).
- 🚩 [`st.multiselect`](/develop/api-reference/widgets/st.multiselect) supports setting placeholders and specifying the maximum number of selections via the `placeholder` and `max_selections` keyword-only arguments, respectively ([#6901](https://github.com/streamlit/streamlit/pull/6901), [#4750](https://github.com/streamlit/streamlit/issues/4750)). Thanks, [@fhiroki](https://github.com/fhiroki)!
- 📅 Customize the date format for `st.date_input` with the `format` parameter ([#6974](https://github.com/streamlit/streamlit/pull/6974), [#5234](https://github.com/streamlit/streamlit/issues/5234)).
- ↩️ [Forms](/develop/api-reference/execution-flow/st.form) can now be submitted with Enter/Return while inside [`st.text_input`](/develop/api-reference/widgets/st.text_input), [`st.number_input`](/develop/api-reference/widgets/st.number_input), or [`st.text_area`](/develop/api-reference/widgets/st.text_area) ([#6911](https://github.com/streamlit/streamlit/pull/6911), [#3790](https://github.com/streamlit/streamlit/issues/3790)).
- 🍢 The app menu icon in the upper-right corner of apps has been changed from "**☰**" to "**⋮**" ([#6947](https://github.com/streamlit/streamlit/pull/6947)).

**Other Changes**

- ⛓️ Minimum required versions increased for multiple Python dependencies, including `numpy&gt;=1.19.3` and `pandas&gt;=1.3.0` ([#6802](https://github.com/streamlit/streamlit/pull/6802)).
- 🛡️ `protobufjs` was bumped from 7.2.1 to 7.2.4 ([#6959](https://github.com/streamlit/streamlit/pull/6959)).
- ✨ Visual design tweaks to Streamlit's input widgets ([#6944](https://github.com/streamlit/streamlit/pull/6944)).
- 🦋 Bug Fix: `st.slider` now accepts general number types like `numpy.int64` instead of just `int` and `float` ([#6816](https://github.com/streamlit/streamlit/pull/6816), [#6815](https://github.com/streamlit/streamlit/issues/6815)). Thanks, [@milliams](https://github.com/milliams)!
- 🐜 Bug Fix: Data labels for `st.slider` and `st.select_slider` no longer overflow when inside `st.expander` ([#6828](https://github.com/streamlit/streamlit/pull/6828), [#6297](https://github.com/streamlit/streamlit/issues/6297)).
- 🐛 Bug Fix: Elements no longer re-render from scratch with each rerun ([#6923](https://github.com/streamlit/streamlit/pull/6923), [#6920](https://github.com/streamlit/streamlit/issues/6920)).
- 🐞 Bug Fix: `st.data_editor` hashes styler objects correctly for stability across reruns ([#6815](https://github.com/streamlit/streamlit/pull/6915), [#6898](https://github.com/streamlit/streamlit/issues/6898)).
- 🐝 Bug Fix: Fixed the padding for embedded apps using `st.chat_input` to prevent messages being cutoff ([#6979](https://github.com/streamlit/streamlit/pull/6979)).

## **Version 1.24.0**

_Release date: June 27, 2023_

**Highlights**

- 💬 Introducing `st.chat_message` and `st.chat_input` — two new [chat elements](/develop/api-reference/chat) that let you build conversational apps. Learn how to use these features in your LLM-powered chat apps in our [tutorial](/develop/tutorials/llms/build-conversational-apps).
- 💾 Streamlit's caching decorators now allow you to customize Streamlit's hashing of input parameters with the keyword-only argument [`hash_funcs`](/develop/concepts/architecture/caching#the-hash_funcs-parameter).

**Notable Changes**

- 🐍 We've deprecated support for Python 3.7 in the core library and Streamlit Community Cloud ([#6868](https://github.com/streamlit/streamlit/pull/6868)).
- 📅 `st.cache_data` and `st.cache_resource` can hash timezone-aware `datetime` objects ([#6812](https://github.com/streamlit/streamlit/pull/6812), [#6690](https://github.com/streamlit/streamlit/issues/6690), [#5110](https://github.com/streamlit/streamlit/issues/5110)).

**Other Changes**

- ✨ Visual design tweaks to Streamlit's input widgets ([#6817](https://github.com/streamlit/streamlit/pull/6817)).
- 🐛 Bug fix: `st.write` pretty-prints dataclasses using `st.help` ([#6750](https://github.com/streamlit/streamlit/pull/6750)).
- 🪲 Bug fix: `st.button`'s height is consistent with that of other widgets ([#6738](https://github.com/streamlit/streamlit/pull/6738)).
- 🐜 Bug fix: Upgraded the `react-range` frontend dependency to fix the memory usage of sliders ([#6764](https://github.com/streamlit/streamlit/pull/6764), [#5436](https://github.com/streamlit/streamlit/issues/5436)). Thanks [@wolfd](https://github.com/wolfd)!
- 🐝 Bug fix: Pydantic validators no longer result in exceptions on app reruns ([#6664](https://github.com/streamlit/streamlit/pull/6664), [#3218](https://github.com/streamlit/streamlit/issues/3218)).
- 🐞 Bug fix: `streamlit config show` honors newlines ([#6758](https://github.com/streamlit/streamlit/pull/6758), [#2868](https://github.com/streamlit/streamlit/issues/2868)).
- 🪰 Bug fix: Fixed a race condition to ensure Streamlit reruns the latest code when the file changes ([#6884](https://github.com/streamlit/streamlit/pull/6884)).
- 🦋 Bug fix: Apps no longer rerun when users click anchor links ([#6834](https://github.com/streamlit/streamlit/pull/6834), [#6500](https://github.com/streamlit/streamlit/issues/6500)).
- 🕸️ Bug fix: Added robust out-of-bounds checks for `min_value` and `max_value` in `st.number_input` ([#6847](https://github.com/streamlit/streamlit/pull/6847), [#6797](https://github.com/streamlit/streamlit/issues/6797)).

## **Version 1.23.0**

_Release date: June 1, 2023_

**Highlights**

- ✂️ Announcing the general availability of [st.data_editor](/develop/api-reference/data/st.data_editor), a widget that allows you to edit DataFrames and many other data structures in a table-like UI. **Breaking change:** the data editor's representation used in `st.session_state` was altered. Find out more about the new format in [Access edited data](/develop/concepts/design/dataframes#access-edited-data).
- ⚙️ Introducing the [Column configuration API](/develop/api-reference/data/st.column_config) with a suite of methods to configure the display and editing behavior of `st.dataframe` and `st.data_editor` columns (e.g. their title, visibility, type, or format). Keep an eye out for a detailed [blog post](https://blog.streamlit.io/) and in-depth [documentation](/develop/concepts/design/dataframes#configuring-columns) upcoming in the next two weeks.
- 🔌 Learn to use `st.experimental_connection` to create and manage data connections in your apps with the new [Connecting to data](/develop/concepts/connections/connecting-to-data) docs and [video tutorial](https://www.youtube.com/watch?v=xQwDfW7UHMo).

**Notable Changes**

- 📊 Streamlit now supports Protobuf 4 and Altair 5 ([#6215](https://github.com/streamlit/streamlit/issues/6215), [#6618](https://github.com/streamlit/streamlit/pull/6618), [#5626](https://github.com/streamlit/streamlit/issues/5626), [#6622](https://github.com/streamlit/streamlit/pull/6622)).
- ☎️ st.dataframe and st.data_editor can hide index columns with `hide_index`, specify the display order of columns with `column_order`, and disable editing for individual columns with the `disabled` parameter.
- ⏱️ The `ttl` parameter in [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data) and [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource) accepts formatted strings, so you can simply say `ttl="30d"`, `ttl="1h30m"` and any other combination of `w`, `d`, `h`, `m`, `s` supported by [Pandas's Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html) ([#6560](https://github.com/streamlit/streamlit/pull/6560)).
- 📂 `st.file_uploader` now interprets the `type` parameter more accurately. For example, "jpg" or ".jpg" now accept both "jpg" and "jpeg" extensions. This functionality has also been extended to "mpeg/mpg", "tiff/tif", "html/htm", and "mpeg4/mp4".
- 🤫 The new `global.disableWidgetStateDuplicationWarning` configuration option allows the silencing of warnings triggered by setting widget default values and keyed session state values concurrently ([#3605](https://github.com/streamlit/streamlit/issues/3605), [#6640](https://github.com/streamlit/streamlit/pull/6640)). Thanks, [@antonAce](https://github.com/antonAce)!

**Other Changes**

- 🏃‍♀️Improved startup time by lazy loading some dependencies ([#6531](https://github.com/streamlit/streamlit/pull/6531)).
- 👋 Removed `st.beta_*` and `st.experimental_show` due to deprecation and low-use ([#6558](https://github.com/streamlit/streamlit/pull/6558))
- 🚀 Further improvements to st.dataframe and st.data_editor:
  - Improved editing on mobile devices for the data editor ([#6548](https://github.com/streamlit/streamlit/pull/6548)).
  - All editable columns have an icon in their column header and support tooltips ([#6550](https://github.com/streamlit/streamlit/pull/6550), [#6561](https://github.com/streamlit/streamlit/pull/6561)).
  - Enable editing for columns containing datetime, date, or time values ([#6025](https://github.com/streamlit/streamlit/pull/6025)).
  - New input validation options for columns in the data editor, such as `max_chars` and `validate` for text columns, and `min_value`, `max_value` and `step` for number columns ([#6563](https://github.com/streamlit/streamlit/pull/6563)).
  - Improved type parsing capabilities in the data editor ([#6551](https://github.com/streamlit/streamlit/pull/6551)).
  - Unified missing values to `None` in returned data structures ([#6544](https://github.com/streamlit/streamlit/pull/6544)).
  - A warning is shown in cells when integers exceed the maximum safe value of `(2^53) -1` ([#6311](https://github.com/streamlit/streamlit/issues/6311), [#6549](https://github.com/streamlit/streamlit/pull/6549)).
  - Prevented editing the sessions state by showing a warning ([#6634](https://github.com/streamlit/streamlit/pull/6634)).
  - Fixed issues with list columns sometimes breaking the frontend ([#6644](https://github.com/streamlit/streamlit/pull/6644)).
  - Fixed a display issue with index columns using category dtype ([#6680](https://github.com/streamlit/streamlit/issues/6680), [#6598](https://github.com/streamlit/streamlit/pull/6598)).
  - Fixed an issue that prevented a rerun when adding empty rows ([#6598](https://github.com/streamlit/streamlit/pull/6598)).
  - Unified the behavior between `st.data_editor` and `st.dataframe` related to auto-hiding the index column(s) based on the input data ([#6659](https://github.com/streamlit/streamlit/issues/6659), [#6598](https://github.com/streamlit/streamlit/pull/6598))
- 🛡️ Streamlit's [Security Policy](https://github.com/streamlit/streamlit/blob/develop/SECURITY.md) can be found in its GitHub repository ([#6666](https://github.com/streamlit/streamlit/pull/6666)).
- 🤏 Documented the integer size limit for `st.number_input` and `st.slider` ([#6724](https://github.com/streamlit/streamlit/pull/6724)).
- 🐍 The majority of Streamlit's Python dependencies have set a maximum allowable version, with the standard upper limit set to the next major version, but not inclusive of it ([#6691](https://github.com/streamlit/streamlit/pull/6691)).
- 💅 UI design improvements to in-app modals ([#6688](https://github.com/streamlit/streamlit/pull/6688)).
- 🐞 Bug fix: `st.date_input`'s date selector is equally visible in dark mode ([#6072](https://github.com/streamlit/streamlit/issues/6072), [#6630](https://github.com/streamlit/streamlit/pull/6630)).
- 🐜 Bug fix: the sidebar navigation expansion indicator in multipage apps is restored ([#6731](https://github.com/streamlit/streamlit/pull/6731)).
- 🐛 Bug fix: The docstring and exception message for `st.set_page_config` have been updated to clarify that this command can be invoked once for each page within a multipage app, rather than once per entire app ([#6594](https://github.com/streamlit/streamlit/pull/6594)).
- 🐝 Bug fix: `st.json` no longer collapses multiple spaces in both keys and values with single space when rendered ([#6657](https://github.com/streamlit/streamlit/issues/6657), [#6663](https://github.com/streamlit/streamlit/pull/6663)).

## **Version 1.22.0**

_Release date: April 27, 2023_

**Highlights**

- 🔌 Introducing `st.experimental_connection`: Easily connect your app to data sources and APIs using our new connection feature. Find more details in the [API reference](/develop/api-reference/connections), and stay tuned for an upcoming blog post and in-depth documentation! In the meantime, explore our updated [MySQL](/develop/tutorials/databases/mysql) and [Snowflake](/develop/tutorials/databases/snowflake) connection tutorials for examples of this feature.

**Notable Changes**

- 🐼 Streamlit now supports Pandas 2.0 ([#6413](https://github.com/streamlit/streamlit/issues/6413), [#6378](https://github.com/streamlit/streamlit/pull/6378), [#6507](https://github.com/streamlit/streamlit/pull/6507)). Thanks, [connortann](https://github.com/connortann)!
- 🍔 Customize the visibility of items in the toolbar, options menu, and the settings dialog using the `client.toolbarMode` [config option](https://docs.streamlit.io/develop/concepts/configuration#view-all-configuration-options) ([#6174](https://github.com/streamlit/streamlit/pull/6174)).
- 🪵 Streamlit logs now reside in the "streamlit" namespace instead of the root logger, enabling app developers to better manage log handling ([#3978](https://github.com/streamlit/streamlit/issues/3978), [#6377](https://github.com/streamlit/streamlit/pull/6377)).

**Other Changes**

- 🔏 CLI parameters can no longer be used to set sensitive configuration values ([#6376](https://github.com/streamlit/streamlit/pull/6376)).
- 🤖 Improved the debugging experience by reducing log noise ([#6391](https://github.com/streamlit/streamlit/pull/6391)).
- 🐞 Bug fix: `@st.cache_data` decorated functions support UUID objects as parameters ([#6440](https://github.com/streamlit/streamlit/issues/6440), [#6459](https://github.com/streamlit/streamlit/pull/6459)).
- 🐛 Bug fix: Tabbing through buttons and other elements now displays a red border only when focused, not when clicked ([#6373](https://github.com/streamlit/streamlit/pull/6373)).
- 🪲 Bug fix: `st.multiselect`'s clear icon is larger and includes a hover effect ([#6471](https://github.com/streamlit/streamlit/pull/6471)).
- 🐜 Bug fix: Custom theme font settings no longer apply to code blocks ([#6484](https://github.com/streamlit/streamlit/issues/6484), [#6535](https://github.com/streamlit/streamlit/pull/6535)).
- ©️ Bug fix: `st.code`'s copy-to-clipboard button appears when you hover on code blocks ([#6490](https://github.com/streamlit/streamlit/issues/6490), [#6498](https://github.com/streamlit/streamlit/pull/6498)).

## **Version 1.21.0**

_Release date: April 6, 2023_

**Highlights**

- 📏 Introducing `st.divider` — a command that displays a horizontal line in your app. Learn how to use this command in its [API reference](/develop/api-reference/text/st.divider).
- 🔏 Streamlit now supports the use of a global `secrets.toml` file, in addition to a project-level file, to easily store and securely access your secrets. Learn more in [Secrets management](/develop/concepts/connections/secrets-management).
- 🚀 [st.help](/develop/api-reference/utilities/st.help) has been revamped to show more information about object methods, attributes, classes, and more, which is great for debugging ([#5857](https://github.com/streamlit/streamlit/pull/5857), [#6382](https://github.com/streamlit/streamlit/pull/6382))!

**Notable Changes**

- 🪜 [st.time_input](/develop/api-reference/widgets/st.time_input) supports adding a stepping interval with the keyword-only `step` parameter ([#6071](https://github.com/streamlit/streamlit/pull/6071)).
- ❓ Most [text elements](/develop/api-reference/text) can include tooltips with the `help` parameter ([#6043](https://github.com/streamlit/streamlit/pull/6043)).
- ↔️ [st.pyplot](/develop/api-reference/charts/st.pyplot) has a `use_container_width` parameter to set the chart to the container width (now all [chart elements](/develop/api-reference/charts) support this parameter) ([#6067](https://github.com/streamlit/streamlit/pull/6067)).
- 👩‍💻 [st.code](/develop/api-reference/text/st.code) supports optionally displaying line numbers to the code block's left with the boolean `line_numbers` parameter ([#5756](https://github.com/streamlit/streamlit/issues/5756), [#6042](https://github.com/streamlit/streamlit/pull/6042)).
- ⚓ Anchors in header elements can be turned off by setting `anchor=False` ([#6158](https://github.com/streamlit/streamlit/pull/6158)).

**Other Changes**

- 🐼 [st.table](/develop/api-reference/data/st.table) and [st.dataframe](/develop/api-reference/data/st.dataframe) support `pandas.Period`, and number and boolean types in categorical columns ([#2547](https://github.com/streamlit/streamlit/issues/2547), [#5429](https://github.com/streamlit/streamlit/pull/5429), [#5329](https://github.com/streamlit/streamlit/issues/5392), [#6248](https://github.com/streamlit/streamlit/pull/6248)).
- 🕸️ Added `.webp` to the list of allowed static file extensions ([#6331](https://github.com/streamlit/streamlit/pull/6331))
- 🐞 Bug fix: stop script execution on websocket close to immediately clear session information ([#6166](https://github.com/streamlit/streamlit/issues/6166), [#6204](https://github.com/streamlit/streamlit/pull/6204)).
- 🐜 Bug fixes: updated allowed/disallowed label markdown behavior such that unsupported elements are unwrapped and only their children (text contents) render ([#5872](https://github.com/streamlit/streamlit/issues/5872), [#6036](https://github.com/streamlit/streamlit/issues/6036), [#6054](https://github.com/streamlit/streamlit/issues/6054), [#6163](https://github.com/streamlit/streamlit/pull/6163)).
- 🪲 Bug fixes: don't push browser history states on rerun, use HTTPS to load external resources in `streamlit hello`, and make the browser back button work for multipage apps ([#5292](https://github.com/streamlit/streamlit/issues/5292), [#6266](https://github.com/streamlit/streamlit/pull/6266), [#6232](https://github.com/streamlit/streamlit/pull/6232)). Thanks, [whitphx](https://github.com/whitphx)!
- 🐝 Bug fix: avoid showing emoji on non-UTF-8 terminals. ([#2284](https://github.com/streamlit/streamlit/issues/2284), [#6088](https://github.com/streamlit/streamlit/pull/6088)). Thanks, [kcarnold](https://github.com/kcarnold)!
- 📁 Bug fix: override default use of [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API) for `react-dropzone` so that `st.file_uploader`'s File Selection Dialog only shows file types corresponding to those included in the `type` parameter ([#6176](https://github.com/streamlit/streamlit/issues/6176), [#6315](https://github.com/streamlit/streamlit/pull/6315)).
- 💾 Bug fix: make the `.clear()` method on cache-decorated functions work ([#6310](https://github.com/streamlit/streamlit/issues/6310), [#6321](https://github.com/streamlit/streamlit/pull/6321)).
- 🏃 Bug fix: `st.experimental_get_query_params` doesn't need reruns to work ([#6347](https://github.com/streamlit/streamlit/issues/6347), [#6348](https://github.com/streamlit/streamlit/pull/6348)). Thanks, [PaleNeutron](https://github.com/PaleNeutron)!
- 🐛 Bug fix: `CachedStFunctionWarning` mentions `experimental_allow_widgets` instead of the deprecated `suppress_st_warning` ([#6216](https://github.com/streamlit/streamlit/issues/6216), [#6217](https://github.com/streamlit/streamlit/pull/6217)).

## **Version 1.20.0**

_Release date: March 09, 2023_

**Notable Changes**

- 🔐 Added support for configuring SSL to [serve apps directly over HTTPS](/develop/concepts/configuration/https-support) ([#5969](https://github.com/streamlit/streamlit/pull/5969)).
- 🖼️ Granular control over app embedding behavior with the `/?embed` and `/?embed_options` query parameters. Learn how to use this feature in our [docs](/deploy/streamlit-community-cloud/share-your-app/embed-your-app) ([#6011](https://github.com/streamlit/streamlit/pull/6011), [#6019](https://github.com/streamlit/streamlit/pull/6019)).
- ⚡ Enabled the `runner.fastReruns` [configuration option](/develop/concepts/configuration#view-all-configuration-options) by default to make apps much more responsive to user interaction ([#6200](https://github.com/streamlit/streamlit/pull/6200)).

**Other Changes**

- 🍔 Cleaned up the hamburger menu by removing the least used options ([#6080](https://github.com/streamlit/streamlit/pull/6080)).
- 🖨️ Design changes to ensure apps being printed or saved as a PDF look good ([#6180](https://github.com/streamlit/streamlit/pull/6180)).
- 🐞 Bug fix: improved `dtypes` checking in `st.experimental_data_editor` ([#6185](https://github.com/streamlit/streamlit/issues/6185), [#6188](https://github.com/streamlit/streamlit/pull/6188)).
- 🐛 Bug fix: properly position `st.metric`'s `help` tooltip when not inside columns ([#6168](https://github.com/streamlit/streamlit/pull/6168)).
- 🪲 Bug fix: regression in retrieving messages from the server's `ForwardMsgCache` ([#6210](https://github.com/streamlit/streamlit/pull/6210)).
- 🌀 Bug fix: `st.cache_data` docstring for the `show_spinner` param now lists `str` as a supported type ([#6207](https://github.com/streamlit/streamlit/issues/6207), [#6213](https://github.com/streamlit/streamlit/pull/6213)).
- ⏱️ Made ping and websocket timeouts far more forgiving ([#6212](https://github.com/streamlit/streamlit/pull/6212)).
- 🗺️ `st.map` and `st.pydeck_chart` docs state that Streamlit's Mapbox token will not work indefinitely ([#6143](https://github.com/streamlit/streamlit/pull/6143)).

## **Version 1.19.0**

_Release date: February 23, 2023_

**Highlights**

- ✂️ Introducing `st.experimental_data_editor`, a widget that allows you to edit DataFrames and many other data structures in a table-like UI. Read more in our [documentation](/develop/concepts/design/dataframes) and [blog post](https://blog.streamlit.io/editable-dataframes-are-here/).

**Other Changes**

- ✨ Streamlit's GitHub README got a new look ([#6016](https://github.com/streamlit/streamlit/pull/6016)).
- 🌚 Improved readability of styled dataframe cells in dark mode ([#6060](https://github.com/streamlit/streamlit/issues/6060), [#6098](https://github.com/streamlit/streamlit/pull/6098)).
- 🐛 Bug fix: make apps work again in the latest versions of Safari, and in Chrome with third-party cookies blocked ([#6092](https://github.com/streamlit/streamlit/issues/6092), [#6094](https://github.com/streamlit/streamlit/pull/6094), [#6087](https://github.com/streamlit/streamlit/issues/6087), [#6100](https://github.com/streamlit/streamlit/pull/6100)).
- 🐞 Bug fix: refer to new cache primitives in the "Clear cache" dialog and error messages ([#6082](https://github.com/streamlit/streamlit/pull/6082), [#6128](https://github.com/streamlit/streamlit/pull/6128)).
- 🐝 Bug fix: properly cache class member functions and instance methods ([#6109](https://github.com/streamlit/streamlit/issues/6109), [#6114](https://github.com/streamlit/streamlit/pull/6114)).
- 🐜 Bug fix: regression in `st.metric` tooltip position ([#6093](https://github.com/streamlit/streamlit/issues/6093), [#6129](https://github.com/streamlit/streamlit/pull/6129)).
- 🪲 Bug fix: allow fullscreen button to show for dataframes, charts, etc, in expander ([#6083](https://github.com/streamlit/streamlit/pull/6083), [#6148](https://github.com/streamlit/streamlit/pull/6148)).

## **Version 1.18.0**

_Release date: February 09, 2023_

**Highlights**

- 🎊 Introducing `@st.cache_data` and `@st.cache_resource` — two new caching commands to replace `st.cache`! Check out our [blog post](https://blog.streamlit.io/p/c0a90231-9848-47ec-a40c-ad4a344e4de1/) and [documentation](/develop/concepts/architecture/caching) for more information.

**Notable Changes**

- 🪆 `st.columns` supports up to one level of column nesting (i.e., columns inside columns) in the main area of the app.
- ⏳ `st.progress` supports adding a message to display above the progress bar with the `text` keyword parameter.
- ↔️ `st.button` has an optional `use_container_width` parameter to allow you to stretch buttons across the full container width.
- 🐍 We formally added support for Python 3.11.
- 🖨️ Save your app as a PDF via the "Print" option in your app's hamburger menu.
- 🛎️ Apps can serve small, static media files via the `enableStaticServing` config option. See our [documentation](/develop/concepts/configuration/serving-static-files) on how to use this feature and our demo [app](https://static-file-serving.streamlit.app/) for an example.

**Other Changes**

- 🏁 All Streamlit endpoints (including `/healthz`) have been renamed to have a consistent pattern and avoid any clashes with reserved endpoints of GCP (notably Cloud Run and App Engine) ([#5534](https://github.com/streamlit/streamlit/pull/5534)).
- ⚡ Improved caching performance when multiple sessions access an uncomputed cached value simultaneously ([#6017](https://github.com/streamlit/streamlit/pull/6017)).
- 🚧 Streamlit only displays deprecation warnings in the browser when the `client.showErrorDetails` config option is set to `True`. Deprecation warnings always get logged to the console, regardless of whether they're displayed in-browser ([#5945](https://github.com/streamlit/streamlit/pull/5945)).
- 🏓 Refactored the `st.dataframe` internals to improve dataframe handling and conversion, such as detecting more types, converting key-value dicts to dataframes, and more ([#6026](https://github.com/streamlit/streamlit/pull/6026), [#6023](https://github.com/streamlit/streamlit/pull/6023)).
- 💽 The behavior of widget labels when they are passed unsupported Markdown elements is documented ([#5978](https://github.com/streamlit/streamlit/pull/5978)).
- 📊 Bug fix: Plotly improvements — upgraded multiple frontend dependencies, including Plotly, to the latest version to properly redraw cached charts, make Plotly mapbox animations work, and allow users to update the figure layout when using the Streamlit theme ([#5885](https://github.com/streamlit/streamlit/pull/5885), [#5967](https://github.com/streamlit/streamlit/pull/5967), [#6055](https://github.com/streamlit/streamlit/pull/6055)).
- 📶 Bug fix: allow browser tabs that transiently disconnect (due to a network blip, load balancer timeout, etc.) to avoid losing all of their state ([#5856](https://github.com/streamlit/streamlit/pull/5856)).
- 📱 Bug fix: the keyboard is hidden on mobile when `st.selectbox` and `st.multiselect` have less than 10 options ([#5979](https://github.com/streamlit/streamlit/pull/5979)).
- 🐝 Bug fix: design tweaks to `st.metric`, `st.multiselect`, `st.tabs` , and menu items to prevent label overflow and scrolling issues, especially with small viewport sizes ([#5933](https://github.com/streamlit/streamlit/pull/5933), [#6034](https://github.com/streamlit/streamlit/pull/6034)).
- 🐞 Bug fix: switched to a functioning Twemoji URL from which page favicons are loaded in `st.set_page_config` ([#5943](https://github.com/streamlit/streamlit/pull/5943)).
- ✍️ More type hints ([#5986](https://github.com/streamlit/streamlit/pull/5986)). Thanks, [harahu](https://github.com/harahu)!

## **Version 1.17.0**

_Release date: January 12, 2023_

**Notable Changes**

- 🪄 [`@st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton#validating-the-cache) supports an optional `validate` parameter that accepts a validation function for cached data and is called each time the cached value is accessed.
- 💾  [`@st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo)'s `persist` parameter can also accept booleans.

**Other Changes**

- 📟 Multipage apps exclude `__init__.py` from the page selector ([#5890](https://github.com/streamlit/streamlit/pull/5890)).
- 📐 The iframes of embedded apps have the ability to dynamically resize their height ([#5894](https://github.com/streamlit/streamlit/pull/5894)).
- 🐞 Bug fix: thumb values of range sliders respect the container width ([#5913](https://github.com/streamlit/streamlit/pull/5913)).
- 🪲 Bug fix: all examples in docstrings of Streamlit commands contain relevant imports to make them reproducible ([#5877](https://github.com/streamlit/streamlit/pull/5877)).

---

# 2022 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2022


This page contains release notes for Streamlit versions released in 2022. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## **Version 1.16.0**

_Release date: December 14, 2022_

**Highlights**

- 👩‍🎨 Introducing a new Streamlit theme for Altair, Plotly, and Vega-Lite charts! Check out our [blog post](https://blog.streamlit.io/a-new-streamlit-theme-for-altair-and-plotly/) for more information.
- 🎨 Streamlit now supports colored text in all commands that accept Markdown, including `st.markdown`, `st.header`, and more. Learn more in our [documentation](/develop/api-reference/text/st.markdown).

**Notable Changes**

- 🔁 Functions cached with `st.experimental_memo` or `st.experimental_singleton` can contain Streamlit media elements and forms.
- ⛄ All Streamlit commands that accept pandas DataFrames as input also support Snowpark and PySpark DataFrames.
- 🏷 [st.checkbox](/develop/api-reference/widgets/st.checkbox) and [st.metric](/develop/api-reference/data/st.metric) can customize how to hide their labels with the `label_visibility` parameter.

**Other Changes**

- 🗺️ `st.map` improvements: support for upper case columns and better exception messages ([#5679](https://github.com/streamlit/streamlit/pull/5679), [#5792](https://github.com/streamlit/streamlit/pull/5792)).
- 🐞 Bug fix: `st.plotly_chart` respects the figure's height attribute and the `use_container_width` parameter ([#5779](https://github.com/streamlit/streamlit/pull/5779)).
- 🪲 Bug fix: all commands with the `icon` parameter such as [st.error](/develop/api-reference/status/st.error), [st.warning](/develop/api-reference/status/st.warning), etc, can contain emojis with variant selectors ([#5583](https://github.com/streamlit/streamlit/pull/5583)).
- 🐝 Bug fix: prevent `st.camera_input` from jittering when resizing the browser window ([#5661](https://github.com/streamlit/streamlit/pull/5711)).
- 🐜 Bug fix: update exception layout to avoid overflow of stack traces ([#5700](https://github.com/streamlit/streamlit/pull/5700)).

## **Version 1.15.0**

_Release date: November 17, 2022_

**Notable Changes**

- 💅 Widget labels can contain inline Markdown. See our [docs](/develop/api-reference/widgets) and demo [app](https://markdown-labels.streamlit.app/) for more info.
- 🎵 [`st.audio`](/develop/api-reference/media/st.audio) now supports playing audio data passed in as NumPy arrays with the keyword-only `sample_rate` parameter.
- 🔁 Functions cached with `st.experimental_memo` or `st.experimental_singleton` can contain Streamlit widgets using the `experimental_allow_widgets` parameter. This allows caching checkboxes, sliders, radio buttons, and more!

**Other Changes**

- 👩‍🎨 Design tweak to prevent jittering in sliders ([#5612](https://github.com/streamlit/streamlit/pull/5612)).
- 🐛 Bug fix: links in headers are red, not blue ([#5609](https://github.com/streamlit/streamlit/pull/5609)).
- 🐞 Bug fix: properly resize Plotly charts when exiting fullscreen ([#5645](https://github.com/streamlit/streamlit/pull/5645)).
- 🐝: Bug fix: don't accidentally trigger `st.balloons` and `st.snow` ([#5401](https://github.com/streamlit/streamlit/pull/5401)).

## **Version 1.14.0**

_Release date: October 27, 2022_

**Highlights**

- 🎨 `st.button` and `st.form_submit_button` support designating buttons as "primary" (for additional emphasis) or "secondary" (for normal buttons) with the `type` keyword-only parameter.

**Notable Changes**

- 🤏 `st.multiselect` has a keyword-only `max_selections` parameter to limit the number of options that can be selected at a time.
- 📄 `st.form_submit_button` now has the `disabled` parameter that removes interactivity.

**Other Changes**

- 🏓 `st.dataframe` and `st.table` accept categorical intervals as input ([#5395](https://github.com/streamlit/streamlit/pull/5395)).
- ⚡ Performance improvements to Plotly charts ([#5542](https://github.com/streamlit/streamlit/pull/5542)).
- 🪲 Bug fix: `st.download_button` supports non-latin1 characters in filenames ([#5465](https://github.com/streamlit/streamlit/pull/5465)).
- 🐞 Bug fix: Allow `st.image` to render a local GIF as a GIF, not as a static PNG ([#5438](https://github.com/streamlit/streamlit/pull/5438)).
- 📱 Design tweaks to the sidebar in multipage apps ([#5538](https://github.com/streamlit/streamlit/pull/5538), [#5445](https://github.com/streamlit/streamlit/pull/5445), [#5559](https://github.com/streamlit/streamlit/pull/5559)).
- 📊 Improvements to the axis configuration for built-in charts ([#5412](https://github.com/streamlit/streamlit/pull/5412)).
- 🔧 Memo and singleton improvements: support text values for `show_spinner`, use `datetime.timedelta` objects as `ttl` parameter value, properly hash PIL images and `Enum` classes, show better error messages when returning unevaluated dataframes ([#5447](https://github.com/streamlit/streamlit/pull/5447), [#5413](https://github.com/streamlit/streamlit/pull/5413), [#5504](https://github.com/streamlit/streamlit/pull/5504), [#5426](https://github.com/streamlit/streamlit/pull/5426), [#5515](https://github.com/streamlit/streamlit/pull/5515)).
- 🔍 Zoom buttons in maps created with `st.map` and `st.pydeck_chart` use light or dark style based on the app's theme ([#5479](https://github.com/streamlit/streamlit/pull/5479)).
- 🗜 Websocket headers from the current session's incoming WebSocket request can be obtained from a new "internal" (i.e.: subject to change without deprecation) API ([#5457](https://github.com/streamlit/streamlit/pull/5457)).
- 📝 Improve the text that gets printed when you first install and use Streamlit ([#5473](https://github.com/streamlit/streamlit/pull/5473)).

## **Version 1.13.0**

_Release date: September 22, 2022_

**Notable Changes**

- 🏷 Widgets can customize how to hide their labels with the `label_visibility` parameter.
- 🔍 `st.map` adds zoom buttons to the map by default.
- ↔️ `st.dataframe` supports the `use_container_width` parameter to stretch across the full container width.
- 🪄 Improvements to `st.dataframe` sizing: Column width calculation respects column headers, supports double click between column headers to autosize, better fullscreen support, and fixes the issue with the `width` parameter.

**Other Changes**

- ⌨️ `st.time_input` allows for keyboard-only input ([#5194](https://github.com/streamlit/streamlit/pull/5194)).
- 💿 `st.memo` will warn the user when using `ttl` and `persist` keyword argument together ([#5032](https://github.com/streamlit/streamlit/pull/5032)).
- 🔢 `st.number_input` returns consistent type after rerun ([#5359](https://github.com/streamlit/streamlit/pull/5359)).
- 🚒 `st.sidebar` UI fixes including a fix for scrollbars in Firefox browsers ([#5157](https://github.com/streamlit/streamlit/pull/5157), [#5324](https://github.com/streamlit/streamlit/pull/5324)).
- 👩‍💻 Improvements to usage metrics to guide API development.
- ✍️ More type hints! ([#5191](https://github.com/streamlit/streamlit/pull/5191), [#5192](https://github.com/streamlit/streamlit/pull/5192), [#5242](https://github.com/streamlit/streamlit/pull/5242), [#5243](https://github.com/streamlit/streamlit/pull/5243), [#5244](https://github.com/streamlit/streamlit/pull/5244), [#5245](https://github.com/streamlit/streamlit/pull/5245), [#5246](https://github.com/streamlit/streamlit/pull/5246)) Thanks [harahu](https://github.com/harahu)!

## **Version 1.12.0**

_Release date: August 11, 2022_

**Highlights**

- 📊 Built-in charts (e.g. `st.line_chart`) get a brand-new look and parameters `x` and `y`! Check out our [blog post](https://blog.streamlit.io/built-in-charts-get-a-new-look-and-parameters/) for more information.

**Notable Changes**

- ⏯ Functions cached with `st.experimental_memo` or `st.experimental_singleton` can now contain static `st` commands. This allows caching text, charts, dataframes, and more!
- ↔️ The sidebar is now resizable via drag and drop.
- ☎️ `st.info`, `st.success`, `st.error`, and `st.warning` got a redesign and have a new keyword-only parameter: `icon`.

**Other Changes**

- 🎚️ `st.select_slider` correctly handles all floats now ([#4973](https://github.com/streamlit/streamlit/pull/4973), [#4978](https://github.com/streamlit/streamlit/pull/4978)).
- 🔢 `st.multi_select` can take values from enums ([#4987](https://github.com/streamlit/streamlit/pull/4987)).
- 🍊 `st.slider` range values can now be set through `st.session_state` ([#5007](https://github.com/streamlit/streamlit/pull/5007)).
- 🎨 `st.progress` got a redesign ([#5011](https://github.com/streamlit/streamlit/pull/5011), [#5086](https://github.com/streamlit/streamlit/pull/5086)).
- 🔘 `st.radio` better deals with list-like dataframes ([#5021](https://github.com/streamlit/streamlit/pull/5021)).
- 🧞‍♂️ `st.cache` properly handles JSON files now ([#5023](https://github.com/streamlit/streamlit/pull/5023)).
- ⚓️ Headers render markdown now when the `anchor` parameter is set ([#5038](https://github.com/streamlit/streamlit/pull/5038)).
- 🗻 `st.image` can now load SVGs from Inkscape ([#5040](https://github.com/streamlit/streamlit/pull/5040)).
- 🗺️ `st.map` and `st.pydeck_chart` use light or dark style based on the app's theme ([#5074](https://github.com/streamlit/streamlit/pull/5074), [#5108](https://github.com/streamlit/streamlit/pull/5108)).
- 🎈 Clicks on elements below `st.balloons` and `st.snow` don't get blocked anymore ([#5098](https://github.com/streamlit/streamlit/pull/5098)).
- 🔝 Embedded apps have lower top padding ([#5111](https://github.com/streamlit/streamlit/pull/5111)).
- 💅 Adjusted padding and alignment for widgets, charts, and dataframes ([#4995](https://github.com/streamlit/streamlit/pull/4995), [#5061](https://github.com/streamlit/streamlit/pull/5061), [#5081](https://github.com/streamlit/streamlit/pull/5081)).
- ✍️ More type hints! ([#4926](https://github.com/streamlit/streamlit/pull/4926), [#4932](https://github.com/streamlit/streamlit/pull/4932), [#4933](https://github.com/streamlit/streamlit/pull/4933))

## **Version 1.11.0**

_Release date: July 14, 2022_

**Highlights**

- 🗂 Introducing `st.tabs` to have tab containers in your app. See our [documentation](/develop/api-reference/layout/st.tabs) on how to use this feature.

**Notable Changes**

- ℹ️ `st.metric` supports tooltips with the `help` keyword parameter.
- 🚇 `st.columns` supports setting the gap size between columns with the `gap` keyword parameter.

**Other Changes**

- 💅 Design tweaks to `st.selectbox`, `st.expander`, `st.spinner` ([#4801](https://github.com/streamlit/streamlit/pull/4801)).
- 📱 The sidebar will close when users select a page from the navigation menu on mobile devices ([#4851](https://github.com/streamlit/streamlit/pull/4841)).
- 🧠 `st.memo` supports dataclasses! ([#4850](https://github.com/streamlit/streamlit/pull/4850))
- 🏎 Bug fix for a race condition that destroyed widget state with rapid interaction ([#4882](https://github.com/streamlit/streamlit/pull/4882)).
- 🏓 `st.table` presents overflowing content to be scrollable when placed inside columns and expanders ([#4934](https://github.com/streamlit/streamlit/pull/4934)).
- 🐍 Types: More updated type annotations across Streamlit! ([#4808](https://github.com/streamlit/streamlit/pull/4808), [#4809](https://github.com/streamlit/streamlit/pull/4809), [#4856](https://github.com/streamlit/streamlit/pull/4856))

## **Version 1.10.0**

_Release date: June 2, 2022_

**Highlights**

- 📖 Introducing native support for multipage apps! Check out our [blog post](https://blog.streamlit.io/introducing-multipage-apps) and try out our new `streamlit hello`.

**Notable Changes**

- ✨ `st.dataframe` has been redesigned.
- 🔘 `st.radio` has a `horizontal` keyword-only parameter to display options horizontally.
- ⚠️ Streamlit Community Cloud will support richer exception formatting.
- 🏂 Get user information on private apps using `st.experimental_user`.

**Other Changes**

- 📊 Upgraded Vega-Lite library to support even more interactive charting improvements. See their [release notes](https://github.com/vega/vega-lite/releases) to find out more. ([#4751](https://github.com/streamlit/streamlit/pull/4751)).
- 📈 `st.vega_lite_chart` will respond to updates, particularly in response to input widgets ([#4736](https://github.com/streamlit/streamlit/pull/4736)).
- 💬 `st.markdown` with long text will always wrap ([#4696](https://github.com/streamlit/streamlit/pull/4696)).
- 📦 Support for [PDM](https://pdm.fming.dev/) ([#4724](https://github.com/streamlit/streamlit/pull/4724)).
- ✍️ Types: Updated type annotations across Streamlit! ([#4679](https://github.com/streamlit/streamlit/pull/4679), [#4680](https://github.com/streamlit/streamlit/pull/4680), [#4681](https://github.com/streamlit/streamlit/pull/4681), [#4682](https://github.com/streamlit/streamlit/pull/4682), [#4683](https://github.com/streamlit/streamlit/pull/4683), [#4684](https://github.com/streamlit/streamlit/pull/4684), [#4685](https://github.com/streamlit/streamlit/pull/4685), [#4686](https://github.com/streamlit/streamlit/pull/4686), [#4687](https://github.com/streamlit/streamlit/pull/4687), [#4688](https://github.com/streamlit/streamlit/pull/4688), [#4690](https://github.com/streamlit/streamlit/pull/4690), [#4703](https://github.com/streamlit/streamlit/pull/4703), [#4704](https://github.com/streamlit/streamlit/pull/4704), [#4705](https://github.com/streamlit/streamlit/pull/4705), [#4706](https://github.com/streamlit/streamlit/pull/4706), [#4707](https://github.com/streamlit/streamlit/pull/4707), [#4708](https://github.com/streamlit/streamlit/pull/4708), [#4710](https://github.com/streamlit/streamlit/pull/4710), [#4723](https://github.com/streamlit/streamlit/pull/4723), [#4733](https://github.com/streamlit/streamlit/pull/4733)).

## **Version 1.9.0**

_Release date: May 4, 2022_

**Notable Changes**

- 🪗 `st.json` now supports a keyword-only argument, `expanded` on whether the JSON should be expanded by default (defaults to `True`).
- 🏃‍♀️ More performance improvements from reducing redundant work each script run.

**Other Changes**

- 🏇 Widgets when `disabled` is set/unset will maintain its value ([#4527](https://github.com/streamlit/streamlit/pull/4527)).
- 🧪 Experimental feature to increase the speed of reruns using configuration `runner.fastReruns`. See [#4628](https://github.com/streamlit/streamlit/pull/4628) for the known issues in enabling this feature.
- 🗺️ DataFrame timestamps support UTC offset (in addition to time zone notation) ([#4669](https://github.com/streamlit/streamlit/pull/4669)).

## **Version 1.8.0**

_Release date: March 24, 2022_

**Notable Changes**

- 🏃‍♀️ Dataframes should see performance improvements ([#4463](https://github.com/streamlit/streamlit/pull/4463)).

**Other Changes**

- 🕰 `st.slider` handles timezones better by removing timezone conversions on the backend ([#4348](https://github.com/streamlit/streamlit/pull/4358)).
- 👩‍🎨 Design improvements to our header ([#4496](https://github.com/streamlit/streamlit/pull/4496)).

## **Version 1.7.0**

_Release date: March 3, 2022_

**Highlights**

- Introducing `st.snow`, celebrating our acquisition by Snowflake! See more information in [our blog post](https://blog.streamlit.io/snowflake-to-acquire-streamlit/).

## **Version 1.6.0**

_Release date: Feb 24, 2022_

**Other Changes**

- 🗜 WebSocket compression is now disabled by default, which will improve CPU and latency performance for large dataframes. You can use the `server.enableWebsocketCompression` configuration option to re-enable it if you find the increased network traffic more impactful.
- ☑️ 🔘 Radio and checkboxes improve focus on Keyboard navigation ([#4308](https://github.com/streamlit/streamlit/pull/4308)).

## **Version 1.5.0**

_Release date: Jan 27, 2022_

**Notable Changes**

- 🌟 Favicon defaults to a PNG to allow for transparency ([#4272](https://github.com/streamlit/streamlit/pull/4272)).
- 🚦 Select Slider Widget now has the `disabled` parameter that removes interactivity (completing all of our widgets) ([#4314](https://github.com/streamlit/streamlit/pull/4314)).

**Other Changes**

- 🔤 Improvements to our markdown library to provide better support for HTML (specifically nested HTML) ([#4221](https://github.com/streamlit/streamlit/pull/4221)).
- 📖 Expanders maintain their expanded state better when multiple expanders are present ([#4290](https://github.com/streamlit/streamlit/pull/4290)).
- 🗳 Improved file uploader and camera input to call its `on_change` handler only when necessary ([#4270](https://github.com/streamlit/streamlit/pull/4270)).

## **Version 1.4.0**

_Release date: Jan 13, 2022_

**Highlights**

- 📸 Introducing `st.camera_input` for uploading images straight from your camera.

**Notable Changes**

- 🚦 Widgets now have the `disabled` parameter that removes interactivity.
- 🚮 Clear `st.experimental_memo` and `st.experimental_singleton` programmatically by using the `clear()` method on a cached function.
- 📨 Developers can now configure the maximum size of a message to accommodate larger messages within the Streamlit application. See `server.maxMessageSize`.
- 🐍 We formally added support for Python 3.10.

**Other Changes**

- 😵‍💫 Calling `str` or `repr` on `threading.current_thread()` does not cause a RecursionError ([#4172](https://github.com/streamlit/streamlit/issues/4172)).
- 📹 Gracefully stop screencast recording when user removes permission to record ([#4180](https://github.com/streamlit/streamlit/pull/4180)).
- 🌇 Better scale images by using a higher-quality image bilinear resampling algorithm ([#4159](https://github.com/streamlit/streamlit/pull/4159)).

---

# 2021 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2021


This page contains release notes for Streamlit versions released in 2021. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## Version 1.3.0

_Release date: Dec 16, 2021_

**Notable Changes**

- 💯 Support for NumPy values in `st.metric`.
- 🌐 Support for Mesh Layers in PyDeck.
- 📊 Updated Plotly chart version to support the latest features.
- 🏀 `st.spinner` element has visual animated spinner.
- 🍰 `st.caption` supports HTML in text with `unsafe_allow_html` parameter.

**Other Changes**

- 🪲 Bug fix: Allow `st.session_state` to be used to set number_input values with no warning ([#4047](https://github.com/streamlit/streamlit/pull/4047)).
- 🪲 Bug fix: Fix footer alignment in wide mode ([#4035](https://github.com/streamlit/streamlit/pull/4035)).
- 🐞 Bug fix: Better support for Graphviz and Bokeh charts in containers (columns, expanders, etc.) ([#4039](https://github.com/streamlit/streamlit/pull/4039)).
- 🐞 Bug fix: Support inline data values in Vega-Lite ([#4070](https://github.com/streamlit/streamlit/pull/4070)).
- ✍️ Types: Updated type annotations for experimental memo and singleton decorators.
- ✍️ Types: Improved type annotations for `st.selectbox`, `st.select_slider`, `st.radio`, `st.number_input`, and `st.multiselect`.

## Version 1.2.0

_Release date: Nov 11, 2021_

**Notable Changes**

- ✏️ `st.text_input` and `st.text_area` now have a `placeholder` parameter to display text when the field is empty.
- 📏 Viewers can now resize the input box in `st.text_area`.
- 📁 Streamlit can auto-reload when files in sub-directories change.
- 🌈 We've upgraded Bokeh support to 2.4.1! We recommend updating your Bokeh library to 2.4.1 to maintain functionality. Going forward, we'll let you know if there's a mismatch in your Bokeh version via an error prompt.
- 🔒 Developers can access secrets via attribute notation (e.g. `st.secrets.key` vs `st.secrets["key"]`) just like session state.
- ✍️ Publish type annotations according to [PEP 561](https://mypy.readthedocs.io/en/stable/installed_packages.html). Users now get type annotations for Streamlit when running mypy ([#4025](https://github.com/streamlit/streamlit/pull/4025)).

**Other Changes**

- 👀 Visual fixes ([#3863](https://github.com/streamlit/streamlit/pull/3863), [#3995](https://github.com/streamlit/streamlit/pull/3995), [#3926](https://github.com/streamlit/streamlit/pull/3926), [#3975](https://github.com/streamlit/streamlit/pull/3975)).
- 🍔 Fixes to the hamburger menu ([#3968](https://github.com/streamlit/streamlit/pull/3968)).
- 🖨️ Ability to print session state ([#3970](https://github.com/streamlit/streamlit/pull/3970)).

## Version 1.1.0

_Release date: Oct 21, 2021_

**Highlights**

- 🧠 Memory improvements: Streamlit apps allocate way less memory over time now.

**Notable Changes**

- ♻️ Apps automatically rerun now when the content of `secrets.toml` changes (before this you had to refresh the page manually).

**Other Changes**

- 🔗 Redirected some links to our [brand-new docs site](https://docs.streamlit.io/), e.g. in exceptions.
- 🪲 Bug fix: Allow initialization of range slider with session state ([#3586](https://github.com/streamlit/streamlit/issues/3586)).
- 🐞 Bug fix: Refresh chart when using `add_rows` with `datetime` index ([#3653](https://github.com/streamlit/streamlit/issues/3653)).
- ✍️ Added some more type annotation in our codebase ([#3908](https://github.com/streamlit/streamlit/issues/3908)).

## Version 1.0.0

_Release date: Oct 5, 2021_

**Highlights**

- 🎈Announcing Streamlit 1.0! To read more about check out our [1.0 blog post](https://blog.streamlit.io/announcing-streamlit-1-0/).

**Other Changes**

- 🐞 Fixed an issue where using `df.dtypes` to show datatypes for a DF fails while using Arrow ([#3709](https://github.com/streamlit/streamlit/issues/3709)), Image captions stay within image width and are readable ([#3530](https://github.com/streamlit/streamlit/issues/3530)).

## Version 0.89.0

_Release date: Sep 22, 2021_

**Highlights**

- 💰 Introducing `st.experimental_memo` and `experimental_singleton`, a new primitive for caching! See [our blog post](https://blog.streamlit.io/new-experimental-primitives-for-caching/).
- 🍔 Streamlit allows developers to configure their hamburger menu to be more user-centric.

**Notable Changes**

- 💅 We updated our UI to a more polished look with a new font.
- 🎨 We now support `theme.base` in the theme object when it's sent to custom components.
- 🧠 We've modified session state to reset widgets if any of their arguments changed even if they provide a key.
  - Some widget behavior may have changed, but we believe this change makes the most sense. We have added a section to [our documentation](/develop/concepts/widget-semantics) describing how they behave.

**Other Changes**

- 🐞 Bug fixes: Support svgs from a URL ([#3809](https://github.com/streamlit/streamlit/pull/3809)) and that do not start with `<svg>` tag ([#3789](https://github.com/streamlit/streamlit/pull/3789)).

## Version 0.88.0

_Release date: Sep 2, 2021_

**Highlights**

- ⬇️ Introducing `st.download_button`, a new button widget for easily downloading files.

**Notable Changes**

- 🛑 We made changes to improve the redacted exception experience on Streamlit Community Cloud. When `client.showErrorDetails=true` exceptions display the Error Type and the Traceback, but redact the actual error text to prevent data leaks.

## Version 0.87.0

_Release date: Aug 19, 2021_

**Highlights**

- 🔢 Introducing `st.metric`, an API for displaying KPIs. Check out the [demo app](https://streamlit-release-demos-0-87streamlit-app-0-87-rfzphf.streamlit.app/) showcasing the functionality.

**Other Changes**

- 🐞 **Bug Fixes**: File uploader retains state upon expander closing ([#3557](https://github.com/streamlit/streamlit/issues/3557)), setIn Error with `st.empty` ([#3659](https://github.com/streamlit/streamlit/issues/3659)), Missing IFrame embeds in docs ([#3706](https://github.com/streamlit/streamlit/issues/3706)), Fix error writing certain PNG files ([#3597](https://github.com/streamlit/streamlit/issues/3597)).

## Version 0.86.0

_Release date: Aug 5, 2021_

**Highlights**

- 🎓 Our layout primitives are graduating from beta! You can now use `st.columns`, `st.container` and `st.expander` without the `beta_` prefix.

**Notable Changes**

- 📱 When using `st.columns`, columns will stack vertically when viewport size \</svg>

---

# 2020 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2020


This page contains release notes for Streamlit versions released in 2020. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## Version 0.73.0

_Release date: December 17, 2020_

**Notable Changes**

- 🐍 Streamlit can now be installed on Python 3.9. Streamlit components are not
  yet compatible with Python 3.9 and must use version 3.8 or earlier.
- 🧱 Streamlit Components now allows same origin, enabling features provided by
  the browser such as a webcam component.
- 🐙 Fix Streamlit sharing deploy experience for users running on Git versions
  2.7.0 or earlier.
- 🧰 Handle unexpected closing of uploaded files for [`st.file_uploader`](https://docs.streamlit.io/en/0.72.0/api.html#streamlit.file_uploader).

## Version 0.72.0

_Release date: December 2, 2020_

**Notable Changes**

- 🌈 Establish a framework for theming and migrate existing components.
- 📱 Improve the sidebar experience for mobile devices.
- 🧰 Update [`st.file_uploader`](https://docs.streamlit.io/en/0.71.0/api.html#streamlit.file_uploader) to reduce reruns.

## Version 0.71.0

_Release date: November 11, 2020_

**Notable Changes**

- 📁 Updated [`st.file_uploader`](https://docs.streamlit.io/en/0.71.0/api.html#streamlit.file_uploader)
  to automatically reset buffer on app reruns.
- 📊 Optimize the default rendering of charts and reduce issues with the initial render.

## Version 0.70.0

_Release date: October 28, 2020_

**Notable Changes**

- 🧪 [`st.set_page_config`](https://docs.streamlit.io/en/0.70.0/api.html#streamlit.set_page_config) and [`st.color_picker`](https://docs.streamlit.io/en/0.70.0/api.html#streamlit.color_picker) have now been moved into the
  Streamlit namespace. These will be removed from beta January 28th, 2021. Learn
  more about our beta process [here](https://docs.streamlit.io/en/0.70.0/api.html#beta-and-experimental-features).
- 📊 Improve display of bar charts for discrete values.

## Version 0.69.0

_Release date: October 15, 2020_

**Highlights:**

- 🎁 Introducing Streamlit sharing, the best way to deploy, manage, and share your public Streamlit apps—for free. Read more about it on our [blog post](http://blog.streamlit.io/introducing-streamlit-sharing/) or sign up [here](https://streamlit.io/sharing)!
- Added `st.experimental_rerun` to programatically re-run your app. Thanks [SimonBiggs](https://github.com/SimonBiggs)!

**Notable Changes**

- 📹 Better support across browsers for start and stop times for st.video.
- 🖼 Bug fix for intermittently failing media files
- 📦 Bug fix for custom components compatibility with Safari. Make sure to upgrade to the latest [streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib).

## Version 0.68.0

_Release date: October 8, 2020_

**Highlights:**

- ⌗ Introducing new layout options for Streamlit! Move aside, vertical layout.
  Make a little space for... horizontal layout! Check out our
  [blog post](https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/).
- 💾 File uploader redesigned with new functionality for multiple files uploads
  and better support for working with uploaded files. This may cause breaking
  changes. Please see the new api in our
  [documentation](https://docs.streamlit.io/en/0.68.0/api.html#streamlit.file_uploader)

**Notable Changes**

- 🎈 `st.balloon` has gotten a facelift with nicer balloons and smoother animations.
- 🚨 Breaking Change: Following the deprecation of `st.deck_gl_chart` in
  January 2020, we have now removed the API completely. Please use
  `st.pydeck_chart` instead.
- 🚨 Breaking Change: Following the deprecation of `width` and `height` for
  `st.altair_chart`, `st.graphviz_chart`, `st.plotly_chart`, and
  `st.vega_lite_chart` in January 2020, we have now removed the args completely.
  Please set the width and height in the respective charting library.

## Version 0.67.0

_Release date: September 16, 2020_

**Highlights:**

- 🦷 Streamlit Components can now return bytes to your Streamlit App. To create a
  component that returns bytes, make sure to upgrade to the latest
  [streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib).

**Notable Changes**

- 📈 Deprecation warning: Beginning December 1st, 2020 `st.pyplot()` will require a figure to
  be provided. To disable the deprecation warning, please set `deprecation.showPyplotGlobalUse`
  to `False`
- 🎚 `st.multiselect` and `st.select` are now lightning fast when working with large datasets. Thanks [masa3141](https://github.com/masa3141)!

## Version 0.66.0

_Release date: September 1, 2020_

**Highlights:**

- ✏️ `st.write` is now available for use in the sidebar!
- 🎚 A slider for distinct or non-numerical values is now available with `st.select_slider`.
- ⌗ Streamlit Components can now return dataframes to your Streamlit App. Check out our [SelectableDataTable example](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable).
- 📦 The Streamlit Components library used in our Streamlit Component template is
  now available as a npm package ([streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib)) to simplify future upgrades to the latest version.
  Existing components do not need to migrate.

**Notable Changes**

- 🐼 Support StringDtype from pandas version 1.0.0
- 🧦 Support for running Streamlit on Unix sockets

## Version 0.65.0

_Release date: August 12, 2020_

**Highlights:**

- ⚙️ Ability to set page title, favicon, sidebar state, and wide mode via st.beta_set_page_config(). See our [documentation](https://docs.streamlit.io/en/0.65.0/api.html#streamlit.set_page_config) for details.
- 📝 Add stateful behaviors through the use of query parameters with st.experimental_set_query_params and st.experimental_get_query_params. Thanks [@zhaoooyue](https://github.com/zhaoooyue)!
- 🐼 Improved pandas dataframe support for st.radio, st.selectbox, and st.multiselect.
- 🛑 Break out of your Streamlit app with st.stop.
- 🖼 Inline SVG support for st.image.

**Callouts:**

- 🚨Deprecation Warning: The st.image parameter format has been renamed to output_format.

## Version 0.64.0

_Release date: July 23, 2020_

**Highlights:**

- 📊 Default matplotlib to display charts with a tight layout. To disable this,
  set `bbox_inches` to `None`, inches as a string, or a `Bbox`
- 🗃 Deprecation warning for automatic encoding on `st.file_uploader`
- 🙈 If `gatherUserStats` is `False`, do not even load the Segment library.
  Thanks [@tanmaylaud](https://github.com/tanmaylaud)!

## Version 0.63.0

_Release date: July 13, 2020_

**Highlights:**

- 🧩 **Support for Streamlit Components!!!** See
  [documentation](https://docs.streamlit.io/en/latest/streamlit_components.html) for more info.
- 🕗 Support for datetimes in
  [`st.slider`](https://docs.streamlit.io/en/latest/api.html#streamlit.slider). And, of course, just
  like any other value you use in `st.slider`, you can also pass in two-element lists to get a
  datetime range slider.

## Version 0.62.0

_Release date: June 21, 2020_

**Highlights:**

- 📨 Ability to turn websocket compression on/off via the config option
  `server.enableWebsocketCompression`. This is useful if your server strips HTTP headers and you do
  not have access to change that behavior.
- 🗝️ Out-of-the-box support for CSRF protection using the
  [Cookie-to-header token](https://en.wikipedia.org/wiki/Cross-site_request_forgery#Cookie-to-header_token)
  technique. This means that if you're serving your Streamlit app from multiple replicas you'll need
  to configure them to to use the same cookie secret with the `server.cookieSecret` config option.
  To turn XSRF protection off, set `server.enableXsrfProtection=false`.

**Notable bug fixes:**

- 🖼️ Added a grace period to the image cache expiration logic in order to fix multiple related bugs
  where images sent with `st.image` or `st.pyplot` were sometimes missing.

## Version 0.61.0

_Release date: June 2, 2020_

**Highlights:**

- 📅 Support for date ranges in `st.date_picker`. See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.date_picker)
  for more info, but the TLDR is: just pass a list/tuple as the default date and it will be
  interpreted as a range.
- 🗣️ You can now choose whether `st.echo` prints the code above or below the output of the echoed
  block. To learn more, refer to the `code_location` argument in the
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.echo).
- 📦 Improved `@st.cache` support for Keras models and Tensorflow `saved_models`.

## Version 0.60.0

_Release date: May 18, 2020_

**Highlights:**

- ↕️ Ability to set the height of an `st.text_area` with the `height` argument
  (expressed in pixels). See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.text_area) for more.
- 🔡 Ability to set the maximimum number of characters allowed in `st.text_area`
  or `st.text_input`. Check out the `max_chars` argument in the
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.text_area).
- 🗺️ Better DeckGL support for the [H3](https://h3geo.org/) geospatial indexing
  system. So now you can use things like `H3HexagonLayer` in
  [`st.pydeck_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart).
- 📦 Improved `@st.cache` support for PyTorch TensorBase and Model.

## Version 0.59.0

_Release date: May 05, 2020_

**Highlights:**

- 🎨 New color-picker widget! Use it with
  [`st.beta_color_picker()`](https://docs.streamlit.io/en/0.69.0/api.html#streamlit.beta_color_picker)
- 🧪 Introducing `st.beta_*` and `st.experimental_*` function prefixes, for faster
  Streamlit feature releases. See
  [docs](https://docs.streamlit.io/en/latest/api.html#pre-release-features) for more info.
- 📦 Improved `@st.cache` support for SQL Alchemy objects, CompiledFFI, PyTorch
  Tensors, and `builtins.mappingproxy`.

## Version 0.58.0

_Release date: April 22, 2020_

**Highlights:**

- 💼 Made `st.selectbox` filtering case-insensitive.
- ㈬ Better support for Tensorflow sessions in `@st.cache`.
- 📊 Changed behavior of `st.pyplot` to auto-clear the figure only when using
  the global Matplotlib figure (i.e. only when calling `st.pyplot()` rather
  than `st.pyplot(fig)`).

## Version 0.57.0

_Release date: March 26, 2020_

**Highlights:**

- ⏲️ Ability to set expiration options for `@st.cache`'ed functions by setting
  the `max_entries` and `ttl` arguments. See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.cache).
- 🆙 Improved the machinery behind `st.file_uploader`, so it's much more
  performant now! Also increased the default upload limit to 200MB
  (configurable via `server.max_upload_size`).
- 🔒 The `server.address` config option now _binds_ the server to that address
  for added security.
- 📄 Even more details added to error messages for `@st.cache` for easier
  debugging.

## Version 0.56.0

_Release date: February 15, 2020_

**Highlights:**

- 📄 Improved error messages for st.cache. The errors now also point to the new
  caching docs we just released. Read more
  [here](https://discuss.streamlit.io/t/help-us-stress-test-streamlit-s-latest-caching-update/1944)!

**Breaking changes:**

- 🐍 As [announced last month](https://discuss.streamlit.io/t/streamlit-will-deprecate-python-2-in-february/1656),
  **Streamlit no longer supports Python 2.** To use Streamlit you'll need
  Python 3.5 or above.

## Version 0.55.0

_Release date: February 4, 2020_

**Highlights:**

- 📺 **Ability to record screencasts directly from Streamlit!** This allows
  you to easily record and share explanations about your models, analyses,
  data, etc. Just click ☰ then "Record a screencast". Give it a try!

## Version 0.54.0

_Release date: January 29, 2020_

**Highlights:**

- ⌨️ Support for password fields! Just pass `type="password"` to
  `st.text_input()`.

**Notable fixes:**

- ✳️ Numerous st.cache improvements, including better support for complex objects.
- 🗣️ Fixed cross-talk in sidebar between multiple users.

**Breaking changes:**

- If you're using the SessionState <del>hack</del> Gist, you should re-download it!
  Depending on which hack you're using, here are some links to save you some
  time:
  - [SessionState.py](https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92)
  - [st_state_patch.py](https://gist.github.com/tvst/0899a5cdc9f0467f7622750896e6bd7f)

## Version 0.53.0

_Release date: January 14, 2020_

**Highlights:**

- 🗺️ Support for all DeckGL features! Just use
  [Pydeck](https://deckgl.readthedocs.io/en/latest/) instead of
  [`st.deck_gl_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart).
  To do that, simply pass a PyDeck object to
  [`st.pydeck_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart),
  [`st.write`](https://docs.streamlit.io/en/latest/api.html#streamlit.write),
  or [magic](https://docs.streamlit.io/en/latest/api.html#magic).

  _Note that as a **preview release** things may change in the near future.
  Looking forward to hearing input from the community before we stabilize the
  API!_

  **The goals is for this to replace `st.deck_gl_chart`,** since it
  is does everything the old API did _and much more!_

- 🆕 Better handling of Streamlit upgrades while developing. We now auto-reload
  the browser tab if the app it is displaying uses a newer version of Streamlit
  than the one the tab is running.

- 👑 New favicon, with our new logo!

**Notable fixes:**

- Magic now works correctly in Python 3.8. It no longer causes
  docstrings to render in your app.

**Breaking changes:**

- Updated how we calculate the default width and height of all chart types.
  We now leave chart sizing up to your charting library itself, so please refer
  to the library's documentation.

  As a result, the `width` and `height` arguments have been deprecated
  from most chart commands, and `use_container_width` has been introduced
  everywhere to allow you to make charts fill as much horizontal space as
  possible (this used to be the default).

---

# 2019 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2019


This page contains release notes for Streamlit versions released in 2019. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## Version 0.52.0

_Release date: December 20, 2019_

**Highlights:**

- 📤 Preview release of the file uploader widget. To try it out just call
  [`st.file_uploader`](https://docs.streamlit.io/en/latest/api.html#streamlit.file_uploader)!

  _Note that as a **preview release** things may change in the near future.
  Looking forward to hearing input from the community before we stabilize the
  API!_

- 👋 Support for [emoji codes](https://www.webfx.com/tools/emoji-cheat-sheet/) in
  `st.write` and `st.markdown`! Try it out with `st.write("Hello :wave:")`.

**Breaking changes:**

- 🧹 `st.pyplot` now clears figures by default, since that's what you want 99% of
  the time. This allows you to create two or more Matplotlib charts without
  having to call
  [`pyplot.clf`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.clf.html)
  every time. If you want to turn this behavior off, use
  [`st.pyplot(clear_figure=False)`](https://docs.streamlit.io/en/latest/api.html#streamlit.pyplot)
- 📣 `st.cache` no longer checks for input mutations. This is the first change
  of our ongoing effort to simplify the caching system and prepare Streamlit
  for the launch of other caching primitives like Session State!

## Version 0.51.0

_Release date: November 30, 2019_

**Highlights:**

- 🐕 You can now tweak the behavior of the file watcher with the config option `server.fileWatcherType`. Use it to switch between:
  - `auto` (default) : Streamlit will attempt to use the watchdog module, and
    falls back to polling if watchdog is not available.
  - `watchdog` : Force Streamlit to use the watchdog module.
  - `poll` : Force Streamlit to always use polling.
  - `none` : Streamlit will not watch files.

**Notable bug fixes:**

- Fix the "keyPrefix" option in static report sharing [#724](https://github.com/streamlit/streamlit/pull/724)
- Add support for getColorX and getTargetColorX to DeckGL Chart [#718](https://github.com/streamlit/streamlit/pull/718)
- Fixing Tornado on Windows + Python 3.8 [#682](https://github.com/streamlit/streamlit/pull/682)
- Fall back on webbrowser if xdg-open is not installed on Linux [#701](https://github.com/streamlit/streamlit/pull/701)
- Fixing number input spin buttons for Firefox [#683](https://github.com/streamlit/streamlit/pull/683)
- Fixing CTRL+ENTER on Windows [#699](https://github.com/streamlit/streamlit/pull/699)
- Do not automatically create credential file when in headless mode [#467](https://github.com/streamlit/streamlit/pull/467)

## Version 0.50.1

_Release date: November 10, 2019_

**Highlights:**

- 👩‍🎓 SymPy support and ability to draw mathematical expressions using LaTeX! See
  [`st.latex`](/develop/api-reference/text/st.latex),
  [`st.markdown`](/develop/api-reference/text/st.markdown),
  and
  [`st.write`](/develop/api-reference/write-magic/st.write).
- 🌄 You can now set config options using environment variables. For example,
  `export STREAMLIT_SERVER_PORT=9876`.
- 🐱 Ability to call `streamlit run` directly with Github and Gist URLs. No
  need to grab the "raw" URL first!
- 📃 Cleaner exception stack traces. We now remove all Streamlit-specific code
  from stack traces originating from the user's app.

## Version 0.49.0

_Release date: October 23, 2019_

**Highlights:**

- 💯 New input widget for entering numbers with the keyboard: `st.number_input()`
- 📺 Audio/video improvements: ability to load from a URL, to embed YouTube
  videos, and to set the start position.
- 🤝 You can now (once again) share static snapshots of your apps to S3! See
  the S3 section of `streamlit config show` to set it up. Then share from
  top-right menu.
- ⚙️ Use `server.baseUrlPath` config option to set Streamlit's URL to something
  like `http://domain.com/customPath`.

**Notable bug fixes:**

- Fixes numerous Windows bugs, including [Issues
  #339](https://github.com/streamlit/streamlit/issues/399) and
  [#401](https://github.com/streamlit/streamlit/issues/301).

## Version 0.48.0

_Release date: October 12, 2019_

**Highlights:**

- 🔧 Ability to set config options as command line flags or in a local config file.
- ↕️ You can now maximize charts and images!
- ⚡ Streamlit is now much faster when writing data in quick succession to your app.
- ✳️ Ability to blacklist folder globs from "run on save" and `@st.cache` hashing.
- 🎛️ Improved handling of widget state when Python file is modified.
- 🙈 Improved HTML support in `st.write` and `st.markdown`. HTML is still unsafe, though!

**Notable bug fixes:**

- Fixes `@st.cache` bug related to having your Python environment on current
  working directory. [Issue #242](https://github.com/streamlit/streamlit/issues/242)
- Fixes loading of root url `/` on Windows. [Issue #244](https://github.com/streamlit/streamlit/issues/244)

## Version 0.47.0

_Release date: October 1, 2019_

**Highlights:**

- 🌄 New hello.py showing off 4 glorious Streamlit apps. Try it out!
- 🔄 Streamlit now automatically selects an unused port when 8501 is already in use.
- 🎁 Sidebar support is now out of beta! Just start any command with `st.sidebar.` instead of `st.`
- ⚡ Performance improvements: we added a cache to our websocket layer so we no longer re-send data to the browser when it hasn't changed between runs
- 📈 Our "native" charts `st.line_chart`, `st.area_chart` and `st.bar_chart` now use Altair behind the scenes
- 🔫 Improved widgets: custom st.slider labels; default values in multiselect
- 🕵️‍♀️ The filesystem watcher now ignores hidden folders and virtual environments
- 💅 Plus lots of polish around caching and widget state management

**Breaking change:**

- 🛡️ We have temporarily disabled support for sharing static "snapshots" of Streamlit apps. Now that we're no longer in a limited-access beta, we need to make sure sharing is well thought through and abides by laws like the DMCA. But we're working on a solution!

## Version 0.46.0

_Release date: September 19, 2019_

**Highlights:**

- ✨ Magic commands! Use `st.write` without typing `st.write`. See
  [https://docs.streamlit.io/en/latest/api.html#magic-commands](https://docs.streamlit.io/en/latest/api.html#magic-commands)
- 🎛️ New `st.multiselect` widget.
- 🐍 Fixed numerous install issues so now you can use `pip install streamlit`
  even in Conda! We've therefore deactivated our Conda repo.
- 🐞 Multiple bug fixes and additional polish in preparation for our launch!

**Breaking change:**

- 🛡️ HTML tags are now blacklisted in `st.write`/`st.markdown` by default. More
  information and a temporary work-around at:
  [https://github.com/streamlit/streamlit/issues/152](https://github.com/streamlit/streamlit/issues/152)

## Version 0.45.0

_Release date: August 28, 2019_

**Highlights:**

- 😱 Experimental support for _sidebar_! Let us know if you want to be a beta
  tester.
- 🎁 Completely redesigned `st.cache`! Much more performant, has a cleaner API,
  support for caching functions called by `@st.cached` functions,
  user-friendly error messages, and much more!
- 🖼️ Lightning fast `st.image`, ability to choose between JPEG and PNG
  compression, and between RGB and BGR (for OpenCV).
- 💡 Smarter API for `st.slider`, `st.selectbox`, and `st.radio`.
- 🤖 Automatically fixes the Matplotlib backend -- no need to edit .matplotlibrc

## Version 0.44.0

_Release date: July 28, 2019_

**Highlights:**

- ⚡ Lightning-fast reconnect when you do a ctrl-c/rerun on your Streamlit code
- 📣 Useful error messages when the connection fails
- 💎 Fixed multiple bugs and improved polish of our newly-released interactive widgets

## Version 0.43.0

_Release date: July 9, 2019_

**Highlights:**

- ⚡ Support for interactive widgets! 🎈🎉

## Version 0.42.0

_Release date: July 1, 2019_

**Highlights:**

- 💾 Ability to save Vega-Lite and Altair charts to SVG or PNG
- 🐇 We now cache JS files in your browser for faster loading
- ⛔ Improvements to error-handling inside Streamlit apps

## Version 0.41.0

_Release date: June 24, 2019_

**Highlights:**

- 📈 Greatly improved our support for named datasets in Vega-Lite and Altair
- 🙄 Added ability to ignore certain folders when watching for file changes. See the `server.folderWatchBlacklist` config option.
- ☔ More robust against syntax errors on the user's script and imported modules

## Version 0.40.0

_Release date: June 10, 2019_

**Highlights:**

- Streamlit is more than 10x faster. Just save and watch your analyses update instantly.
- We changed how you run Streamlit apps:
  `$ streamlit run your_script.py [script args]`
- Unlike the previous versions of Streamlit, `streamlit run [script] [script args]` creates a server (now you don't need to worry if the proxy is up). To kill the server, all you need to do is hit **Ctrl+c**.

**Why is this so much faster?**

Now, Streamlit keeps a single Python session running until you kill the server. This means that Streamlit can re-run your code without kicking off a new process; imported libraries are cached to memory. An added bonus is that `st.cache` now caches to memory instead of to disk.

**What happens if I run Streamlit the old way?**

If you run `$ python your_script.py` the script will execute from top to bottom, but won't produce a Streamlit app.

**What are the limitations of the new architecture?**

- To switch Streamlit apps, first you have to kill the Streamlit server with **Ctrl-c**. Then, you can use `streamlit run` to generate the next app.
- Streamlit only works when used inside Python files, not interactively from the Python REPL.

**What else do I need to know?**

- The strings we print to the command line when **liveSave** is on have been cleaned up. You may need to adjust any RegEx that depends on those.
- A number of config options have been renamed:

  | Old config                 | New config            |
  | -------------------------- | --------------------- |
  | proxy.isRemote             | server.headless       |
  | proxy.liveSave             | server.liveSave       |
  | proxy.runOnSave            | server.runOnSave      |
  | proxy.watchFileSystem      | server.runOnSave      |
  | proxy.enableCORS           | server.enableCORS     |
  | proxy.port                 | server.port           |
  | browser.proxyAddress       | browser.serverAddress |
  | browser.proxyPort          | browser.serverPort    |
  | client.waitForProxySecs    | _n/a_                 |
  | client.throttleSecs        | _n/a_                 |
  | client.tryToOutliveProxy   | _n/a_                 |
  | client.proxyAddress        | _n/a_                 |
  | client.proxyPort           | _n/a_                 |
  | proxy.autoCloseDelaySecs   | _n/a_                 |
  | proxy.reportExpirationSecs | _n/a_                 |

**What if something breaks?**

If the new Streamlit isn't working, please let us know by Slack or email. You can downgrade at any time with these commands:

```bash
pip install --upgrade streamlit==0.37
```

```bash
conda install streamlit=0.37
```

**What's next?**

Thank you for staying with us on this journey! This version of Streamlit lays the foundation for interactive widgets, a new feature of Streamlit we're really excited to share with you in the next few months.

## Version 0.36.0

_Release date: May 03, 2019_

**Highlights**

- 🚣‍♀️ `st.progress()` now also accepts floats from 0.0–1.0
- 🤯 Improved rendering of long headers in DataFrames
- 🔐 Shared apps now default to HTTPS

## Version 0.35.0

_Release date: April 26, 2019_

**Highlights**

- 📷 Bokeh support! Check out docs for `st.bokeh_chart`
- ⚡️ Improved the size and load time of saved apps
- ⚾️ Implemented better error-catching throughout the codebase

---

# Pre-release features

Source: https://docs.streamlit.io/develop/quick-reference/prerelease


At Streamlit, we like to move quick while keeping things stable. In our latest effort to move even faster without sacrificing stability, we're offering our bold and fearless users two ways to try out Streamlit's bleeding-edge features:

1. [Experimental features](#experimental-features)
2. [Nightly releases](#nightly-releases)

## Experimental Features

Less stable Streamlit features have one naming convention: `st.experimental_`. This distinction is a prefix we attach to our command names to make sure their status is clear to everyone.

Here's a quick rundown of what you get from each naming convention:

- **st**: this is where our core features like `st.write` and `st.dataframe` live. If we ever make backward-incompatible changes to these, they will take place gradually and with months of announcements and warnings.
- **experimental**: this is where we'll put all new features that may or may not ever make it into Streamlit core. This gives you a chance to try the next big thing we're cooking up weeks or months before we're ready to stabilize its API. We don't know whether these features have a future, but we want you to have access to everything we're trying, and work with us to figure them out.

Features with the `experimental_` naming convention are things that we're still working on or trying
to understand. If these features are successful, at some point they'll become part of Streamlit
core. If unsuccessful, these features are removed without much notice. While in experimental, a feature's API and behaviors may not be stable, and it's possible they could change in ways that aren't backward-compatible.

<Warning>

Experimental features and their APIs may change or be removed at any time.

</Warning>

### The lifecycle of an experimental feature

1. A feature is added with the `experimental_` prefix.
2. The feature is potentially tweaked over time, with possible API/behavior breakages.
3. If successful, we promote the feature to Streamlit core and remove it from `experimental_`:
   - a\. The feature's API stabilizes and the feature is _cloned_ without the `experimental_` prefix, so it exists as both `st` and `experimental_`. At this point, users will see a warning when using the version of the feature with the `experimental_` prefix -- but the feature will still work.
   - b\. At some point, the code of the `experimental_`-prefixed feature is _removed_, but there will still be a stub of the function prefixed with `experimental_` that shows an error with appropriate instructions.
   - c\. Finally, at a later date the `experimental_` version is removed.
4. If unsuccessful, the feature is removed without much notice and we leave a stub in `experimental_` that shows an error with instructions.

## Nightly releases

In addition to experimental features, we offer another way to try out Streamlit's newest features: nightly releases.

At the end of each day (at night 🌛), our bots run automated tests against the latest Streamlit code and, if everything looks good, it publishes them as the `streamlit-nightly` package. This means the nightly build includes all our latest features, bug fixes, and other enhancements on the same day they land on our codebase.

**How does this differ from official releases?**

Official Streamlit releases go not only through both automated tests but also rigorous manual testing, while nightly releases only have automated tests. It's important to keep in mind that new features introduced in nightly releases often lack polish. In our official releases, we always make double-sure all new features are ready for prime time.

**How do I use the nightly release?**

All you need to do is install the `streamlit-nightly` package:

```bash
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```

<Warning>

You should never have both `streamlit` and `streamlit-nightly` installed in the same environment!

</Warning>

**Why should I use the nightly release?**

Because you can't wait for official releases, and you want to help us find bugs early!

**Why shouldn't I use the nightly release?**

While our automated tests have high coverage, there's still a significant likelihood that there will be some bugs in the nightly code.

**Can I choose which nightly release I want to install?**

If you'd like to use a specific version, you can find the version number in our [Release history](https://pypi.org/project/streamlit-nightly/#history). Specify the desired version using `pip` as usual: `pip install streamlit-nightly==x.yy.zz-123456`.

**Can I compare changes between releases?**

If you'd like to review the changes for a nightly release, you can use the [comparison tool on GitHub](https://github.com/streamlit/streamlit/compare/0.57.3...0.57.4.dev20200412).

---

# Deploy

Source: https://docs.streamlit.io/deploy


Get all the information you need to deploy your app and share it with your users.

<InlineCalloutContainer>
<InlineCallout bold="Concepts." color="lightBlue-70" href="/deploy/concepts" icon="book">Understand the basics of app deployment.</InlineCallout>
<InlineCallout bold="Streamlit Community Cloud." color="lightBlue-70" href="/deploy/streamlit-community-cloud" icon="cloud">Deploy your app on our free platform and join a community of developers who share their apps around the world. This is a great place for your non-commerical, personal, and educational apps.</InlineCallout>
<InlineCallout bold="Snowflake." color="lightBlue-70" href="/deploy/snowflake" icon="ac_unit">Deploy your app in Snowflake for a secure, enterprise-grade environment. This is a great place for your business apps.</InlineCallout>
<InlineCallout bold="Other platforms." color="lightBlue-70" href="/deploy/tutorials" icon="bolt">Learn how to deploy your app on a variety of platforms with our convenient collection of tutorials.</InlineCallout>
</InlineCalloutContainer>

---

# Deployment concepts

Source: https://docs.streamlit.io/deploy/concepts


Learn the fundamental concepts of app deployment. There are three main processes involved in deploying apps.

- Install Python, Streamlit, and other dependencies in your deployment environment.
- Securely handle your secrets and private information.
- Remote start your app (`streamlit run`).

If you're using Streamlit Community Cloud, we'll do most of the work for you!

<InlineCalloutContainer>
<InlineCallout bold="Dependencies." color="lightBlue-70" href="/deploy/concepts/dependencies" icon="build_circle">Understand the basics of configuring your deployment environment.</InlineCallout>
<InlineCallout bold="Secrets." color="lightBlue-70" href="/deploy/concepts/secrets" icon="password">Understand the basics of secret management.</InlineCallout>
</InlineCalloutContainer>

---

# Managing dependencies when deploying your app

Source: https://docs.streamlit.io/deploy/concepts/dependencies


Before you began developing your app, you set up and configured your development environment by installing Python and Streamlit. When you deploy your app, you need to set up and configure your deployment environment in the same way. When you deploy your app to a cloud service, your app's [Python server](/develop/concepts/architecture/architecture#python-backend-server) will be running on a remote machine. This remote machine will not have access all the files and programs on your personal computer.

All Streamlit apps have at least two dependencies: Python and Streamlit. Your app may have additional dependencies in the form of Python packages or software that must be installed to properly execute your script. If you are using a service like Streamlit Community Cloud which is designed for Streamlit apps, we'll take care of Python and Streamlit for you!

## Install Python and other software

If you are using Streamlit Community Cloud, Python is already installed. You can just pick the version in the deployment dialog. If you need to install Python yourself or you have other non-Python software to install, follow your platform's instructions to install additional software. You will commonly use a package management tool to do this.
For example, Streamlit Community Cloud uses Advanced Package Tool (`apt`) for Debian-based Linux systems. For more information about installing non-Python depencies on Streamlit Community Cloud, see [`apt-get` dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies).

## Install Python packages

Once you have Python installed in your deployment environment, you'll need to install all the necessary Python packages, including Streamlit! With each `import` of an installed package, you add a Python dependency to your script. You need to install those dependencies in your deployment environment through a Python package manager.

If you are using Streamlit Community Cloud, you'll have the latest version of Streamlit and all of its dependencies installed by default. So, if you're making a simple app and don't need additional dependencies, you won't have to do anything at all!

### `pip` and `requirements.txt`

Since `pip` comes by default with Python, the most common way to configure your Python environment is with a `requirements.txt` file. Each line of a `requirements.txt` file is a package to `pip install`. You should _not_ include <a href="https://docs.python.org/3/py-modindex.html" target="_blank">built-in Python libraries</a> like `math`, `random`, or `distutils` in your `requirements.txt` file. These are a part of Python and aren't installed separately.

<Tip>

Since dependencies may rely on a specific version of Python, always be aware of the Python version used in your development environment, and select the same version for your deployment environment.

</Tip>

If you have a script like the following, you would only need to install Streamlit. No extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

```python
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')
```

However, it's a best practice accurately record packages you use, so the recommended `requirements.txt` file would be:

```none
streamlit
pandas
numpy
```

If you needed to specify certain versions, another valid example would be:

```none
streamlit==1.24.1
pandas&gt;2.0
numpy

---

# Managing secrets when deploying your app

Source: https://docs.streamlit.io/deploy/concepts/secrets


If you are connecting to data sources or external services, you will likely be handling secret information like credentials or keys. Secret information should be stored and transmitted in a secure manner. When you deploy your app, ensure that you understand your platform's features and mechanisms for handling secrets so you can follow best practice.

Avoid saving secrets directly in your code and keep `.gitignore` updated to prevent accidentally committing a local secret to your repository. For helpful reminders, see [Security reminders](/develop/concepts/connections/security-reminders).

If you are using Streamlit Community Cloud, [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code. If you are using another platform designed for Streamlit, check if they have a built-in mechanism for working with secrets. In some cases, they may even support `st.secrets` or securely uploading your `secrets.toml` file.

For information about using `st.connection` with environment variables, see [Global secrets, managing multiple apps and multiple data stores](/develop/concepts/connections/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores).

---

# Welcome to Streamlit Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud


With Streamlit Community Cloud, you can create, deploy, and manage your Streamlit apps  all for free. Share your apps with the world and build a customized profile page to display your work. Your Community Cloud account connects directly to your GitHub repositories (public or private). Most apps will launch in only a few minutes. Community Cloud handles all of the containerization, so deploying is easy. Bring your own code, or start from one of our popular templates. Rapidly prototype, explore, and update apps by simply changing your code in GitHub. Most changes appear immediately!

Want to avoid the work of setting up a local development environment? Community Cloud can help you quickly configure a codespace to develop in the cloud. Start coding or editing a Streamlit app with just a few clicks. See [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).

Go to our [Community Cloud quickstart](/deploy/streamlit-community-cloud/get-started/quickstart) to speed-run through creating your account, deploying an example app, and editing it using GitHub Codespaces. If you haven't built your first Streamlit app yet, see [Get started with Streamlit](/get-started).

<InlineCalloutContainer>
<InlineCallout bold="Get started." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started" icon="arrow_forward">Learn about Streamlit Community Cloud accounts and how to create one.</InlineCallout>
<InlineCallout bold="Deploy your app." color="lightBlue-70" href="/deploy/streamlit-community-cloud/deploy-your-app" icon="flight_takeoff">A step-by-step guide on how to get your app deployed.</InlineCallout>
<InlineCallout bold="Manage your app." color="lightBlue-70" href="/deploy/streamlit-community-cloud/manage-your-app" icon="settings">Access logs, reboot apps, set favorites, and more. Jump into a GitHub codespace to edit your app in the cloud.</InlineCallout>
<InlineCallout bold="Share your app." color="lightBlue-70" href="/deploy/streamlit-community-cloud/share-your-app" icon="share">Share or embed your app.</InlineCallout>
<InlineCallout bold="Manage your account." color="lightBlue-70" href="/deploy/streamlit-community-cloud/manage-your-account" icon="manage_accounts">Update your email, manage connections, or delete your account.</InlineCallout>
</InlineCalloutContainer>

---

# Get started with Streamlit Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started


Welcome to Streamlit Community Cloud, where you can share your Streamlit apps with the world! Whether you've already created your first Streamlit app or you're just getting started, you're in the right place.

First things first, you need to create your Streamlit Community Cloud account to start deploying apps.

<TileContainer>
<Tile background="lightBlue-70" icon="rocket_launch" link="/deploy/streamlit-community-cloud/get-started/quickstart" text="Create your account and deploy an example app as fast as possible. Jump right into coding with GitHub Codespaces." title="Quickstart"/>
<Tile background="lightBlue-70" icon="security" link="/deploy/streamlit-community-cloud/get-started/trust-and-security" text="Security first! If you want to read up on how we handle your data before you get started, we've got you covered." title="Trust and Security"/>
</TileContainer>

If you're looking for help to build your first Streamlit app, read our [Get started](/get-started) docs for the Streamlit library. If you want to fork an app and start with an example, check out our <a href="https://streamlit.io/gallery" target="_blank">App gallery</a>. Either way, it only takes a few minutes to create your first app.

If you're looking for more detailed instructions than the quickstart, try the following:

<InlineCalloutContainer>
<InlineCallout bold="Create your account." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started/create-your-account" icon="person">See all the options and get complete explanations as you create your Streamlit Community Cloud account.</InlineCallout>
<InlineCallout bold="Connect your GitHub account." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started/connect-your-github-account" icon="code">After your create your Community Cloud account, connect GitHub for source control.</InlineCallout>
<InlineCallout bold="Explore your workspace." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started/explore-your-workspace" icon="computer">Take a quick tour of your Community Cloud workspace. See where all the magic happens.</InlineCallout>
<InlineCallout bold="Deploy an app from a template." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started/deploy-from-a-template" icon="auto_fix_high">Use a template to get your own app up and running in minutes.</InlineCallout>
<InlineCallout bold="Fork and edit a public app." color="lightBlue-70" href="/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app" icon="fork_right">Start with a bang! Fork a public app and jump right into the code.</InlineCallout>
</InlineCalloutContainer>

---

# Quickstart

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart


This is a concise set of steps to create your Streamlit Community Cloud account, deploy a sample app, and start editing it with GitHub Codespaces. For other options and complete explanations, start with [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).

You will sign in to your GitHub account during this process. Community Cloud will use the email from your GitHub account to create your Community Cloud account. For other sign-in options, see [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).

## Prerequisites

- You must have a GitHub account.

## Sign up for Streamlit Community Cloud

1. Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. Click "**Continue to sign-in**."
1. Click "**Continue with GitHub**."
1. Enter your GitHub credentials and follow GitHub's authentication prompts.
1. Fill in your account information, and click "**I accept**" at the bottom.

## Add access to your public repositories

1. In the upper-left corner, click "**Workspaces <i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

# Create your account

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account


Before you can start deploying apps for the world to see, you need to sign up for your Streamlit Community Cloud account.

Each Community Cloud account is associated with an email. Two accounts can't have the same email. When sharing a private app, you will assign viewing privileges by email. Additionally, two accounts can't have the same source control (GitHub account). If you try to create a second Community Cloud account with the same source control, Community Cloud will merge the accounts.

## Sign up

Community Cloud allows you to sign in using one of the three following methods:

- Emailed, one-use codes
- Google
- GitHub

<Important>
    Even when you sign in through GitHub, the authentication flow returns your email address to Community Cloud. Changing the email on your GitHub account can affect your Community Cloud account if you sign in through GitHub.
</Important>

1. Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. Click "**Continue to sign-in**."
1. Continue with one of the three options listed below.

   ### Option 1: Sign in using emailed codes
   1. In the "Email" field, enter your email address.
   1. Click "**Continue**." (If prompted, verify you are human.)
   1. Go to your email inbox, and copy your one-time, six-digit code. The code is valid for ten minutes.
   1. Return to the authentication page, and enter your code. (If prompted, verify you are human.)

   ### Option 2: Sign in using Google
   1. Click "**Continue with Google**."
   1. Enter your Google credentials, and follow Google's authentication prompts.

   ### Option 3: Sign in using GitHub
   1. Click "**Continue with GitHub**."
   1. Enter your GitHub credentials, and follow GitHub's authentication prompts.

      This adds the "Streamlit Community Cloud" OAuth application to your GitHub account. This application is only used to pass your email when you sign in to Community Cloud. On the next page, you'll perform additional steps to allow Community Cloud to access your repositories. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps) in GitHub's docs.

1. Fill in your information, and click "**Continue**" at the bottom.

   The "Primary email" field is prefilled with the email you used to sign in. If you change this email in the account setup form, it will only impact marketing emails; it will not reflect on your new account. To change the email associated with your account after it's created, see [Update your email address](/deploy/streamlit-community-cloud/manage-your-account/update-your-email).

## Finish up

Congratulations on creating your Streamlit Community Cloud account! A warning icon (<i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

# Connect your GitHub account

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account


Connecting GitHub to your Streamlit Community Cloud account allows you to deploy apps directly from the files you store in your repositories. It also lets the system check for updates to those files and automatically update your apps. When you first connect your GitHub account to your Community Cloud account, you'll be able to deploy apps from your public repositories to Community Cloud. If you want to deploy from private repositories, you can give Community Cloud additional permissions to do so. For more information about these permissions, see [GitHub OAuth scope](/deploy/streamlit-community-cloud/status#github-oauth-scope).

<Important>
    In order to deploy an app, you must have **admin** permissions to its repository. If you don't have admin access, contact the repository's owner or fork the repository to create your own copy. For more help, see our <a href="https://discuss.streamlit.io/" target="_blank">community forum</a>.
</Important>

If you are a member of a GitHub organization, that organization is displayed at the bottom of each GitHub OAuth prompt. In this case, we recommend reading about [Organization access](#organization-access) at the end of this page before performing the steps to connect your GitHub account. You must be an organization's owner in GitHub to grant access to that organization.

## Prerequisites

- You must have a Community Cloud account. See [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).
- You must have a GitHub account.

## Add access to public repositories

1. In the upper-left corner, click "**Workspaces <i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

# Explore your workspace

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace


If you just [created your account](/deploy/streamlit-community-cloud/get-started/create-your-account) and [connected your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account), congrats! You are now signed in and ready to go. If you are joining someone else's workspace you may already see some apps.

## Workspaces

Each GitHub account and organization is associated with a workspace in Community Cloud. When you sign in to Community Cloud for the first time, you will land in your personal workspace associated with your GitHub user account. The upper-left corner of Community Cloud shows your current workspace.

![A new, empty workspace in Streamlit Community Cloud. The workspace owner is displayed in the upper-left corner.](/images/streamlit-community-cloud/workspace-empty-SM.png)

### Switching workspaces

To switch between workspaces, click the workspace name in the upper-left corner and select a new workspace.

Other workspaces are available to you as follows:

- When you have write permissions to a repository and the repository owner has joined Community Cloud, you can select the associated workspace. An owner can be a GitHub user or organization.
- If someone has shared an app with you through Community Cloud, you will see the app's associated workspace. This is view-only access.

![This workspace is for the user `sammy-streamlit`, who has access to their personal workspace and another workspace for the organization `we-love-streamlit`.](/images/streamlit-community-cloud/workspace-empty-switch.png)

### Invite other developers to your workspace

Inviting other developers is simple: Just give them write access to your GitHub repository so that you can code together. When they sign in to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, they'll have access to your workspace.

Streamlit Community Cloud inherits developer permissions from GitHub. When others sign in to Community Cloud, they will automatically see the workspaces they share with you. From there you can all deploy, manage, and share apps together.

<Note>

When a user is added to a repository on GitHub, it will take at most 15 minutes before they can deploy or manage the app on Community Cloud. If a user is removed from a repository on GitHub, it will take at most 15 minutes before their permission to manage the app from that repository is revoked.

</Note>

And remember, whenever anyone on the team updates the code on GitHub, the app will automatically update for you!

## My apps

The "**My apps**" section of your workspace is your base of operations to deploy and manage your apps. When you deploy an app, it is added to this section of your workspace.

### Deploying apps

If you already have an app saved to a GitHub repo, you can deploy it directly. Otherwise, Community Cloud provides templates you can use. When you deploy from a template, Community Cloud will fork a project into your GitHub account and deploy from the new fork. This is a convenient way to get started if you haven't already created a Streamlit app.

To get started, just click "**Create app**" in the upper-right corner. To learn more, see [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app) and [Deploy from a template](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template).

## My profile

The "**My profile**" section of your workspace lets you customize a personal portfolio of Streamlit apps to share with the world. Curate and feature your Streamlit apps to show off your work.

## Explore

For inspiration, check out the "**Explore**" section. This is a gallery of Streamlit apps created by the Streamlit community. Check out popular and trending apps, or search for apps in an area that interests you.

---


---

**Navigation:** [← Previous](./09-2025-release-notes.md) | [Index](./index.md) | [Next →](./11-deploy-an-app-from-a-template.md)
