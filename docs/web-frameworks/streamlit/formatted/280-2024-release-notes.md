---
title: "2024 release notes"
source: https://docs.streamlit.io/develop/quick-reference/release-notes/2024
section: 280
---

# 2024 release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2024


This page contains release notes for Streamlit versions released in 2024. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

## **Version 1.41.0**

_Release date: December 10, 2024_

**Notable Changes**

- 🔲 [`st.metric`](/develop/api-reference/data/st.metric) and [`st.columns`](/develop/api-reference/layout/st.columns) have a parameter to show an optional border ([#9927](https://github.com/streamlit/streamlit/pull/9927), [#9928](https://github.com/streamlit/streamlit/pull/9928)).
- 🎨 Text and background color in [Markdown](/develop/api-reference/text/st.markdown) can use the "primary" color from the `theme.primaryColor` configuration option ([#9676](https://github.com/streamlit/streamlit/pull/9676)).
- 🥶 You can freeze columns with [column configuration](/develop/api-reference/data/st.column_config) to make them always visible when scrolling horizontally ([#9535](https://github.com/streamlit/streamlit/pull/9535), [#7078](https://github.com/streamlit/streamlit/issues/7078)).
- 3️⃣ The `type` parameter for [buttons](/develop/api-reference/widgets/st.button) accepts a new option, `"tertiary"` ([#9923](https://github.com/streamlit/streamlit/pull/9923)).
- 🚶‍♂️ Streamlit supports `pathlib.Path` objects everywhere you can use a string path ([#9711](https://github.com/streamlit/streamlit/pull/9711), [#9783](https://github.com/streamlit/streamlit/pull/9783)).
- ⏱️ [`st.date_input`](/develop/api-reference/widgets/st.date_input) and [`st.time_input`](/develop/api-reference/widgets/st.time_input) accept ISO formatted strings for initial values ([#9753](https://github.com/streamlit/streamlit/pull/9753)).
- 💬 [`st.write_stream`](/develop/api-reference/write-magic/st.write_stream) accepts async generators, which it converts internally to sync generators ([#8724](https://github.com/streamlit/streamlit/pull/8724), [#8161](https://github.com/streamlit/streamlit/issues/8161)).
- 🪵 The [`client.showErrorDetails`](/develop/api-reference/configuration/config.toml#client) configuration option has additional values to show or hide more information ([#9909](https://github.com/streamlit/streamlit/pull/9909)).
- 🔎 When Streamlit shows stack traces in the app for uncaught exceptions, internal code is omitted or reduced for easier debugging ([#9913](https://github.com/streamlit/streamlit/pull/9913)).
- 📈 [`st.line_chart`](/develop/api-reference/charts/st.line_chart) shows tooltips for the nearest point on hover ([#9674](https://github.com/streamlit/streamlit/pull/9674)).
- 🌐 [`st.html`](/develop/api-reference/utilities/st.html) will attempt to convert non-string objects with `._repr_html_()` before falling back to `str()` ([#9877](https://github.com/streamlit/streamlit/pull/9877)).
- 🐍 Streamlit supports Python 3.13 and no longer supports Python 3.8 ([#9635](https://github.com/streamlit/streamlit/pull/9635)).

**Other Changes**

- 🔣 Material Symbols have been updated with the latest icons ([#9813](https://github.com/streamlit/streamlit/pull/9813), [#9810](https://github.com/streamlit/streamlit/issues/9810)).
- 👽 Streamlit supports Watchdog version 6 ([#9785](https://github.com/streamlit/streamlit/pull/9785)). Thanks, [RubenVanEldik](https://github.com/RubenVanEldik).
- 🌀 Bug fix: Streamlit only shows cached function spinners on cache misses and doesn't show spinners for nested cached functions ([#9956](https://github.com/streamlit/streamlit/pull/9956), [#9951](https://github.com/streamlit/streamlit/issues/9951)).
- 🔈 Bug fix: Streamlit's audio buffer handles channels better to correctly play audio recordings in Firefox ([#9885](https://github.com/streamlit/streamlit/pull/9885), [#9799](https://github.com/streamlit/streamlit/issues/9799)).
- 🦊 Bug fix: URL patterns are matched correctly to allow Community Cloud developer tools to display correctly in Firefox ([#9849](https://github.com/streamlit/streamlit/pull/9849), [#9848](https://github.com/streamlit/streamlit/issues/9848)).
- ☠️ Bug fix: Corrected a performance and alignment problem with containers ([#9901](https://github.com/streamlit/streamlit/pull/9901), [#9456](https://github.com/streamlit/streamlit/issues/9456), [#9560](https://github.com/streamlit/streamlit/issues/9560)).
- 👻 Bug fix: `st.rerun` will raise an error if an invalid `scope` is passed to it ([#9911](https://github.com/streamlit/streamlit/pull/9911), [#9908](https://github.com/streamlit/streamlit/issues/9908)).
- 🦋 Bug fix: Dataframe toolbars show correctly in dialogs ([#9897](https://github.com/streamlit/streamlit/pull/9897), [#9461](https://github.com/streamlit/streamlit/issues/9461)).
- 🦀 Bug fix: `LinkColumn` regex for `display_text` uses the correct URI decoding ([#9895](https://github.com/streamlit/streamlit/pull/9895), [#9893](https://github.com/streamlit/streamlit/issues/9893)).
- 🦎 Bug fix: `st.dataframe` has correct type hinting when `on_selection="ignore"` ([#9898](https://github.com/streamlit/streamlit/pull/9898), [#9669](https://github.com/streamlit/streamlit/issues/9669)).
- 🐌 Bug fix: Padding is applied consistently for wide and centered layout mode ([#9882](https://github.com/streamlit/streamlit/pull/9882), [#9707](https://github.com/streamlit/streamlit/issues/9707)).
- 🕸️ Bug fix: `st.graphviz_chart` is displayed correctly when `use_container_width=True` ([#9867](https://github.com/streamlit/streamlit/pull/9867), [#9866](https://github.com/streamlit/streamlit/issues/9866)).
- 🦗 Bug fix: The overloaded definitions of `st.pills` and `st.segmented_control` use the correct selection-mode default ([#9801](https://github.com/streamlit/streamlit/pull/9801)). Thanks, [RubenVanEldik](https://github.com/RubenVanEldik)!
- 🦂 Bug fix: `st.text_area` (and other widgets) are correctly submitted in a form when using `Ctrl+Enter` ([#9847](https://github.com/streamlit/streamlit/pull/9847), [#9841](https://github.com/streamlit/streamlit/issues/9841)).
- 🦟 Bug Fix: `st.write` renders `DeltaGenerator` objects with [`st.help`](http://st.help) ([#9828](https://github.com/streamlit/streamlit/pull/9828), [#9827](https://github.com/streamlit/streamlit/issues/9827)).
- 🦠 Bug fix: `st.text_area` correctly matches the value in Session State when used with a key ([#9829](https://github.com/streamlit/streamlit/pull/9829), [#9825](https://github.com/streamlit/streamlit/issues/9825)).
- 🪰 Bug fix: `st.text_input` does not trigger a rerun when a user submits an unchanged value ([#9826](https://github.com/streamlit/streamlit/pull/9826)).
- 🪳 Bug fix: Improved styling for `st.exception` to fix overflow and incorrect padding ([#9818](https://github.com/streamlit/streamlit/pull/9818), [#9817](https://github.com/streamlit/streamlit/issues/9817), [#9816](https://github.com/streamlit/streamlit/issues/9816)).
- 🕷️ Bug fix: Large dataframe don't overflow and cover the dataframe toolbar in fullscreen mode ([#9803](https://github.com/streamlit/streamlit/pull/9803), [#9798](https://github.com/streamlit/streamlit/issues/9798)).
- 🐞 Bug fix: `st.audio_input` shows the correct time on recording in time zones with a half-hour offset ([#9791](https://github.com/streamlit/streamlit/pull/9791), [#9631](https://github.com/streamlit/streamlit/issues/9631)).
- 🐝 Bug fix: In iOS, `st.number_input` shows a number pad instead of a keyboard when in focus ([#9766](https://github.com/streamlit/streamlit/pull/9766), [#9763](https://github.com/streamlit/streamlit/issues/9763)).
- 🐜 Bug fix: Widget keys containing hyphens are correctly added to HTML classes in the DOM with an `st-key-` prefix ([#9793](https://github.com/streamlit/streamlit/pull/9793)).
- 🪲 Bug fix: Audio files created by `st.audio_input` include a timestamp to ensure unique file names ([#9768](https://github.com/streamlit/streamlit/pull/9768)).
- 🐛 Bug fix: Double slash URL pathnames do not create a 301 redirect ([#9754](https://github.com/streamlit/streamlit/pull/9754), [#9690](https://github.com/streamlit/streamlit/issues/9690)).

## **Version 1.40.0**

_Release date: November 6, 2024_

**Highlights**

- 💊 Introducing [`st.pills`](/develop/api-reference/widgets/st.pills) to create a single- or multi-select group of pill-buttons.
- 🎛️ Introducing [`st.segmented_control`](/develop/api-reference/widgets/st.segmented_control) to create a segmented button or button group.
- 🎤 Announcing the general availability of [`st.audio_input`](), a widget to let users record sound with their microphones.

**Notable Changes**

- ➡️ Markdown renders a limited set of typographical symbols (arrows and comparators).
- <img src="/logo.svg">{{ display: "inline-block", width: "1em" }} /&gt; You can use `:streamlit:` to render the Streamlit logo in [Markdown](/develop/api-reference/text/st.markdown).
- 🐍 [`st.text`](/develop/api-reference/text/st.text) wraps text and no longer uses monospace font.
- 🪣 You can set `use_container_width` for [`st.image`](/develop/api-reference/media/st.image). `use_column_width` is deprecated.
- 📅 [`st.date_input`](/develop/api-reference/widgets/st.date_input) infers the first day of the week from the user’s locale ([#9706](https://github.com/streamlit/streamlit/pull/9706), [#5215](https://github.com/streamlit/streamlit/issues/5215)).

**Other Changes**

- 🎶 Streamlit’s CLI tool accepts array values for configuration options ([#9577](https://github.com/streamlit/streamlit/pull/9577)).
- ⛓️ Static file serving supports symlinks ([#9147](https://github.com/streamlit/streamlit/pull/9147), [#9146](https://github.com/streamlit/streamlit/issues/9146)). Thanks, [link89](https://github.com/link89)!
- 🚀 Streamlit provides helpful links for deployment when an app is running locally ([#9681](https://github.com/streamlit/streamlit/pull/9681)).
- ↕️ The fullscreen button for charts matches with the dataframe toolbar ([#9721](https://github.com/streamlit/streamlit/pull/9721)).
- 🏃 The running-man icon has a brief delay before rendering to avoid an unnecessary flicker for fast running apps ([#9732](https://github.com/streamlit/streamlit/pull/9732)).
- 🖇️ The `ComponentRequestHandler` allows symlinks ([#9588](https://github.com/streamlit/streamlit/pull/9588)).
- 👆 Streamlit works with `pillow` version 11 ([#9742](https://github.com/streamlit/streamlit/pull/9742)). Thanks, [hauntsaninja](https://github.com/hauntsaninja)!
- 🗺️ Deck.gl was upgraded to version 9.0.33 ([#9636](https://github.com/streamlit/streamlit/pull/9636)).
- 🦠 Bug fix: `st.latex` stays center-aligned when using the `help` keyword argument ([#9698](https://github.com/streamlit/streamlit/pull/9698), [#9682](https://github.com/streamlit/streamlit/issues/9682)). Thanks, [emmagarr](https://github.com/emmagarr)!
- 🪰 Bug fix: Apps correctly access local storage on Android ([#9744](https://github.com/streamlit/streamlit/pull/9744), [#9740](https://github.com/streamlit/streamlit/issues/9740)).
- 🕷️ Bug fix: Cached class methods can be cleared ([#9642](https://github.com/streamlit/streamlit/pull/9642), [#9633](https://github.com/streamlit/streamlit/issues/9633)).
- 🐞 Bug fix: Streamlit clears fragment auto-reruns when a user changes pages. This prevents an invalid index ([#9617](https://github.com/streamlit/streamlit/pull/9617)).
- 🐝 Bug fix: `st.page_link` margins are correct ([#9625](https://github.com/streamlit/streamlit/pull/9625)).
- 🐜 Bug fix: Form widgets show submission instructions when in focus ([#9576](https://github.com/streamlit/streamlit/pull/9576), [#7079](https://github.com/streamlit/streamlit/issues/7079)).
- 🪲 Bug fix: `st.navigation` correctly reconciles `client.showSidebarNavigation` ([#9589](https://github.com/streamlit/streamlit/pull/9589), [#9581](https://github.com/streamlit/streamlit/issues/9581)).
- 🐛 Bug fix: `st.text_area` requires a minimum height of 68px which fits two lines ([#9561](https://github.com/streamlit/streamlit/pull/9561), [#9217](https://github.com/streamlit/streamlit/issues/9217)).
- 💅 Bug fix: Various styling fixes ([#9529](https://github.com/streamlit/streamlit/pull/9529), [#8131](https://github.com/streamlit/streamlit/issues/8131), [#9555](https://github.com/streamlit/streamlit/pull/9555), [#9496](https://github.com/streamlit/streamlit/issues/9496), [#9554](https://github.com/streamlit/streamlit/pull/9554), [#9349](https://github.com/streamlit/streamlit/issues/9349), [#7739](https://github.com/streamlit/streamlit/issues/7739)).

## **Version 1.39.0**

_Release date: October 1, 2024_

**Highlights**

- 🎤 Introducing [`st.experimental_audio_input`](/develop/api-reference/widgets/st.audio_input) to let users record with their microphones!
- 📍 [`st.pydeck_chart`](/develop/api-reference/charts/st.pydeck_chart#chart-selections) can return selection events!

**Notable Changes**

- 😃 [`st.button`](/develop/api-reference/widgets/st.button), [`st.download_button`](/develop/api-reference/widgets/st.download_button), [`st.form_submit_button`](/develop/api-reference/execution-flow/st.form_submit_button), [`st.link_button`](/develop/api-reference/widgets/st.link_button), and [`st.popover`](/develop/api-reference/layout/st.popover) each have a new parameter to add an icon.
- 🏢 [`st.logo`](/develop/api-reference/media/st.logo) has a new parameter to adjust the size of your logo.
- 🧭 [`st.navigation`](/develop/api-reference/navigation/st.navigation) lets you display an always-expanded or collapsible menu using a new `expanded` parameter.
- ↕️ You can set `height` and `width` for [`st.map`](/develop/api-reference/charts/st.map) and [`st.pydeck_chart`](/develop/api-reference/charts/st.pydeck_chart).
- ↩️ Form submission behavior can be configured with a new `enter_to_submit` parameter ([#9480](https://github.com/streamlit/streamlit/pull/9480), [#7538](https://github.com/streamlit/streamlit/issues/7538), [#9406](https://github.com/streamlit/streamlit/pull/9406), [#8042](https://github.com/streamlit/streamlit/issues/8042)).
- ⏱️ A new config option, `server.disconnectedSessionTTL`, lets you set a minimum time before a disconnected session is cleaned up ([#9179](https://github.com/streamlit/streamlit/pull/9179)).
- 🤹 Dataframes support multi-index headers ([#9483](https://github.com/streamlit/streamlit/pull/9483), [#6319](https://github.com/streamlit/streamlit/issues/6319)).

**Other Changes**

- 🔑 Widget keys appear as HTML classes in the DOM with an `st-key-` prefix ([#9295](https://github.com/streamlit/streamlit/pull/9295), [#5437](https://github.com/streamlit/streamlit/issues/5437), [#3888](https://github.com/streamlit/streamlit/issues/3888)).
- 🔍 The `StreamlitAPIException` class has been extended into more specific exceptions for some of the most common errors ([#9318](https://github.com/streamlit/streamlit/pull/9318)).
- 🗺️ `st.map` and `st.pydeck_chart` have a full-screen toggle that matches the dataframe toolbar.
- ⬆️ Frontend dependencies for Vega have been upgraded ([#9443](https://github.com/streamlit/streamlit/pull/9443), [#9438](https://github.com/streamlit/streamlit/issues/9438)).
- 🕵️ Streamlit is compatible with Watchdog version 5 ([#9354](https://github.com/streamlit/streamlit/pull/9354)). Thanks, [RubenVanEldik](https://github.com/RubenVanEldik)!
- 🔁 Streamlit is compatible with Tenacity version 9 ([#9348](https://github.com/streamlit/streamlit/pull/9348)).
- 🔢 Bug fix: Column configuration will override any text or number format from `pandas.Styler` ([#9538](https://github.com/streamlit/streamlit/pull/9538), [#7329](https://github.com/streamlit/streamlit/issues/7329), [#7977](https://github.com/streamlit/streamlit/issues/7977)).
- 🦋 Bug fix: Deck GL zoom button has the correct border radius ([#9536](https://github.com/streamlit/streamlit/pull/9536)).
- 🦐 Bug fix: Embedded apps have the correct padding to avoid hiding elements ([#9524](https://github.com/streamlit/streamlit/pull/9524), [#9341](https://github.com/streamlit/streamlit/issues/9341)).
- 🎨 Bug fix: The `st.multiselect` placeholder text has the correct color ([#9523](https://github.com/streamlit/streamlit/pull/9523), [#9514](https://github.com/streamlit/streamlit/issues/9514)).
- 🧹 Bug fix: `st.json` scrolls horizontally instead of overflowing its container ([#9521](https://github.com/streamlit/streamlit/pull/9521), [#9520](https://github.com/streamlit/streamlit/issues/9520)).
- 🌬️ Bug fix: Bokeh charts (temporarily) don't have a fullscreen button to prevent horizontal scrolling ([#9528](https://github.com/streamlit/streamlit/pull/9528), [#2358](https://github.com/streamlit/streamlit/issues/2358)).
- 🐡 Bug fix: Users are correctly redirected if they add a trailing slash to a page URL ([#9500](https://github.com/streamlit/streamlit/pull/9500), [#9127](https://github.com/streamlit/streamlit/issues/9127)).
- 📁 Bug fix: `st.Page` warns developers against using subdirectories in `url_path`, which is not supported ([#9499](https://github.com/streamlit/streamlit/pull/9499)).
- 💩 Bug fix: Streamlit correctly calculates dataframe widths to prevent Minified React error #185: Maximum update depth exceeded ([#9490](https://github.com/streamlit/streamlit/pull/9490), [#7949](https://github.com/streamlit/streamlit/issues/7949)).
- ☠️ Bug fix: ScriptRunContext handles the active script hash to avoid a race condition where widgets lose state in a multipage app ([#9441](https://github.com/streamlit/streamlit/pull/9441), [#9100](https://github.com/streamlit/streamlit/issues/9100)).
- 🪱 Bug fix: PDFs don't appear as plain text when hosted through static file serving in Streamlit ([#9439](https://github.com/streamlit/streamlit/pull/9439), [#9425](https://github.com/streamlit/streamlit/issues/9425)).
- 👻 Bug fix: Fragment elements don't disappear when used with custom components and callbacks ([#9381](https://github.com/streamlit/streamlit/pull/9381), [#9389](https://github.com/streamlit/streamlit/pull/9389), [#9372](https://github.com/streamlit/streamlit/issues/9372)).
- 👽 Bug fix: Streamlit watches the correct directory for file changes ([#9453](https://github.com/streamlit/streamlit/pull/9453), [#7467](https://github.com/streamlit/streamlit/issues/7467)).
- 🦀 Bug fix: The sidebar navigation uses page count to determine when to display a "show more" button for more consistent behavior ([#9394](https://github.com/streamlit/streamlit/pull/9394)).
- 🦎 Bug fix: The internal script hash is updated at the beginning of a script run instead of the end for correct page routing when a script run is interrupted ([#9408](https://github.com/streamlit/streamlit/pull/9408), [#8975](https://github.com/streamlit/streamlit/issues/8975)).
- 🐌 Bug fix: Bold formatting in headers is ignored ([#9395](https://github.com/streamlit/streamlit/pull/9395), [#4248](https://github.com/streamlit/streamlit/issues/4428)).
- 🕸️ Bug fix: Streamlit correctly identifies the MIME type of more files to prevent custom components from not rendering ([#9390](https://github.com/streamlit/streamlit/pull/9390), [#9365](https://github.com/streamlit/streamlit/issues/9365)). Thanks, [t0mdavid-m](https://github.com/t0mdavid-m)!
- 🦗 Bug fix: The `client.showSidebarNavigation` configuration option works correctly with `st.navigation` ([#9379](https://github.com/streamlit/streamlit/pull/9379)).
- 🦂 Bug fix: Streamlit uses `example.com` instead of `test.com` in a health check to avoid unnecessary warnings ([#9371](https://github.com/streamlit/streamlit/pull/9371)). Thanks, [wyattscarpenter](https://github.com/wyattscarpenter)!
- 🦟 Bug fix: `st.Page` will raise an error if it tries to initialize a page with an empty path ([#9374](https://github.com/streamlit/streamlit/pull/9374), [#8892](https://github.com/streamlit/streamlit/issues/8892)).
- 🦠 Bug fix: An unchanged `st.dialog` can be programmatically reopened after a user has dismissed it ([#9333](https://github.com/streamlit/streamlit/pull/9333), [#9323](https://github.com/streamlit/streamlit/issues/9323)).
- 🪰 Bug fix: Streamlit will not remove underscores from declared page titles in `st.Page` ([#9375](https://github.com/streamlit/streamlit/pull/9375), [#8890](https://github.com/streamlit/streamlit/issues/8890)).
- 🪳 Bug fix: `st.logo` does not flicker when switching pages ([#9361](https://github.com/streamlit/streamlit/pull/9361), [#8815](https://github.com/streamlit/streamlit/issues/8815)).
- 🕷️ Bug fix: `st.data_editor` allows users to re-add a row with the same index after deleting it ([#8864](https://github.com/streamlit/streamlit/pull/8864), [#8854](https://github.com/streamlit/streamlit/issues/8854)).
- 🐞 Bug fix: `st.logo` maintains its aspect ratio when resized to fit within the sidebar width ([#9368](https://github.com/streamlit/streamlit/pull/9368)).
- 🐝 Bug fix: Streamlit correctly removes `st.logo` if not called during a rerun ([#9337](https://github.com/streamlit/streamlit/pull/9337), [#9336](https://github.com/streamlit/streamlit/issues/9336)).
- 🐜 Bug fix: `st.logo` does not flicker when the sidebar changes its state ([#9338](https://github.com/streamlit/streamlit/pull/9338)).
- 🪲 Bug fix: Streamlit renders `st.balloons` and `st.snow` in a React Portal for improved rendering and compatibility with `st.dialog` ([#9335](https://github.com/streamlit/streamlit/pull/9335), [#9236](https://github.com/streamlit/streamlit/issues/9236)).
- 🐛 Bug fix: Option labels are cleanly truncated when `st.multiselect` is displayed in a narrow container ([#9334](https://github.com/streamlit/streamlit/pull/9334), [#8213](https://github.com/streamlit/streamlit/issues/8213)).

## **Version 1.38.0**

_Release date: August 27, 2024_

**Highlights**

- 📈 Streamlit natively supports more dataframe formats! Use dataframe and series objects from popular libraries like Dask, Modin, Numpy, pandas, Polars, PyArrow, Snowpark, Xarray, and more. Use database cursors compliant with the Python Database API Specification 2.0. Use anything that supports the Python dataframe interchange protocol. See the [docs](/develop/api-reference/data/st.dataframe).

**Notable Changes**

- ↔️ You can control the initial expansion state of [`st.json`](/develop/api-reference/data/st.json) elements.
- 🧑‍💻 You can choose to wrap lines in [`st.code`](/develop/api-reference/text/st.code).
- 🕵️ Streamlit supports Kubernetes style secrets so you can use Snowflake Snowpark Container Services secret format ([#9078](https://github.com/streamlit/streamlit/pull/9078)).
- ⤴️ Breaking change: We removed a patch that allows custom validators in `pydantic</img>

---

[← Previous](279-2025-release-notes.md) | [Index](index.md) | [Next →](index.md)
