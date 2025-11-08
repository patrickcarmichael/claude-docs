**Navigation:** [← Previous](./01-get-started-with-streamlit.md) | [Index](./index.md) | [Next →](./03-customize-colors-and-borders-in-your-streamlit-app.md)

---

# Define multipage apps with `st.Page` and `st.navigation`

Source: https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation


`st.Page` and `st.navigation` are the preferred commands for defining multipage apps. With these commands, you have flexibility to organize your project files and customize your navigation menu. Simply initialize `StreamlitPage` objects with `st.Page`, then pass those `StreamlitPage` objects to `st.navigation` in your entrypoint file (i.e. the file you pass to `streamlit run`).

This page assumes you understand the [Page terminology](/develop/concepts/multipage-apps/overview#page-terminology) presented in the overview.

## App structure

When using `st.navigation`, your entrypoint file acts like a page router. Each page is a script executed from your entrypoint file. You can define a page from a Python file or function. If you include elements or widgets in your entrypoint file, they become common elements between your pages. In this case, you can think of your entrypoint file like a picture frame around each of your pages.

You can only call `st.navigation` once per app run and you must call it from your entrypoint file. When a user selects a page in navigation (or is routed through a command like `st.switch_page`), `st.navigation` returns the selected page. You must manually execute that page with the `.run()` method. The following example is a two-page app where each page is defined by a Python file.

**Directory structure:**

```
your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py
```

**`streamlit_app.py`:**

```python
import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()
```

## Defining pages

`st.Page` lets you define a page. The first and only required argument defines your page source, which can be a Python file or function. When using Python files, your pages may be in a subdirectory (or superdirectory). The path to your page file must always be relative to the entrypoint file. Once you create your page objects, pass them to `st.navigation` to register them as pages in your app.

If you don't define your page title or URL pathname, Streamlit will infer them from the file or function name as described in the multipage apps [Overview](/develop/concepts/multipage-apps/overview#automatic-page-labels-and-urls). However, `st.Page` lets you configure them manually. Within `st.Page`, Streamlit uses `title` to set the page label and title. Additionaly, Streamlit uses `icon` to set the page icon and favicon. If you want to have a different page title and label, or different page icon and favicon, you can use `st.set_page_config` to change the page title and/or favicon. Just call `st.set_page_config` in your entrypoint file or in your page script. You can call `st.set_page_config` multiple times to additively configure your page. Use `st.set_page_config` in your entrypoint file to declare a default configuration, and call it within page scripts to override that default.

The following example uses `st.set_page_config` to set a page title and favicon consistently across pages. Each page will have its own label and icon in the navigation menu, but the browser tab will show a consistent title and favicon on all pages.

**Directory structure:**

```
your-repository/
├── create.py
├── delete.py
└── streamlit_app.py
```

**`streamlit_app.py`:**

```python
import streamlit as st

create_page = st.Page("create.py", title="Create entry", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
```

<div>{{ maxWidth: '564px', margin: 'auto' }}&gt;
<Image src="/images/mpa-v2-use-set-page-config.jpg"/>
</div>

---

# Creating multipage apps using the `pages/` directory

Source: https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory


The most customizable method for declaring multipage apps is using [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation). However, Streamlit also provides a frictionless way to create multipage apps where pages are automatically recognized and shown in a navigation widget inside your app's sidebar. This method uses the `pages/` directory.

This page assumes you understand the [Page terminology](/develop/concepts/multipage-apps/overview#page-terminology) presented in the overview.

## App structure

When you use the `pages/` directory, Streamlit identifies pages in your multipage app by directory structure and filenames. Your entrypoint file (the file you pass to `streamlit run`), is your app's homepage. When you have a `pages/` directory next to your entrypoint file, Streamlit will identify each Python file within it as a page. The following example has three pages. `your_homepage.py` is the entrypoint file and homepage.

```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```

Run your multipage app just like you would for a single-page app. Pass your entrypoint file to `streamlit run`.

```
streamlit run your_homepage.py
```

Only `.py` files in the `pages/` directory will be identified as pages. Streamlit ignores all other files in the `pages/` directory and its subdirectories. Streamlit also ignores Python files in subdirectories of `pages/`.

<Important>

If you call `st.navigation` in your app (in any session), Streamlit will switch to using the newer, Page-and-navigation multipage structure. In this case, the `pages/` directory will be ignored across all sessions. You will not be able to revert back to the `pages/` directory unless you restart you app.

</Important>

### How pages are sorted in the sidebar

See the overview to understand how Streamlit assigns [Automatic page labels and URLs](/develop/concepts/multipage-apps/overview#automatic-page-labels-and-urls) based on the `number`, `separator`, `identifier`, and `".py"` extension that constitute a filename.

The entrypoint file is always displayed first. The remaining pages are sorted as follows:

- Files that have a `number` appear before files without a `number`.
- Files are sorted based on the `number` (if any), followed by the `label` (if any).
- When files are sorted, Streamlit treats the `number` as an actual number rather than a string. So `03` is the same as `3`.

This table shows examples of filenames and their corresponding labels, sorted by the order in which they appear in the sidebar.

**Examples**:

| **Filename**              | **Rendered label** |
| :------------------------ | :----------------- |
| `1 - first page.py`       | first page         |
| `12 monkeys.py`           | monkeys            |
| `123.py`                  | 123                |
| `123_hello_dear_world.py` | hello dear world   |
| `_12 monkeys.py`          | 12 monkeys         |

<Tip>

Emojis can be used to make your page names more fun! For example, a file named `🏠_Home.py` will create a page titled "🏠 Home" in the sidebar. When adding emojis to filenames, it’s best practice to include a numbered prefix to make autocompletion in your terminal easier. Terminal-autocomplete can get confused by unicode (which is how emojis are represented).

</Tip>

## Notes and limitations

- Pages support run-on-save.
  - When you update a page while your app is running, this causes a rerun for users currently viewing that exact page.
  - When you update a page while your app is running, the app will not automatically rerun for users currently viewing a different page.
- While your app is running, adding or deleting a page updates the sidebar navigation immediately.
- [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) works at the page level.
  - When you set `title` or `favicon` using `st.set_page_config`, this applies to the current page only.
  - When you set `layout` using `st.set_page_config`, the setting will remain for the session until changed by another call to `st.set_page_config`. If you use `st.set_page_config` to set `layout`, it's recommended to call it on _all_ pages.
- Pages share the same Python modules globally:

  ```python
  # page1.py
  import foo
  foo.hello = 123

  # page2.py
  import foo
  st.write(foo.hello)  # If page1 already executed, this writes 123
  ```

- Pages share the same [st.session_state](/develop/concepts/architecture/session-state):

  ```python
  # page1.py
  import streamlit as st
  if "shared" not in st.session_state:
     st.session_state["shared"] = True

  # page2.py
  import streamlit as st
  st.write(st.session_state["shared"]) # If page1 already executed, this writes True
  ```

You now have a solid understanding of multipage apps. You've learned how to structure apps, define pages, and navigate between pages in the user interface. It's time to [create your first multipage app](/get-started/tutorials/create-a-multipage-app)! 🥳

---

# Working with widgets in multipage apps

Source: https://docs.streamlit.io/develop/concepts/multipage-apps/widgets


When you create a widget in a Streamlit app, Streamlit generates a widget ID and uses it to make your widget stateful. As your app reruns with user interaction, Streamlit keeps track of the widget's value by associating its value to its ID. In particular, a widget's ID depends on the page where it's created. If you define an identical widget on two different pages, then the widget will reset to its default value when you switch pages.

This guide explains three strategies to deal with the behavior if you'd like to have a widget remain stateful across all pages. If don't want a widget to appear on all pages, but you do want it to remain stateful when you navigate away from its page (and then back), Options 2 and 3 can be used. For detailed information about these strategies, see [Understanding widget behavior](/develop/concepts/architecture/widget-behavior).

## Option 1 (preferred): Execute your widget command in your entrypoint file

When you define your multipage app with `st.Page` and `st.navigation`, your entrypoint file becomes a frame of common elements around your pages. When you execute a widget command in your entrypoint file, Streamlit associates the widget to your entrypoint file instead of a particular page. Since your entrypoint file is executed in every app rerun, any widget in your entrypoint file will remain stateful as your users switch between pages.

This method does not work if you define your app with the `pages/` directory.

The following example includes a selectbox and slider in the sidebar that are rendered and stateful on all pages. The widgets each have an assigned key so you can access their values through Session State within a page.

**Directory structure:**

```
your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py
```

**`streamlit_app.py`:**

```python
import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])

st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()
```

## Option 2: Save your widget values into a dummy key in Session State

If you want to navigate away from a widget and return to it while keeping its value, or if you want to use the same widget on multiple pages, use a separate key in `st.session_state` to save the value independently from the widget. In this example, a temporary key is used with a widget. The temporary key uses an underscore prefix. Hence, `"_my_key"` is used as the widget key, but the data is copied to `"my_key"` to preserve it between pages.

```python
import streamlit as st

def store_value():
    # Copy the value to the permanent key
    st.session_state["my_key"] = st.session_state["_my_key"]

# Copy the saved value to the temporary key
st.session_state["_my_key"] = st.session_state["my_key"]
st.number_input("Number of filters", key="_my_key", on_change=store_value)
```

If this is functionalized to work with multiple widgets, it could look something like this:

```python
import streamlit as st

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

load_value("my_key")
st.number_input("Number of filters", key="_my_key", on_change=store_value, args=["my_key"])
```

## Option 3: Interrupt the widget clean-up process

When Streamlit gets to the end of an app run, it will delete the data for any widgets that were not rendered. This includes data for any widget not associated to the current page. However, if you re-save a key-value pair in an app run, Streamlit will not associate the key-value pair to any widget until you execute a widget command again with that key.

As a result, if you have the following code at the top of every page, any widget with the key `"my_key"` will retain its value wherever it's rendered (or not). Alternatively, if you are using `st.navigation` and `st.Page`, you can include this once in your entrypoint file before executing your page.

```python
if "my_key" in st.session_state:
    st.session_state.my_key = st.session_state.my_key
```

---

# App design concepts and considerations

Source: https://docs.streamlit.io/develop/concepts/design


<TileContainer layout="list">
<RefCard href="/develop/concepts/design/animate">
<h5>Animate and update elements</h5>

Understand how to create dynamic, animated content or update elements without rerunning your app.

</RefCard>
<RefCard href="/develop/concepts/design/buttons">
<h5>Button behavior and examples</h5>

Understand how buttons work with explanations and examples to avoid common mistakes.

</RefCard>
<RefCard href="/develop/concepts/design/dataframes">
<h5>Dataframes</h5>

Dataframes are a great way to display and edit data in a tabular format. Understand the UI and options available in Streamlit.

</RefCard>
<RefCard href="/develop/concepts/design/custom-classes">
<h5>Using custom Python classes in your Streamlit app</h5>

Understand the impact of defining your own Python classes within Streamlit's rerun model.

</RefCard>
<RefCard href="/develop/concepts/design/multithreading">
<h5>Multithreading</h5>

Understand how to use multithreading within Streamlit apps.

</RefCard>
<RefCard href="/develop/concepts/design/timezone-handling">
<h5>Working with timezones</h5>

Understand how to localize time to your users.

</RefCard>
</TileContainer>

---

# Animate and update elements

Source: https://docs.streamlit.io/develop/concepts/design/animate


Sometimes you display a chart or dataframe and want to modify it live as the app
runs (for example, in a loop). Some elements have built-in methods to allow you
to update them in-place without rerunning the app.

Updatable elements include the following:

- `st.empty` containers can be written to in sequence and will always show the last thing written. They can also be cleared with an
  additional `.empty()` called like a method.
- `st.dataframe`, `st.table`, and many chart elements can be updated with the `.add_rows()` method which appends data.
- `st.progress` elements can be updated with additional `.progress()` calls. They can also be cleared with a `.empty()` method call.
- `st.status` containers have an `.update()` method to change their labels, expanded state, and status.
- `st.toast` messages can be updated in place with additional `.toast()` calls.

## `st.empty` containers

`st.empty` can hold a single element. When you write any element to an `st.empty` container, Streamlit discards its previous content
displays the new element. You can also `st.empty` containers by calling `.empty()` as a method. If you want to update a set of elements, use
a plain container (`st.container()`) inside `st.empty` and write contents to the plain container. Rewrite the plain container and its
contents as often as desired to update your app's display.

## The `.add_rows()` method

`st.dataframe`, `st.table`, and all chart functions can be mutated using the `.add_rows()` method on their output. In the following example, we use `my_data_element = st.line_chart(df)`. You can try the example with `st.table`, `st.dataframe`, and most of the other simple charts by just swapping out `st.line_chart`. Note that `st.dataframe` only shows the first ten rows by default and enables scrolling for additional rows. This means adding rows is not as visually apparent as it is with `st.table` or the chart elements.

```python
import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")
```

---

# Button behavior and examples

Source: https://docs.streamlit.io/develop/concepts/design/buttons


## Summary

Buttons created with [`st.button`](/develop/api-reference/widgets/st.button) do not retain state. They return `True` on the script rerun resulting from their click and immediately return to `False` on the next script rerun. If a displayed element is nested inside `if st.button('Click me'):`, the element will be visible when the button is clicked and disappear as soon as the user takes their next action. This is because the script reruns and the button return value becomes `False`.

In this guide, we will illustrate the use of buttons and explain common misconceptions. Read on to see a variety of examples that expand on `st.button` using [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state). [Anti-patterns](#anti-patterns) are included at the end. Go ahead and pull up your favorite code editor so you can `streamlit run` the examples as you read. Check out Streamlit's [Basic concepts](/get-started/fundamentals/main-concepts) if you haven't run your own Streamlit scripts yet.

## When to use `if st.button()`

When code is conditioned on a button's value, it will execute once in response to the button being clicked and not again (until the button is clicked again).

Good to nest inside buttons:

- Transient messages that immediately disappear.
- Once-per-click processes that saves data to session state, a file, or
  a database.

Bad to nest inside buttons:

- Displayed items that should persist as the user continues.
- Other widgets which cause the script to rerun when used.
- Processes that neither modify session state nor write to a file/database.\*

\* This can be appropriate when disposable results are desired. If you
have a "Validate" button, that could be a process conditioned directly on a
button. It could be used to create an alert to say 'Valid' or 'Invalid' with no
need to keep that info.

## Common logic with buttons

### Show a temporary message with a button

If you want to give the user a quick button to check if an entry is valid, but not keep that check displayed as the user continues.

In this example, a user can click a button to check if their `animal` string is in the `animal_shelter` list. When the user clicks "**Check availability**" they will see "We have that animal!" or "We don't have that animal." If they change the animal in [`st.text_input`](/develop/api-reference/widgets/st.text_input), the script reruns and the message disappears until they click "**Check availability**" again.

```python
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
```

Note: The above example uses [magic](/develop/api-reference/write-magic/magic) to render the message on the frontend.

### Stateful button

If you want a clicked button to continue to be `True`, create a value in `st.session_state` and use the button to set that value to `True` in a callback.

```python
import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
```

### Toggle button

If you want a button to work like a toggle switch, consider using [`st.checkbox`](/develop/api-reference/widgets/st.checkbox). Otherwise, you can use a button with a callback function to reverse a boolean value saved in `st.session_state`.

In this example, we use `st.button` to toggle another widget on and off. By displaying [`st.slider`](/develop/api-reference/widgets/st.slider) conditionally on a value in `st.session_state`, the user can interact with the slider without it disappearing.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
```

Alternatively, you can use the value in `st.session_state` on the slider's `disabled` parameter.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

st.slider('Select a value', disabled=st.session_state.button)
```

### Buttons to continue or control stages of a process

Another alternative to nesting content inside a button is to use a value in `st.session_state` that designates the "step" or "stage" of a process. In this example, we have four stages in our script:

0. Before the user begins.
1. User enters their name.
2. User chooses a color.
3. User gets a thank-you message.

A button at the beginning advances the stage from 0 to 1. A button at the end resets the stage from 3 to 0. The other widgets used in stage 1 and 2 have callbacks to set the stage. If you have a process with dependant steps and want to keep previous stages visible, such a callback forces a user to retrace subsequent stages if they change an earlier widget.

```python
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage &gt;= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage &gt;= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage &gt;= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])
```

### Buttons to modify `st.session_state`

If you modify `st.session_state` inside of a button, you must consider where that button is within the script.

#### A slight problem

In this example, we access `st.session_state.name` both before and after the buttons which modify it. When a button ("**Jane**" or "**John**") is clicked, the script reruns. The info displayed before the buttons lags behind the info written after the button. The data in `st.session_state` before the button is not updated. When the script executes the button function, that is when the conditional code to update `st.session_state` creates the change. Thus, this change is reflected after the button.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'

if st.button('John'):
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])
```

#### Logic used in a callback

Callbacks are a clean way to modify `st.session_state`. Callbacks are executed as a prefix to the script rerunning, so the position of the button relative to accessing data is not important.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

def change_name(name):
    st.session_state['name'] = name

st.header(st.session_state['name'])

st.button('Jane', on_click=change_name, args=['Jane Doe'])
st.button('John', on_click=change_name, args=['John Doe'])

st.header(st.session_state['name'])
```

#### Logic nested in a button with a rerun

Although callbacks are often preferred to avoid extra reruns, our first 'John Doe'/'Jane Doe' example can be modified by adding [`st.rerun`](/develop/api-reference/execution-flow/st.rerun) instead. If you need to acces data in `st.session_state` before the button that modifies it, you can include `st.rerun` to rerun the script after the change has been committed. This means the script will rerun twice when a button is clicked.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.rerun()

st.header(st.session_state['name'])
```

### Buttons to modify or reset other widgets

When a button is used to modify or reset another widget, it is the same as the above examples to modify `st.session_state`. However, an extra consideration exists: you cannot modify a key-value pair in `st.session_state` if the widget with that key has already been rendered on the page for the current script run.

<Important>

Don't do this!

```python
import streamlit as st

st.text_input('Name', key='name')

# These buttons will error because their nested code changes
# a widget's state after that widget within the script.
if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')
```

</Important>

#### Option 1: Use a key for the button and put the logic before the widget

If you assign a key to a button, you can condition code on a button's state by using its value in `st.session_state`. This means that logic depending on your button can be in your script before that button. In the following example, we use the `.get()` method on `st.session_state` because the keys for the buttons will not exist when the script runs for the first time. The `.get()` method will return `False` if it can't find the key. Otherwise, it will return the value of the key.

```python
import streamlit as st

# Use the get method since the keys won't be in session_state
# on the first script run
if st.session_state.get('clear'):
    st.session_state['name'] = ''
if st.session_state.get('streamlit'):
    st.session_state['name'] = 'Streamlit'

st.text_input('Name', key='name')

st.button('Clear name', key='clear')
st.button('Streamlit!', key='streamlit')
```

#### Option 2: Use a callback

```python
import streamlit as st

st.text_input('Name', key='name')

def set_name(name):
    st.session_state.name = name

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])
```

#### Option 3: Use containers

By using [`st.container`](/develop/api-reference/layout/st.container) you can have widgets appear in different orders in your script and frontend view (webpage).

```python
import streamlit as st

begin = st.container()

if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')

# The widget is second in logic, but first in display
begin.text_input('Name', key='name')
```

### Buttons to add other widgets dynamically

When dynamically adding widgets to the page, make sure to use an index to keep the keys unique and avoid a `DuplicateWidgetID` error. In this example, we define a function `display_input_row` which renders a row of widgets. That function accepts an `index` as a parameter. The widgets rendered by `display_input_row` use `index` within their keys so that `display_input_row` can be executed multiple times on a single script rerun without repeating any widget keys.

```python
import streamlit as st

def display_input_row(index):
    left, middle, right = st.columns(3)
    left.text_input('First', key=f'first_{index}')
    middle.text_input('Middle', key=f'middle_{index}')
    right.text_input('Last', key=f'last_{index}')

if 'rows' not in st.session_state:
    st.session_state['rows'] = 0

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )
```

### Buttons to handle expensive or file-writing processes

When you have expensive processes, set them to run upon clicking a button and save the results into `st.session_state`. This allows you to keep accessing the results of the process without re-executing it unnecessarily. This is especially helpful for processes that save to disk or write to a database. In this example, we have an `expensive_process` that depends on two parameters: `option` and `add`. Functionally, `add` changes the output, but `option` does not`option` is there to provide a parameter

```python
import streamlit as st
import pandas as pd
import time

def expensive_process(option, add):
    with st.spinner('Processing...'):
        time.sleep(5)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
    return (df, add)

cols = st.columns(2)
option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
add = cols[1].number_input('Add a number', min_value=0, max_value=10)

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
if st.button('Process'):
    result = expensive_process(option, add)
    st.session_state.processed[option] = result
    st.write(f'Option {option} processed with add {add}')
    result[0]
```

Astute observers may think, "This feels a little like caching." We are only saving results relative to one parameter, but the pattern could easily be expanded to save results relative to both parameters. In that sense, yes, it has some similarities to caching, but also some important differences. When you save results in `st.session_state`, the results are only available to the current user in their current session. If you use [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) instead, the results are available to all users across all sessions. Furthermore, if you want to update a saved result, you have to clear all saved results for that function to do so.

## Anti-patterns

Here are some simplified examples of how buttons can go wrong. Be on the lookout for these common mistakes.

### Buttons nested inside buttons

```python
import streamlit as st

if st.button('Button 1'):
    st.write('Button 1 was clicked')
    if st.button('Button 2'):
        # This will never be executed.
        st.write('Button 2 was clicked')
```

### Other widgets nested inside buttons

```python
import streamlit as st

if st.button('Sign up'):
    name = st.text_input('Name')

    if name:
        # This will never be executed.
        st.success(f'Welcome {name}')
```

### Nesting a process inside a button without saving to session state

```python
import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if st.button('Get data'):
    df = pd.read_csv(file)
    # This display will go away with the user's next action.
    st.write(df)

if st.button('Save'):
    # This will always error.
    df.to_csv('data.csv')
```

---

# Dataframes

Source: https://docs.streamlit.io/develop/concepts/design/dataframes


Dataframes are a great way to display and edit data in a tabular format. Working with Pandas DataFrames and other tabular data structures is key to data science workflows. If developers and data scientists want to display this data in Streamlit, they have multiple options: `st.dataframe` and `st.data_editor`. If you want to solely display data in a table-like UI, [st.dataframe](/develop/api-reference/data/st.dataframe) is the way to go. If you want to interactively edit data, use [st.data_editor](/develop/api-reference/data/st.data_editor). We explore the use cases and advantages of each option in the following sections.

## Display dataframes with st.dataframe

Streamlit can display dataframes in a table-like UI via `st.dataframe` :

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
```

<Cloud height="300px" name="doc-dataframe-basic"/>

## `st.dataframe` UI features

`st.dataframe` provides additional functionality by using [glide-data-grid](https://github.com/glideapps/glide-data-grid) under the hood:

- **Column sorting**: To sort columns, select their headers, or select "**Sort ascending**" or "**Sort descending**" from the header menu (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# Multithreading in Streamlit

Source: https://docs.streamlit.io/develop/concepts/design/multithreading


Multithreading is a type of concurrency, which improves the efficiency of computer programs. It's a way for processors to multitask. Streamlit uses threads within its architecture, which can make it difficult for app developers to include their own multithreaded processes. Streamlit does not officially support multithreading in app code, but this guide provides information on how it can be accomplished.

## Prerequisites

- You should have a basic understanding of Streamlit's [architecture](/develop/concepts/architecture/architecture).

## When to use multithreading

Multithreading is just one type of concurrency. Multiprocessing and coroutines are other forms of concurrency. You need to understand how your code is bottlenecked to choose the correct kind of concurrency.

Multiprocessing is inherently parallel, meaning that resources are split and multiple tasks are performed simultaneously. Therefore, multiprocessing is helpful with compute-bound operations. In contrast, multithreading and coroutines are not inherently parallel and instead allow resource switching. This makes them good choices when your code is stuck _waiting_ for something, like an IO operation. AsyncIO uses coroutines and may be preferable with very slow IO operations. Threading may be preferable with faster IO operations. For a helpful guide to using AsyncIO with Streamlit, see this [Medium article by Sehmi-Conscious Thoughts](https://sehmi-conscious.medium.com/got-that-asyncio-feeling-f1a7c37cab8b).

Don't forget that Streamlit has [fragments](/develop/concepts/architecture/fragments) and [caching](/develop/concepts/architecture/caching), too! Use caching to avoid unnecessarily repeating computations or IO operations. Use fragments to isolate a bit of code you want to update separately from the rest of the app. You can set fragments to rerun at a specified interval, so they can be used to stream updates to a chart or table.

## Threads created by Streamlit

Streamlit creates two types of threads in Python:

- The **server thread** runs the Tornado web (HTTP + WebSocket) server.
- A **script thread** runs page code  one thread for each script run in a session.

When a user connects to your app, this creates a new session and runs a script thread to initialize the app for that user. As the script thread runs, it renders elements in the user's browser tab and reports state back to the server. When the user interacts with the app, another script thread runs, re-rendering the elements in the browser tab and updating state on the server.

This is a simplifed illustration to show how Streamlit works:

![Each user session uses script threads to communicate between the user's front end and the Streamlit server.](/images/concepts/Streamlit-threading.svg)

## `streamlit.errors.NoSessionContext`

Many Streamlit commands, including `st.session_state`, expect to be called from a script thread. When Streamlit is running as expected, such commands use the `ScriptRunContext` attached to the script thread to ensure they work within the intended session and update the correct user's view. When those Streamlit commands can't find any `ScriptRunContext`, they raise a `streamlit.errors.NoSessionContext` exception. Depending on your logger settings, you may also see a console message identifying a thread by name and warning, "missing ScriptRunContext!"

## Creating custom threads

When you work with IO-heavy operations like remote query or data loading, you may need to mitigate delays. A general programming strategy is to create threads and let them work concurrently. However, if you do this in a Streamlit app, these custom threads may have difficulty interacting with your Streamlit server.

This section introduces two patterns to let you create custom threads in your Streamlit app. These are only patterns to provide a starting point rather than complete solutions.

### Option 1: Do not use Streamlit commands within a custom thread

If you don't call Streamlit commands from a custom thread, you can avoid the problem entirely. Luckily Python threading provides ways to start a thread and collect its result from another thread.

In the following example, five custom threads are created from the script thread. After the threads are finished running, their results are displayed in the app.

```python
import streamlit as st
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.return_value = None

    def run(self):
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.return_value = f"start: {start_time}, end: {end_time}"


delays = [5, 4, 3, 2, 1]
threads = [WorkerThread(delay) for delay in delays]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
for i, thread in enumerate(threads):
    st.header(f"Thread {i}")
    st.write(thread.return_value)

st.button("Rerun")
```

<Cloud height="700px" name="doc-multithreading-no-st-commands-batched"/>

If you want to display results in your app as various custom threads finish running, use containers. In the following example, five custom threads are created similarly to the previous example. However, five containers are initialized before running the custom threads and a `while` loop is used to display results as they become available. Since the Streamlit `write` command is called outside of the custom threads, this does not raise an exception.

```python
import streamlit as st
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.return_value = None

    def run(self):
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.return_value = f"start: {start_time}, end: {end_time}"


delays = [5, 4, 3, 2, 1]
result_containers = []
for i, delay in enumerate(delays):
    st.header(f"Thread {i}")
    result_containers.append(st.container())

threads = [WorkerThread(delay) for delay in delays]
for thread in threads:
    thread.start()
thread_lives = [True] * len(threads)

while any(thread_lives):
    for i, thread in enumerate(threads):
        if thread_lives[i] and not thread.is_alive():
            result_containers[i].write(thread.return_value)
            thread_lives[i] = False
    time.sleep(0.5)

for thread in threads:
    thread.join()

st.button("Rerun")
```

<Cloud height="700px" name="doc-multithreading-no-st-commands-iterative"/>

### Option 2: Expose `ScriptRunContext` to the thread

If you want to call Streamlit commands from within your custom threads, you must attach the correct `ScriptRunContext` to the thread.

<Warning>

- This is not officially supported and may change in a future version of Streamlit.
- This may not work with all Streamlit commands.
- Ensure custom threads do not outlive the script thread owning the `ScriptRunContext`. Leaking of `ScriptRunContext` may cause security vulnerabilities, fatal errors, or unexpected behavior.

</Warning>

In the following example, a custom thread with `ScriptRunContext` attached can call `st.write` without a warning.

```python
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay, target):
        super().__init__()
        self.delay = delay
        self.target = target

    def run(self):
        # runs in custom thread, but can call Streamlit APIs
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.target.write(f"start: {start_time}, end: {end_time}")


delays = [5, 4, 3, 2, 1]
result_containers = []
for i, delay in enumerate(delays):
    st.header(f"Thread {i}")
    result_containers.append(st.container())

threads = [
    WorkerThread(delay, container)
    for delay, container in zip(delays, result_containers)
]
for thread in threads:
    add_script_run_ctx(thread, get_script_run_ctx())
    thread.start()

for thread in threads:
    thread.join()

st.button("Rerun")
```

<Cloud height="700px" name="doc-multithreading-expose-context"/>

---

# Using custom Python classes in your Streamlit app

Source: https://docs.streamlit.io/develop/concepts/design/custom-classes


If you are building a complex Streamlit app or working with existing code, you may have custom Python classes defined in your script. Common examples include the following:

- Defining a `@dataclass` to store related data within your app.
- Defining an `Enum` class to represent a fixed set of options or values.
- Defining custom interfaces to external services or databases not covered by [`st.connection`](/develop/api-reference/connections/st.connection).

Because Streamlit reruns your script after every user interaction, custom classes may be redefined multiple times within the same Streamlit session. This may result in unwanted effects, especially with class and instance comparisons. Read on to understand this common pitfall and how to avoid it.

We begin by covering some general-purpose patterns you can use for different types of custom classes, and follow with a few more technical details explaining why this matters. Finally, we go into more detail about [Using `Enum` classes](#using-enum-classes-in-streamlit) specifically, and describe a configuration option which can make them more convenient.

## Patterns to define your custom classes

### Pattern 1: Define your class in a separate module

This is the recommended, general solution. If possible, move class definitions into their own module file and import them into your app script. As long as you are not editing the files that define your app, Streamlit will not re-import those classes with each rerun. Therefore, if a class is defined in an external file and imported into your script, the class will not be redefined during the session, unless you are actively editing your app.

#### Example: Move your class definition

Try running the following Streamlit app where `MyClass` is defined within the page's script. `isinstance()` will return `True` on the first script run then return `False` on each rerun thereafter.

```python
# app.py
import streamlit as st

# MyClass gets redefined every time app.py reruns
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on the first run then False on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

If you move the class definition out of `app.py` into another file, you can make `isinstance()` consistently return `True`. Consider the following file structure:

```
myproject/
├── my_class.py
└── app.py
```

```python
# my_class.py
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
```

```python
# app.py
import streamlit as st
from my_class import MyClass # MyClass doesn't get redefined with each rerun

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

Streamlit only reloads code in imported modules when it detects the code has changed. Thus, if you are actively editing your app code, you may need to start a new session or restart your Streamlit server to avoid an undesirable class redefinition.

### Pattern 2: Force your class to compare internal values

For classes that store data (like [dataclasses](https://docs.python.org/3/library/dataclasses.html)), you may be more interested in comparing the internally stored values rather than the class itself. If you define a custom `__eq__` method, you can force comparisons to be made on the internally stored values.

#### Example: Define `__eq__`

Try running the following Streamlit app and observe how the comparison is `True` on the first run then `False` on every rerun thereafter.

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on the first run the False on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

Since `MyDataclass` gets redefined with each rerun, the instance stored in Session State will not be equal to any instance defined in a later script run. You can fix this by forcing a comparison of internal values as follows:

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def __eq__(self, other):
        # An instance of MyDataclass is equal to another object if the object
        # contains the same fields with the same values
        return (self.var1, self.var2) == (other.var1, other.var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

The default Python `__eq__` implementation for a regular class or `@dataclass` depends on the in-memory ID of the class or class instance. To avoid problems in Streamlit, your custom `__eq__` method should not depend the `type()` of `self` and `other`.

### Pattern 3: Store your class as serialized data

Another option for classes that store data is to define serialization and deserialization methods like `to_str` and `from_str` for your class. You can use these to store class instance data in `st.session_state` rather than storing the class instance itself. Similar to pattern 2, this is a way to force comparison of the internal data and bypass the changing in-memory IDs.

#### Example: Save your class instance as a string

Using the same example from pattern 2, this can be done as follows:

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def to_str(self):
        return f"{self.var1},{self.var2}"

    @classmethod
    def from_str(cls, serial_str):
        values = serial_str.split(",")
        var1 = int(values[0])
        var2 = float(values[1])
        return cls(var1, var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5).to_str()

# Displays True on every rerun
MyDataclass.from_str(st.session_state.my_dataclass) == MyDataclass(1, 5.5)

st.button("Rerun")
```

### Pattern 4: Use caching to preserve your class

For classes that are used as resources (database connections, state managers, APIs), consider using the cached singleton pattern. Use `@st.cache_resource` to decorate a `@staticmethod` of your class to generate a single, cached instance of the class. For example:

```python
import streamlit as st

class MyResource:
    def __init__(self, api_url: str):
        self._url = api_url

    @st.cache_resource(ttl=300)
    @staticmethod
    def get_resource_manager(api_url: str):
        return MyResource(api_url)

# This is cached until Session State is cleared or 5 minutes has elapsed.
resource_manager = MyResource.get_resource_manager("http://example.com/api/")
```

When you use one of Streamlit's caching decorators on a function, Streamlit doesn't use the function object to look up cached values. Instead, Streamlit's caching decorators index return values using the function's qualified name and module. So, even though Streamlit redefines `MyResource` with each script run, `st.cache_resource` is unaffected by this. `get_resource_manager()` will return its cached value with each rerun, until the value expires.

## Understanding how Python defines and compares classes

So what's really happening here? We'll consider a simple example to illustrate why this is a pitfall. Feel free to skip this section if you don't want to deal more details. You can jump ahead to learn about [Using `Enum` classes](#using-enum-classes-in-streamlit).

### Example: What happens when you define the same class twice?

Set aside Streamlit for a moment and think about this simple Python script:

```python
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
Marshall_B = Student(1, "Marshall")

# This is True (because a dataclass will compare two of its instances by value)
Marshall_A == Marshall_B

# Redefine the class
@dataclass
class Student:
    student_id: int
    name: str

Marshall_C = Student(1, "Marshall")

# This is False
Marshall_A == Marshall_C
```

In this example, the dataclass `Student` is defined twice. All three Marshalls have the same internal values. If you compare `Marshall_A` and `Marshall_B` they will be equal because they were both created from the first definition of `Student`. However, if you compare `Marshall_A` and `Marshall_C` they will not be equal because `Marshall_C` was created from the _second_ definition of `Student`. Even though both `Student` dataclasses are defined exactly the same, they have different in-memory IDs and are therefore different.

### What's happening in Streamlit?

In Streamlit, you probably don't have the same class written twice in your page script. However, the rerun logic of Streamlit creates the same effect. Let's use the above example for an analogy. If you define a class in one script run and save an instance in Session State, then a later rerun will redefine the class and you may end up comparing a `Mashall_C` in your rerun to a `Marshall_A` in Session State. Since widgets rely on Session State under the hood, this is where things can get confusing.

## How Streamlit widgets store options

Several Streamlit UI elements, such as `st.selectbox` or `st.radio`, accept multiple-choice options via an `options` argument. The user of your application can typically select one or more of these options. The selected value is returned by the widget function. For example:

```python
number = st.selectbox("Pick a number, any number", options=[1, 2, 3])
# number == whatever value the user has selected from the UI.
```

When you call a function like `st.selectbox` and pass an `Iterable` to `options`, the `Iterable` and current selection are saved into a hidden portion of [Session State](/develop/concepts/architecture/session-state) called the Widget Metadata.

When the user of your application interacts with the `st.selectbox` widget, the broswer sends the index of their selection to your Streamlit server. This index is used to determine which values from the original `options` list, _saved in the Widget Metadata from the previous page execution_, are returned to your application.

The key detail is that the value returned by `st.selectbox` (or similar widget function) is from an `Iterable` saved in Session State during a _previous_ execution of the page, NOT the values passed to `options` on the _current_ execution. There are a number of architectural reasons why Streamlit is designed this way, which we won't go into here. However, **this** is how we end up comparing instances of different classes when we think we are comparing instances of the same class.

### A pathological example

The above explanation might be a bit confusing, so here's a pathological example to illustrate the idea.

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
if "B" not in st.session_state:
    st.session_state.B = Student(1, "Marshall")
Marshall_B = st.session_state.B

options = [Marshall_A,Marshall_B]
selected = st.selectbox("Pick", options)

# This comparison does not return expected results:
selected == Marshall_A
# This comparison evaluates as expected:
selected == Marshall_B
```

As a final note, we used `@dataclass` in the example for this section to illustrate a point, but in fact it is possible to encounter these same problems with classes, in general. Any class which checks class identity inside of a comparison operatorsuch as `__eq__` or `__gt__`can exhibit these issues.

## Using `Enum` classes in Streamlit

The [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) class from the Python standard library is a powerful way to define custom symbolic names that can be used as options for `st.multiselect` or `st.selectbox` in place of `str` values.

For example, you might add the following to your streamlit page:

```python
from enum import Enum
import streamlit as st

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

selected_colors = set(st.multiselect("Pick colors", options=Color))

if selected_colors == {Color.RED, Color.GREEN}:
    st.write("Hooray, you found the color YELLOW!")
```

If you're using the latest version of Streamlit, this Streamlit page will work as it appears it should. When a user picks both `Color.RED` and `Color.GREEN`, they are shown the special message.

However, if you've read the rest of this page you might notice something tricky going on. Specifically, the `Enum` class `Color` gets redefined every time this script is run. In Python, if you define two `Enum` classes with the same class name, members, and values, the classes and their members are still considered unique from each other. This _should_ cause the above `if` condition to always evaluate to `False`. In any script rerun, the `Color` values returned by `st.multiselect` would be of a different class than the `Color` defined in that script run.

If you run the snippet above with Streamlit version 1.28.0 or less, you will not be able see the special message. Thankfully, as of version 1.29.0, Streamlit introduced a configuration option to greatly simplify the problem. That's where the enabled-by-default `enumCoercion` configuration option comes in.

### Understanding the `enumCoercion` configuration option

When `enumCoercion` is enabled, Streamlit tries to recognize when you are using an element like `st.multiselect` or `st.selectbox` with a set of `Enum` members as options.

If Streamlit detects this, it will convert the widget's returned values to members of the `Enum` class defined in the latest script run. This is something we call automatic `Enum` coercion.

This behavior is [configurable](/develop/concepts/configuration) via the `enumCoercion` setting in your Streamlit `config.toml` file. It is enabled by default, and may be disabled or set to a stricter set of matching criteria.

If you find that you still encounter issues with `enumCoercion` enabled, consider using the [custom class patterns](#patterns-to-define-your-custom-classes) described above, such as moving your `Enum` class definition to a separate module file.

---

# Working with timezones

Source: https://docs.streamlit.io/develop/concepts/design/timezone-handling


In general, working with timezones can be tricky. Your Streamlit app users are not necessarily in the same timezone as the server running your app. It is especially true of public apps, where anyone in the world (in any timezone) can access your app. As such, it is crucial to understand how Streamlit handles timezones, so you can avoid unexpected behavior when displaying `datetime` information.

## How Streamlit handles timezones

Streamlit always shows `datetime` information on the frontend with the same information as its corresponding `datetime` instance in the backend. I.e., date or time information does not automatically adjust to the users' timezone. We distinguish between the following two cases:

### **`datetime` instance without a timezone (naive)**

When you provide a `datetime` instance _without specifying a timezone_, the frontend shows the `datetime` instance without timezone information. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime

st.write(datetime(2020, 1, 10, 10, 30))
# Outputs: 2020-01-10 10:30:00
```

Users of the above app always see the output as `2020-01-10 10:30:00`.

### **`datetime` instance with a timezone**

When you provide a `datetime` instance _and specify a timezone_, the frontend shows the `datetime` instance in that same timezone. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00
```

Users of the above app always see the output as `2020-01-10 10:30:00-05:00`.

In both cases, neither the date nor time information automatically adjusts to the users' timezone on the frontend. What users see is identical to the corresponding `datetime` instance in the backend. It is currently not possible to automatically adjust the date or time information to the timezone of the users viewing the app.

<Note>

The legacy version of the `st.dataframe` has issues with timezones. We do not plan to roll out additional fixes or enhancements for the legacy dataframe. If you need stable timezone support, please consider switching to the arrow serialization by changing the [config setting](/develop/concepts/configuration), _config.dataFrameSerialization = "arrow"_.

</Note>

---

# Working with connections, secrets, and user authentication

Source: https://docs.streamlit.io/develop/concepts/connections


<TileContainer layout="list">
<RefCard href="/develop/concepts/connections/connecting-to-data">
<h5>Connecting to data</h5>

Connect your app to remote data or a third-party API.

</RefCard>
<RefCard href="/develop/concepts/connections/secrets-management">
<h5>Secrets managements</h5>

Set up your development environement and design your app to handle secrets securely.

</RefCard>
<RefCard href="/develop/concepts/connections/authentication">
<h5>Authentication and user information</h5>

Use an OpenID Connect provider to authenticate users and personalize your app.

</RefCard>
<RefCard href="/develop/concepts/connections/security-reminders">
<h5>Security reminders</h5>

Check out a few reminders to follow best practices and avoid security mistakes.

</RefCard>
</TileContainer>

---

# Connecting to data

Source: https://docs.streamlit.io/develop/concepts/connections/connecting-to-data


Most Streamlit apps need some kind of data or API access to be useful - either retrieving data to view or saving the results of some user action. This data or API is often part of some remote service, database, or other data source.

**Anything you can do with Python, including data connections, will generally work in Streamlit**. Streamlit's [tutorials](/develop/tutorials/databases) are a great starting place for many data sources. However:

- Connecting to data in a Python application is often tedious and annoying.
- There are specific considerations for connecting to data from streamlit apps, such as caching and secrets management.

**Streamlit provides [`st.connection()`](/develop/api-reference/connections/st.connection) to more easily connect your Streamlit apps to data and APIs with just a few lines of code**. This page provides a basic example of using the feature and then focuses on advanced usage.

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo"/>

## Basic usage

For basic startup and usage examples, read up on the relevant [data source tutorial](/develop/tutorials/databases). Streamlit has built-in connections to SQL dialects and Snowflake. We also maintain installable connections for [Cloud File Storage](https://github.com/streamlit/files-connection) and [Google Sheets](https://github.com/streamlit/gsheets-connection).

If you are just starting, the best way to learn is to pick a data source you can access and get a minimal example working from one of the pages above 👆. Here, we will provide an ultra-minimal usage example for using a SQLite database. From there, the rest of this page will focus on advanced usage.

### A simple starting point - using a local SQLite database

A [local SQLite database](https://sqlite.org/index.html) could be useful for your app's semi-persistent data storage.

<Note>

Community Cloud apps do not guarantee the persistence of local file storage, so the platform may delete data stored using this technique at any time.

</Note>

To see the example below running live, check out the interactive demo below:

<Cloud height="600px" name="experimental-connection" path="SQL"/>

#### Step 1: Install prerequisite library - SQLAlchemy

All SQLConnections in Streamlit use SQLAlchemy. For most other SQL dialects, you also need to install the driver. But the [SQLite driver ships with python3](https://docs.python.org/3/develop/sqlite3.html), so it isn't necessary.

```bash
pip install SQLAlchemy==1.4.0
```

#### Step 2: Set a database URL in your Streamlit secrets.toml file

Create a directory and file `.streamlit/secrets.toml` in the same directory your app will run from. Add the following to the file.

```toml
# .streamlit/secrets.toml

[connections.pets_db]
url = "sqlite:///pets.db"
```

#### Step 3: Use the connection in your app

The following app creates a connection to the database, uses it to create a table and insert some data, then queries the data back and displays it in a data frame.

```python
# streamlit_app.py

import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

In this example, we didn't set a `ttl=` value on the call to [`conn.query()`](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionquery), meaning Streamlit caches the result indefinitely as long as the app server runs.

Now, on to more advanced topics! 🚀

## Advanced topics

### Global secrets, managing multiple apps and multiple data stores

Streamlit [supports a global secrets file](/develop/concepts/connections/secrets-management) specified in the user's home directory, such as `~/.streamlit/secrets.toml`. If you build or manage multiple apps, we recommend using a global credential or secret file for local development across apps. With this approach, you only need to set up and manage your credentials in one place, and connecting a new app to your existing data sources is effectively a one-liner. It also reduces the risk of accidentally checking in your credentials to git since they don't need to exist in the project repository.

For cases where you have multiple similar data sources that you connect to during local development (such as a local vs. staging database), you can define different connection sections in your secrets or credentials file for different environments and then decide which to use at runtime. `st.connection` supports this with the _`name=env:<MY_NAME_VARIABLE>`_ syntax.

E.g., say I have a local and a staging MySQL database and want to connect my app to either at different times. I could create a global secrets file like this:

```toml
# ~/.streamlit/secrets.toml

[connections.local]
url = "mysql://me:****@localhost:3306/local_db"

[connections.staging]
url = "mysql://jdoe:******@staging.acmecorp.com:3306/staging_db"
```

Then I can configure my app connection to take its name from a specified environment variable

```python
# streamlit_app.py
import streamlit as st

conn = st.connection("env:DB_CONN", "sql")
df = conn.query("select * from mytable")
# ...
```

Now I can specify whether to connect to local or staging at runtime by setting the `DB_CONN` environment variable.

```bash
# connect to local
DB_CONN=local streamlit run streamlit_app.py

# connect to staging
DB_CONN=staging streamlit run streamlit_app.py
```

### Advanced SQLConnection configuration

The [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) configuration uses SQLAlchemy `create_engine()` function. It will take a single URL argument or attempt to construct a URL from several parts (username, database, host, and so on) using [`SQLAlchemy.engine.URL.create()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create).

Several popular SQLAlchemy dialects, such as Snowflake and Google BigQuery, can be configured using additional arguments to `create_engine()` besides the URL. These can be passed as `**kwargs` to the [st.connection](/develop/api-reference/connections/st.connection) call directly or specified in an additional secrets section called `create_engine_kwargs`.

E.g. snowflake-sqlalchemy takes an additional [`connect_args`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.connect_args) argument as a dictionary for configuration that isn’t supported in the URL. These could be specified as follows:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
url = "snowflake://<user_login_name>@<account_identifier>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
warehouse = "xxx"
role = "xxx"
```

```python
# streamlit_app.py

import streamlit as st

# url and connect_args from secrets.toml above are picked up and used here
conn = st.connection("snowflake", "sql")
# ...
```

Alternatively, this could be specified entirely in `**kwargs`.

```python
# streamlit_app.py

import streamlit as st

# secrets.toml is not needed
conn = st.connection(
    "snowflake",
    "sql",
    url = "snowflake://<user_login_name>@<account_identifier>/",
    connect_args = dict(
        authenticator = "externalbrowser",
        warehouse = "xxx",
        role = "xxx",
    )
)
# ...
```

You can also provide both kwargs and secrets.toml values, and they will be merged (typically, kwargs take precedence).

### Connection considerations in frequently used or long-running apps

By default, connection objects are cached without expiration using [`st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource). In most cases this is desired. You can do `st.connection('myconn', type=MyConnection, ttl=<N>)` if you want the connection object to expire after some time.

Many connection types are expected to be long-running or completely stateless, so expiration is unnecessary. Suppose a connection becomes stale (such as a cached token expiring or a server-side connection being closed). In that case, every connection has a `reset()` method, which will invalidate the cached version and cause Streamlit to recreate the connection the next time it is retrieved

Convenience methods like `query()` and `read()` will typically cache results by default using [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) without an expiration. When an app can run many different read operations with large results, it can cause high memory usage over time and results to become stale in a long-running app, the same as with any other usage of `st.cache_data`. For production use cases, we recommend setting an appropriate `ttl` on these read operations, such as `conn.read('path/to/file', ttl="1d")`. Refer to [Caching](/develop/concepts/architecture/caching) for more information.

For apps that could get significant concurrent usage, ensure that you understand any thread safety implications of your connection, particularly when using a connection built by a third party. Connections built by Streamlit should provide thread-safe operations by default.

### Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

<Cloud height="600px" name="experimental-connection" path="Build_your_own"/>

The typical steps are:

1. Declare the Connection class, extending [`ExperimentalBaseConnection`](/develop/api-reference/connections/st.connections.experimentalbaseconnection) with the type parameter bound to the underlying connection object:

   ```python
   from streamlit.connections import ExperimentalBaseConnection
   import duckdb

   class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection])
   ```

2. Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

   ```python
   def _connect(self, **kwargs) -&gt; duckdb.DuckDBPyConnection:
       if 'database' in kwargs:
           db = kwargs.pop('database')
       else:
           db = self._secrets['database']
       return duckdb.connect(database=db, **kwargs)
   ```

3. Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired)

### Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of st.connection is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:
   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):
   - Keyword arguments specified in the code
   - Streamlit secrets
   - data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in [Connection.reset()](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionreset) method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.</N></account_identifier></user_login_name></account_identifier></user_login_name></MY_NAME_VARIABLE>

---

# Secrets management

Source: https://docs.streamlit.io/develop/concepts/connections/secrets-management


Storing unencrypted secrets in a git repository is a bad practice. For applications that require access to sensitive credentials, the recommended solution is to store those credentials outside the repository - such as using a credentials file not committed to the repository or passing them as environment variables.

Streamlit provides native file-based secrets management to easily store and securely access your secrets in your Streamlit app.

<Note>

Existing secrets management tools, such as [dotenv files](https://pypi.org/project/python-dotenv/), [AWS credentials files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials), [Google Cloud Secret Manager](https://pypi.org/project/google-cloud-secret-manager/), or [Hashicorp Vault](https://www.vaultproject.io/use-cases/secrets-management), will work fine in Streamlit. We just add native secrets management for times when it's useful.

</Note>

## How to use secrets management

### Develop locally and set up secrets

Streamlit provides two ways to set up secrets locally using [TOML](https://toml.io/en/latest) format:

1. In a **global secrets file** at `~/.streamlit/secrets.toml` for macOS/Linux or `%userprofile%/.streamlit/secrets.toml` for Windows:

   ```toml
   # Everything in this section will be available as an environment variable
   db_username = "Jane"
   db_password = "mypassword"

   # You can also add other sections if you like.
   # The contents of sections as shown below will not become environment variables,
   # but they'll be easily accessible from within Streamlit anyway as we show
   # later in this doc.
   [my_other_secrets]
   things_i_like = ["Streamlit", "Python"]
   ```

   If you use the global secrets file, you don't have to duplicate secrets across several project-level files if multiple Streamlit apps share the same secrets.

2. In a **per-project secrets file** at `$CWD/.streamlit/secrets.toml`, where `$CWD` is the folder you're running Streamlit from. If both a global secrets file and a per-project secrets file exist, _secrets in the per-project file overwrite those defined in the global file_.

<Important>

Add this file to your `.gitignore` so you don't commit your secrets!

</Important>

### Use secrets in your app

Access your secrets by querying the `st.secrets` dict, or as environment variables. For example, if you enter the secrets from the section above, the code below shows you how to access them within your Streamlit app.

```python
import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
```

<Tip>

You can access `st.secrets` via attribute notation (e.g. `st.secrets.key`), in addition to key notation (e.g. `st.secrets["key"]`) — like [st.session_state](/develop/api-reference/caching-and-state/st.session_state).

</Tip>

You can even compactly use TOML sections to pass multiple secrets as a single attribute. Consider the following secrets:

```toml
[db_credentials]
username = "my_username"
password = "my_password"
```

Rather than passing each secret as attributes in a function, you can more compactly pass the section to achieve the same result. See the notional code below, which uses the secrets above:

```python
# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
```

### Error handling

Here are some common errors you might encounter when using secrets management.

- If a `.streamlit/secrets.toml` is created _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.
- If you try accessing a secret, but no `secrets.toml` file exists, Streamlit will raise a `FileNotFoundError` exception:
  <Image alt="Secrets management FileNotFoundError" src="/images/secrets-filenotfounderror.png"/>
- If you try accessing a secret that doesn't exist, Streamlit will raise a `KeyError` exception:

  ```python
  import streamlit as st

  st.write(st.secrets["nonexistent_key"])
  ```

    <Image alt="Secrets management KeyError" src="/images/secrets-keyerror.png"/>

### Use secrets on Streamlit Community Cloud

When you deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud), you can use the same secrets management workflow as you would locally. However, you'll need to also set up your secrets in the Community Cloud Secrets Management console. Learn how to do so via the Cloud-specific [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) documentation.

---

# User authentication and information

Source: https://docs.streamlit.io/develop/concepts/connections/authentication


Personalizing your app for your users is a great way to make your app more engaging.

User authentication and personalization unlocks a plethora of use cases for developers, including controls for admins, a personalized stock ticker, or a chatbot app with a saved history between sessions.

Before reading this guide, you should have a basic understanding of [secrets management](/develop/concepts/connections/secrets-management).

## OpenID Connect

Streamlit supports user authentication with OpenID Connect (OIDC), which is an authentication protocol built on top of OAuth 2.0. OIDC supports authentication, but not authorization: that is, OIDC connections tell you _who_ a user is (authentication), but don't give you the authority to _impersonate_ them (authorization). If you need to connect with a generic OAuth 2.0 provider or have your app to act on behalf of a user, consider using or creating a custom component.

Some popular OIDC providers are:

- [Google Identity](https://developers.google.com/identity/openid-connect/openid-connect)
- [Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings)
- [Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm)
- [Auth0](https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps)

## `st.login()`, `st.user`, and `st.logout()`

There are three commands involved with user authentication:

- [`st.login()`](/develop/api-reference/user/st.login) redirects the user to your identity provider. After they log in, Streamlit stores an identity cookie and then redirects them to the homepage of your app in a new session.
- [`st.user`](/develop/api-reference/user/st.user) is a dict-like object for accessing user information. It has a persistent attribute, `.is_logged_in`, which you can check for the user's login status. When they are logged in, other attributes are available per your identity provider's configuration.
- [`st.logout()`](/develop/api-reference/user/st.logout) removes the identity cookie from the user's browser and redirects them to the homepage of your app in a new session.

## User cookies and logging out

Streamlit checks for the identity cookie at the beginning of each new session. If a user logs in to your app in one tab and then opens a new tab, they will automatically be logged in to your app in the new tab. When you call `st.logout()` in a user session, Streamlit removes the identity cookie and starts a new session. This logs the user out from the current session. However, if they were logged in to other sessions already, they will remain logged in within those sessions. The information in `st.user` is updated at the beginning of a session (which is why `st.login()` and `st.logout()` both start new sessions after saving or deleting the identity cookie).

If a user closes your app without logging out, the identity cookie will expire after 30 days. This expiration time is not configurable and is not tied to any expiration time that may be returned in your user's identity token. If you need to prevent persistent authentication in your app, check the expiration information returned by the identity provider in `st.user` and manually call `st.logout()` when needed.

Streamlit does not modify or delete any cookies saved directly by your identity provider. For example, if you use Google as your identity provider and a user logs in to your app with Google, they will remain logged in to their Google account after they log out of your app with `st.logout()`.

## Setting up an identity provider

In order to use an identity provider, you must first configure your identity provider through an admin account. This typically involves setting up a client or application within the identity provider's system. Follow the documentation for your identity provider. As a general overview, an identity-provider client typically does the following:

- Manages the list of your users.
- Optional: Allows users to add themselves to your user list.
- Declares the set of attributes passed from each user account to the client (which is then passed to your Streamlit app).
- Only allows authentication requests to come from your Streamlit app.
- Redirects users back to your Streamlit app after they authenticate.

To configure your app, you'll need the following:

- Your app's URL
  For example, use `http://localhost:8501` for most local development cases.
- A redirect URL, which is your app's URL with the pathname `oauth2callback`
  For example, `http://localhost:8501/oauth2callback` for most local development cases.
- A cookie secret, which should be a strong, randomly generated string

After you use this information to configure your identity-provider client, you'll receive the following information from your identity provider:

- Client ID
- Client secret
- Server metadata URL

Examples for popular OIDC provider configurations are listed in the API reference for `st.login()`.

## Configure your OIDC connection in Streamlit

After you've configured your identity-provider client, you'll need to configure your Streamlit app, too. `st.login()` uses your app's `secrets.toml` file to configure your connection, similar to how `st.connection()` works.

Whether you have one OIDC provider or many, you'll need to have an `[auth]` dictionary in `secrets.toml`. You must declare `redirect_uri` and `cookie_secret` in the `[auth]` dictionary. These two values are shared between all OIDC providers in your app.

If you are only using one OIDC provider, you can put the remaining three properties (`client_id`, `client_secret`, and `server_metadata_url`) in `[auth]`. However, if you are using multiple providers, they should each have a unique name so you can declare their unique values in their own dictionaries. For example, if you name your connections `"connection_1"` and `"connection_2"`, put their remaining properties in dictionaries named `[auth.connection_1]` and `[auth.connection_2]`, respectively.

## A simple example

If you use Google Identity as your identity provider, a basic configuration for local development will look like the following TOML file:

`.streamlit/secrets.toml`:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

Make sure the port in `redirect_uri` matches the port you are using. The `cookie_secret` should be a strong, randomly generated secret. Both the `redirect_uri` and `cookie_secret` should have been entered into your client configuration on Google Cloud. You must copy the `client_id` and `client_secret` from Google Cloud after you create your client. For some identity providers, `server_metadata_url` may be unique to your client. However, for Google Cloud, a single URL is shared for OIDC clients.

In your app, create a simple login flow:

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login()
    st.stop()

if st.button("Log out"):
    st.logout()
st.markdown(f"Welcome! {st.user.name}")
```

When you use `st.stop()`, your script run ends as soon as the login button is displayed. This lets you avoid nesting your entire page within a conditional block. Additionally, you can use callbacks to simplify the code further:

```python
import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login)
    st.stop()

st.button("Log out", on_click=st.logout)
st.markdown(f"Welcome! {st.user.name}")
```

## Using multiple OIDC providers

If you use more than one OIDC provider, you'll need to declare a unique name for each. If you want to use Google Identity and Microsoft Entra ID as two providers for the same app, your configuration for local development will look like the following TOML file:

`.streamlit/secrets.toml`:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.google]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"
```

Microsoft's server metadata URL varies slightly depending on how your client is scoped. Replace `{tenant}` with the appropriate value described in Microsoft's documentation for [OpenID configuration](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri).

Your app code:

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login("google")
    if st.button("Log in with Microsoft"):
        st.login("microsoft")
    st.stop()

if st.button("Log out"):
    st.logout()
st.markdown(f"Welcome! {st.user.name}")
```

Using callbacks, this would look like:

```python
import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login, args=["google"])
    st.button("Log in with Microsoft", on_click=st.login, args=["microsoft"])
    st.stop()

st.button("Log out", on_click=st.logout)
st.markdown(f"Welcome! {st.user.name}")
```

## Passing keywords to your identity provider

To customize the behavior of your identity provider, you may need to declare additional keywords. For a complete list of OIDC parameters, see [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) and your provider's documentation. By default, Streamlit sets `scope="openid profile email"` and `prompt="select_account"`. You can change these and other OIDC parameters by passing a dictionary of settings to `client_kwargs`. `state` and `nonce`, which are used for security, are handled automatically and don't need to be specified.

For example,if you are using Auth0 and need to force users to log in every time, use `prompt="login"` as described in Auth0's [Customize Signup and Login Prompts](https://auth0.com/docs/customize/login-pages/universal-login/customize-signup-and-login-prompts). Your configuration will look like this:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
client_kwargs = { "prompt" = "login" }
```

<Note>
  Hosted Code environments such as GitHub Codespaces have additional security controls in place preventing the login redirect to be handled properly.
</Note>

---

# Security reminders

Source: https://docs.streamlit.io/develop/concepts/connections/security-reminders


## Protect your secrets

Never save usernames, passwords, or security keys directly in your code or commit them to your repository.

### Use environment variables

Avoid putting sensitve information in your code by using environment variables. Be sure to check out [`st.secrets`](/develop/concepts/connections/secrets-management). Research any platform you use to follow their security best practices. If you use Streamlit Community Cloud, [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code.

### Keep `.gitignore` updated

If you use any sensitive or private information during development, make sure that information is saved in separate files from your code. Ensure `.gitignore` is properly configured to prevent saving private information to your repository.

## Pickle warning

Streamlit's [`st.cache_data`](/develop/concepts/architecture/caching#stcache_data) and [`st.session_state`](/develop/concepts/architecture/session-state#serializable-session-state) implicitly use the `pickle` module, which is known to be insecure. It is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

- When using `st.cache_data`, anything your function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values. This warning also applies to [`st.cache`](/develop/api-reference/caching-and-state/st.cache) (deprecated).
- When the `runner.enforceSerializableSessionState` [configuration option](

---

# Custom Components

Source: https://docs.streamlit.io/develop/concepts/custom-components


Components are third-party Python modules that extend what's possible with Streamlit.

## How to use a Component

Components are super easy to use:

1. Start by finding the Component you'd like to use. Two great resources for this are:
   - The [Component gallery](https://streamlit.io/components)
   - [This thread](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634),
     by Fanilo A. from our forums.

2. Install the Component using your favorite Python package manager. This step and all following
   steps are described in your component's instructions.

   For example, to use the fantastic [AgGrid
   Component](https://github.com/PablocFonseca/streamlit-aggrid), you first install it with:

   ```python
   pip install streamlit-aggrid
   ```

3. In your Python code, import the Component as described in its instructions. For AgGrid, this step
   is:

   ```python
   from st_aggrid import AgGrid
   ```

4. ...now you're ready to use it! For AgGrid, that's:

   ```python
   AgGrid(my_dataframe)
   ```

## Making your own Component

If you're interested in making your own component, check out the following resources:

- [Create a Component](/develop/concepts/custom-components/create)
- [Publish a Component](/develop/concepts/custom-components/publish)
- [Components API](/develop/concepts/custom-components/intro)
- [Blog post for when we launched Components!](https://blog.streamlit.io/introducing-streamlit-components/)

Alternatively, if you prefer to learn using videos, our engineer Tim Conkling has put together some
amazing tutorials:

##### Video tutorial, part 1

<YouTube videoId="BuD3gILJW-Q"/>

##### Video tutorial, part 2

<YouTube videoId="QjccJl_7Jco"/>

---

# Intro to custom components

Source: https://docs.streamlit.io/develop/concepts/custom-components/intro


The first step in developing a Streamlit Component is deciding whether to create a static component (i.e. rendered once, controlled by Python) or to create a bi-directional component that can communicate from Python to JavaScript and back.

## Create a static component

If your goal in creating a Streamlit Component is solely to display HTML code or render a chart from a Python visualization library, Streamlit provides two methods that greatly simplify the process: `components.html()` and `components.iframe()`.

If you are unsure whether you need bi-directional communication, **start here first**!

### Render an HTML string

While [`st.text`](/develop/api-reference/text/st.text), [`st.markdown`](/develop/api-reference/text/st.markdown) and [`st.write`](/develop/api-reference/write-magic/st.write) make it easy to write text to a Streamlit app, sometimes you'd rather implement a custom piece of HTML. Similarly, while Streamlit natively supports [many charting libraries](/develop/api-reference/charts#chart-elements), you may want to implement a specific HTML/JavaScript template for a new charting library. [`components.html`](/develop/api-reference/custom-components/st.components.v1.html) works by giving you the ability to embed an iframe inside of a Streamlit app that contains your desired output.

**Example**

```python
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link crossorigin="anonymous" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" rel="stylesheet">
<script crossorigin="anonymous" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" src="https://code.jquery.com/jquery-3.2.1.slim.min.js"/>
<script crossorigin="anonymous" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"/>
<div id="accordion">
<div class="card">
<div class="card-header" id="headingOne">
<h5 class="mb-0">
<button aria-controls="collapseOne" aria-expanded="true" class="btn btn-link" data-target="#collapseOne" data-toggle="collapse">
            Collapsible Group Item #1
            </button>
</h5>
</div>
<div aria-labelledby="headingOne" class="collapse show" data-parent="#accordion" id="collapseOne">
<div class="card-body">
            Collapsible Group Item #1 content
          </div>
</div>
</div>
<div class="card">
<div class="card-header" id="headingTwo">
<h5 class="mb-0">
<button aria-controls="collapseTwo" aria-expanded="false" class="btn btn-link collapsed" data-target="#collapseTwo" data-toggle="collapse">
            Collapsible Group Item #2
            </button>
</h5>
</div>
<div aria-labelledby="headingTwo" class="collapse" data-parent="#accordion" id="collapseTwo">
<div class="card-body">
            Collapsible Group Item #2 content
          </div>
</div>
</div>
</div>
    """,
    height=600,
)
```

### Render an iframe URL

[`components.iframe`](/develop/api-reference/custom-components/st.components.v1.iframe) is similar in features to `components.html`, with the difference being that `components.iframe` takes a URL as its input. This is used for situations where you want to include an entire page within a Streamlit app.

**Example**

```python
import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://example.com", height=500)
```

## Create a bi-directional component

A bi-directional Streamlit Component has two parts:

1. A **frontend**, which is built out of HTML and any other web tech you like (JavaScript, React, Vue, etc.), and gets rendered in Streamlit apps via an iframe tag.
2. A **Python API**, which Streamlit apps use to instantiate and talk to that frontend

To make the process of creating bi-directional Streamlit Components easier, we've created a React template and a TypeScript-only template in the [Streamlit Component-template GitHub repo](https://github.com/streamlit/component-template). We also provide some [example Components](https://github.com/streamlit/component-template/tree/master/examples) in the same repo.

### Development Environment Setup

To build a Streamlit Component, you need the following installed in your development environment:

- Python 3.9 - Python 3.13
- Streamlit
- [nodejs](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

Clone the [component-template GitHub repo](https://github.com/streamlit/component-template), then decide whether you want to use the React.js (["template"](https://github.com/streamlit/component-template/tree/master/template)) or plain TypeScript (["template-reactless"](https://github.com/streamlit/component-template/tree/master/template-reactless)) template.

1. Initialize and build the component template frontend from the terminal:

   ```bash
   # React template
   template/my_component/frontend
   npm install    # Initialize the project and install npm dependencies
   npm run start  # Start the Vite dev server

   # or

   # TypeScript-only template
   template-reactless/my_component/frontend
   npm install    # Initialize the project and install npm dependencies
   npm run start  # Start the Vite dev server
   ```

2. _From a separate terminal_, run the Streamlit app (Python) that declares and uses the component:

   ```bash
   # React template
   cd template
   . venv/bin/activate # or similar to activate the venv/conda environment where Streamlit is installed
   pip install -e . # install template as editable package
   streamlit run my_component/example.py # run the example

   # or

   # TypeScript-only template
   cd template-reactless
   . venv/bin/activate # or similar to activate the venv/conda environment where Streamlit is installed
   pip install -e . # install template as editable package
   streamlit run my_component/example.py # run the example
   ```

After running the steps above, you should see a Streamlit app in your browser that looks like this:

![Streamlit Component Example App](/images/component_demo_example.png)

The example app from the template shows how bi-directional communication is implemented. The Streamlit Component displays a button (`Python → JavaScript`), and the end-user can click the button. Each time the button is clicked, the JavaScript front-end increments the counter value and passes it back to Python (`JavaScript → Python`), which is then displayed by Streamlit (`Python → JavaScript`).

### Frontend

Because each Streamlit Component is its own webpage that gets rendered into an `iframe`, you can use just about any web tech you'd like to create that web page. We provide two templates to get started with in the Streamlit [Components-template GitHub repo](https://github.com/streamlit/component-template/); one of those templates uses [React](https://reactjs.org/) and the other does not.

<Note>

Even if you're not already familiar with React, you may still want to check out the React-based
template. It handles most of the boilerplate required to send and receive data from Streamlit, and
you can learn the bits of React you need as you go.

If you'd rather not use React, please read this section anyway! It explains the fundamentals of
Streamlit ↔ Component communication.
</Note>

#### React

The React-based template is in `template/my_component/frontend/src/MyComponent.tsx`.

- `MyComponent.render()` is called automatically when the component needs to be re-rendered (just like in any React app)
- Arguments passed from the Python script are available via the `this.props.args` dictionary:

```python
# Send arguments in Python:
result = my_component(greeting="Hello", name="Streamlit")
```

```javascript
// Receive arguments in frontend:
let greeting = this.props.args["greeting"]; // greeting = "Hello"
let name = this.props.args["name"]; // name = "Streamlit"
```

- Use `Streamlit.setComponentValue()` to return data from the component to the Python script:

```javascript
// Set value in frontend:
Streamlit.setComponentValue(3.14);
```

```python
# Access value in Python:
result = my_component(greeting="Hello", name="Streamlit")
st.write("result = ", result) # result = 3.14
```

When you call `Streamlit.setComponentValue(new_value)`, that new value is sent to Streamlit, which then _re-executes the Python script from top to bottom_. When the script is re-executed, the call to `my_component(...)` will return the new value.

From a _code flow_ perspective, it appears that you're transmitting data synchronously with the frontend: Python sends the arguments to JavaScript, and JavaScript returns a value to Python, all in a single function call! But in reality this is all happening _asynchronously_, and it's the re-execution of the Python script that achieves the sleight of hand.

- Use `Streamlit.setFrameHeight()` to control the height of your component. By default, the React template calls this automatically (see `StreamlitComponentBase.componentDidUpdate()`). You can override this behavior if you need more control.
- There's a tiny bit of magic in the last line of the file: `export default withStreamlitConnection(MyComponent)` - this does some handshaking with Streamlit, and sets up the mechanisms for bi-directional data communication.

#### TypeScript-only

The TypeScript-only template is in `template-reactless/my_component/frontend/src/MyComponent.tsx`.

This template has much more code than its React sibling, in that all the mechanics of handshaking, setting up event listeners, and updating the component's frame height are done manually. The React version of the template handles most of these details automatically.

- Towards the bottom of the source file, the template calls `Streamlit.setComponentReady()` to tell Streamlit it's ready to start receiving data. (You'll generally want to do this after creating and loading everything that the Component relies on.)
- It subscribes to `Streamlit.RENDER_EVENT` to be notified of when to redraw. (This event won't be fired until `setComponentReady` is called)
- Within its `onRender` event handler, it accesses the arguments passed in the Python script via `event.detail.args`
- It sends data back to the Python script in the same way that the React template does—clicking on the "Click Me!" button calls `Streamlit.setComponentValue()`
- It informs Streamlit when its height may have changed via `Streamlit.setFrameHeight()`

#### Working with Themes

<Note>

Custom component theme support requires streamlit-component-lib version 1.2.0 or higher.

</Note>

Along with sending an `args` object to your component, Streamlit also sends
a `theme` object defining the active theme so that your component can adjust
its styling in a compatible way. This object is sent in the same message as
`args`, so it can be accessed via `this.props.theme` (when using the React
template) or `event.detail.theme` (when using the plain TypeScript template).

The `theme` object has the following shape:

```json
{
  "base": "lightORdark",
  "primaryColor": "someColor1",
  "backgroundColor": "someColor2",
  "secondaryBackgroundColor": "someColor3",
  "textColor": "someColor4",
  "font": "someFont"
}
```

The `base` option allows you to specify a preset Streamlit theme that your custom theme inherits from. Any theme config options not defined in your theme settings have their values set to those of the base theme. Valid values for `base` are `"light"` and `"dark"`.

Note that the theme object has fields with the same names and semantics as the
options in the "theme" section of the config options printed with the command
`streamlit config show`.

When using the React template, the following CSS variables are also set
automatically.

```css
--base
--primary-color
--background-color
--secondary-background-color
--text-color
--font
```

If you're not familiar with
[CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties),
the TLDR version is that you can use them like this:

```css
.mySelector {
  color: var(--text-color);
}
```

These variables match the fields defined in the `theme` object above, and
whether to use CSS variables or the theme object in your component is a matter
of personal preference.

#### Other frontend details

- Because you're hosting your component from a dev server (via `npm run start`), any changes you make should be automatically reflected in the Streamlit app when you save.
- If you want to add more packages to your component, run `npm add` to add them from within your component's `frontend/` directory.

```bash
npm add baseui
```

- To build a static version of your component, run `npm run export`. See [Prepare your Component](publish#prepare-your-component) for more information

### Python API

`components.declare_component()` is all that's required to create your Component's Python API:

```python
  import streamlit.components.v1 as components
  my_component = components.declare_component(
    "my_component",
    url="http://localhost:3001"
  )
```

You can then use the returned `my_component` function to send and receive data with your frontend code:

```python
# Send data to the frontend using named arguments.
return_value = my_component(name="Blackbeard", ship="Queen Anne's Revenge")

# `my_component`'s return value is the data returned from the frontend.
st.write("Value = ", return_value)
```

While the above is all you need to define from the Python side to have a working Component, we recommend creating a "wrapper" function with named arguments and default values, input validation and so on. This will make it easier for end-users to understand what data values your function accepts and allows for defining helpful docstrings.

Please see [this example](https://github.com/streamlit/component-template/blob/master/template/my_component/__init__.py#L41-L77) from the Components-template for an example of creating a wrapper function.

### Data serialization

#### Python → Frontend

You send data from Python to the frontend by passing keyword args to your Component's invoke function (that is, the function returned from `declare_component`). You can send the following types of data from Python to the frontend:

- Any JSON-serializable data
- `numpy.array`
- `pandas.DataFrame`

Any JSON-serializable data gets serialized to a JSON string, and deserialized to its JavaScript equivalent. `numpy.array` and `pandas.DataFrame` get serialized using [Apache Arrow](https://arrow.apache.org/) and are deserialized as instances of `ArrowTable`, which is a custom type that wraps Arrow structures and provides a convenient API on top of them.

Check out the [CustomDataframe](https://github.com/streamlit/component-template/tree/master/examples/CustomDataframe) and [SelectableDataTable](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable) Component example code for more context on how to use `ArrowTable`.

#### Frontend → Python

You send data from the frontend to Python via the `Streamlit.setComponentValue()` API (which is part of the template code). Unlike arg-passing from Python → frontend, **this API takes a single value**. If you want to return multiple values, you'll need to wrap them in an `Array` or `Object`.

Custom Components can send JSON-serializable data from the frontend to Python, as well as [Apache Arrow](http://arrow.apache.org/) `ArrowTable`s to represent dataframes.</link>

---

# Create a Component

Source: https://docs.streamlit.io/develop/concepts/custom-components/create


<Note>

If you are only interested in **using Streamlit Components**, then you can skip this section and
head over to the [Streamlit Components Gallery](https://streamlit.io/components) to find and install
components created by the community!

</Note>

Developers can write JavaScript and HTML "components" that can be rendered in Streamlit apps. Streamlit Components can receive data from, and also send data to, Streamlit Python scripts.

Streamlit Components let you expand the functionality provided in the base Streamlit package. Use Streamlit Components to create the needed functionality for your use-case, then wrap it up in a Python package and share with the broader Streamlit community!

**With Streamlit Components you can add new features to your app in the following ways:**

- Create your own components to use in place of existing Streamlit elements and widgets.
- Create completely new Streamlit elements and widgets by wrapping existing React.js, Vue.js, or other JavaScript widget toolkits.
- Render Python objects by constructing HTML representations and styling them to fit your app's theme.
- Create convenience functions to embed commonly-used web features like [GitHub gists and Pastebin](https://github.com/randyzwitch/streamlit-embedcode).

Check out these Streamlit Components tutorial videos by Streamlit engineer Tim Conkling to get started:

## Part 1: Setup and Architecture

<YouTube videoId="BuD3gILJW-Q"/>

## Part 2: Make a Slider Widget

<YouTube videoId="QjccJl_7Jco"/>

---

# Publish a Component

Source: https://docs.streamlit.io/develop/concepts/custom-components/publish


## Publish to PyPI

Publishing your Streamlit Component to [PyPI](https://pypi.org/) makes it easily accessible to Python users around the world. This step is completely optional, so if you won’t be releasing your component publicly, you can skip this section!

<Note>

For [static Streamlit Components](/develop/concepts/custom-components/intro#create-a-static-component), publishing a Python package to PyPI follows the same steps as the
[core PyPI packaging instructions](https://packaging.python.org/tutorials/packaging-projects/). A static Component likely contains only Python code, so once you have your
[setup.py](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py) file correct and
[generate your distribution files](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives), you're ready to
[upload to PyPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives).

[Bi-directional Streamlit Components](/develop/concepts/custom-components/intro#create-a-bi-directional-component) at minimum include both Python and JavaScript code, and as such, need a bit more preparation before they can be published on PyPI. The remainder of this page focuses on the bi-directional Component preparation process.

</Note>

### Prepare your Component

A bi-directional Streamlit Component varies slightly from a pure Python library in that it must contain pre-compiled frontend code. This is how base Streamlit works as well; when you `pip install streamlit`, you are getting a Python library where the HTML and frontend code contained within it have been compiled into static assets.

The [component-template](https://github.com/streamlit/component-template) GitHub repo provides the folder structure necessary for PyPI publishing. But before you can publish, you'll need to do a bit of housekeeping:

1. Give your Component a name, if you haven't already
   - Rename the `template/my_component/` folder to `template/<component>/`
   - Pass your component's name as the the first argument to `declare_component()`
2. Edit `MANIFEST.in`, change the path for recursive-include from `package/frontend/build *` to `<component>/frontend/build *`
3. Edit `setup.py`, adding your component's name and other relevant info
4. Create a release build of your frontend code. This will add a new directory, `frontend/build/`, with your compiled frontend in it:

   ```bash
   cd frontend
   npm run build
   ```

5. Pass the build folder's path as the `path` parameter to `declare_component`. (If you're using the template Python file, you can set `_RELEASE = True` at the top of the file):

   ```python
      import streamlit.components.v1 as components

      # Change this:
      # component = components.declare_component("my_component", url="http://localhost:3001")

      # To this:
      parent_dir = os.path.dirname(os.path.abspath(__file__))
      build_dir = os.path.join(parent_dir, "frontend/build")
      component = components.declare_component("new_component_name", path=build_dir)
   ```

### Build a Python wheel

Once you've changed the default `my_component` references, compiled the HTML and JavaScript code and set your new component name in `components.declare_component()`, you're ready to build a Python wheel:

1. Make sure you have the latest versions of setuptools, wheel, and twine

2. Create a wheel from the source code:

   ```bash
    # Run this from your component's top-level directory; that is,
    # the directory that contains `setup.py`
    python setup.py sdist bdist_wheel
   ```

### Upload your wheel to PyPI

With your wheel created, the final step is to upload to PyPI. The instructions here highlight how to upload to [Test PyPI](https://test.pypi.org/), so that you can learn the mechanics of the process without worrying about messing anything up. Uploading to PyPI follows the same basic procedure.

1. Create an account on [Test PyPI](https://test.pypi.org/) if you don't already have one
   - Visit [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) and complete the steps

   - Visit [https://test.pypi.org/manage/account/#api-tokens](https://test.pypi.org/manage/account/#api-tokens) and create a new API token. Don’t limit the token scope to a particular project, since you are creating a new project. Copy your token before closing the page, as you won’t be able to retrieve it again.

2. Upload your wheel to Test PyPI. `twine` will prompt you for a username and password. For the username, use **\_\_token\_\_**. For the password, use your token value from the previous step, including the `pypi-` prefix:

   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. Install your newly-uploaded package in a new Python project to make sure it works:

   ```bash
    python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
   ```

If all goes well, you're ready to upload your library to PyPI by following the instructions at [https://packaging.python.org/tutorials/packaging-projects/#next-steps](https://packaging.python.org/tutorials/packaging-projects/#next-steps).

Congratulations, you've created a publicly-available Streamlit Component!

## Promote your Component!

We'd love to help you share your Component with the Streamlit Community! To share it:

1. If you host your code on GitHub, add the tag `streamlit-component`, so that it's listed in the [GitHub **streamlit-component** topic](https://github.com/topics/streamlit-component):

   <Image caption="Add the streamlit-component tag to your GitHub repo" src="/images/component-tag.gif"/>

2. Post on the Streamlit Forum in [Show the Community!](https://discuss.streamlit.io/c/streamlit-examples/9). Use a post title similar to "New Component: `<your>name&gt;`, a new way to do X".
3. Add your component to the [Community Component Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634).
4. Tweet us at [@streamlit](https://twitter.com/streamlit) so that we can retweet your announcement for you.

Our [Components Gallery](https://streamlit.io/components) is updated approximately every month. Follow the above recommendations to maximize the liklihood of your component landing in our Components Gallery. Community Components featured in our docs are hand-curated on a less-regular basis. Popular components with many stars and good documentation are more likely to be selected.</your></component></component>

---

# Limitations of custom components

Source: https://docs.streamlit.io/develop/concepts/custom-components/limitations


## How do Streamlit Components differ from functionality provided in the base Streamlit package?

- Streamlit Components are wrapped up in an iframe, which gives you the ability to do whatever you want (within the iframe) using any web technology you like.

## What types of things aren't possible with Streamlit Components?

Because each Streamlit Component gets mounted into its own sandboxed iframe, this implies a few limitations on what is possible with Components:

- **Can't communicate with other Components**: Components can’t contain (or otherwise communicate with) other components, so Components cannot be used to build something like a grid layout.
- **Can't modify CSS**: A Component can’t modify the CSS that the rest of the Streamlit app uses, so you can't create something to put the app in dark mode, for example.
- **Can't add/remove elements**: A Component can’t add or remove other elements of a Streamlit app, so you couldn't make something to remove the app menu, for example.

## My Component seems to be blinking/stuttering...how do I fix that?

Currently, no automatic debouncing of Component updates is performed within Streamlit. The Component creator themselves can decide to rate-limit the updates they send back to Streamlit.

---

# Configure and customize your app

Source: https://docs.streamlit.io/develop/concepts/configuration


<TileContainer>
<RefCard href="/develop/concepts/configuration/options">
<h5>Configuration options</h5>

Understand the types of options available to you through Streamlit configuration.

</RefCard>
<RefCard href="/develop/concepts/configuration/https-support">
<h5>HTTPS support</h5>

Understand how to configure SSL and TLS for your Streamlit app.

</RefCard>
<RefCard href="/develop/concepts/configuration/serving-static-files">
<h5>Static file serving</h5>

Understand how to host files alongside your app to make them accessible by URL. Use this if you want to point to files with raw HTML.

</RefCard>
</TileContainer>

## Theming

<TileContainer>
<RefCard href="/develop/concepts/configuration/theming">
<h5>Theming</h5>

Understand how you can use theming configuration options to customize the appearance of your app.

</RefCard>
<RefCard href="/develop/concepts/configuration/theming-customize-colors-and-borders">
<h5>Customize colors and borders</h5>

Understand the configuration options for customizing your app's color scheme.

</RefCard>
<RefCard href="/develop/concepts/configuration/theming-customize-fonts">
<h5>Customize fonts</h5>

Understand the configuration options for customizing your app's font.

</RefCard>
</TileContainer>

---

# Working with configuration options

Source: https://docs.streamlit.io/develop/concepts/configuration/options


Streamlit provides four different ways to set configuration options. This list is in reverse order of precedence, i.e. command line flags take precedence over environment variables when the same configuration option is provided multiple times.

<Note>

If you change theme settings in `.streamlit/config.toml` _while_ the app is running, these changes will reflect immediately. If you change non-theme settings in `.streamlit/config.toml` _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.

</Note>

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:

   ```toml
   [server]
   port = 80
   ```

2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where
   `$CWD` is the folder you're running Streamlit from.

3. Through `STREAMLIT_*` **environment variables**, such as:

   ```bash
   export STREAMLIT_SERVER_PORT=80
   export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme
   ```

4. As **flags on the command line** when running `streamlit run`:

   ```bash
   streamlit run your_script.py --server.port 80
   ```

## Available options

All available configuration options are documented in [`config.toml`](/develop/api-reference/configuration/config.toml). These options may be declared in a TOML file, as environment variables, or as command line options.

When using environment variables to override `config.toml`, convert the variable (including its section header) to upper snake case and add a `STREAMLIT_` prefix. For example, `STREAMLIT_CLIENT_SHOW_ERROR_DETAILS` is equivalent to the following in TOML:

```toml
[client]
showErrorDetails = true
```

When using command line options to override `config.toml` and environment variables, use the same case as you would in the TOML file and include the section header as a period-separated prefix. For example, the command line option `--server.enableStaticServing true` is equivalent to the following:

```toml
[server]
enableStaticServing = true
```

## Telemetry

As mentioned during the installation process, Streamlit collects usage statistics. You can find out
more by reading our [Privacy Notice](https://streamlit.io/privacy-policy), but the high-level
summary is that although we collect telemetry data we cannot see and do not store information
contained in Streamlit apps.

If you'd like to opt out of usage statistics, add the following to your config file:

```toml
[browser]
gatherUsageStats = false
```

## Theming

You can change the base colors of your app using the `[theme]` section of the configuration system.
To learn more, see [Theming.](/develop/concepts/configuration/theming)

## View all configuration options

As described in [Command-line options](/develop/api-reference/cli), you can
view all available configuration options using:

```bash
streamlit config show
```

---

# HTTPS support

Source: https://docs.streamlit.io/develop/concepts/configuration/https-support


Many apps need to be accessed with SSL / [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol or `https://`.

We recommend performing SSL termination in a reverse proxy or load balancer for self-hosted and production use cases, not directly in the app. [Streamlit Community Cloud](/deploy/streamlit-community-cloud) uses this approach, and every major cloud and app hosting platform should allow you to configure it and provide extensive documentation. You can find some of these platforms in our [Deployment tutorials](/deploy/tutorials).

To terminate SSL in your Streamlit app, you must configure `server.sslCertFile` and `server.sslKeyFile`. Learn how to set config options in [Configuration](/develop/concepts/configuration).

## Details on usage

- The configuration value should be a local file path to a cert file and key file. These must be available at the time the app starts.
- Both `server.sslCertFile` and `server.sslKeyFile` must be specified. If only one is specified, your app will exit with an error.
- This feature will not work in Community Cloud. Community Cloud already serves your app with TLS.

<Warning>

In a production environment, we recommend performing SSL termination by the load balancer or the reverse proxy, not using this option. The use of this option in Streamlit has not gone through extensive security audits or performance tests.

</Warning>

## Example usage

```toml
# .streamlit/config.toml

[server]
sslCertFile = '/path/to/certchain.pem'
sslKeyFile = '/path/to/private.key'
```

---

# Static file serving

Source: https://docs.streamlit.io/develop/concepts/configuration/serving-static-files


Streamlit apps can host and serve small, static media files to support media embedding use cases that
won't work with the normal [media elements](/develop/api-reference/media).

To enable this feature, set `enableStaticServing = true` under `[server]` in your config file,
or environment variable `STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true`.

Media stored in the folder `./static/` relative to the running app file is served at path
`app/static/[filename]`, such as `http://localhost:8501/app/static/cat.png`.

## Details on usage

- Files with the following extensions will be served normally:
  - Common image types: `.jpg`, `.jpeg`, `.png`, `.gif`
  - Common font types: `.otf`, `.ttf`, `.woff`, `.woff2`
  - Other types: `.pdf`, `.xml`, `.json`
    Any other file will be sent with header `Content-Type:text/plain` which will cause browsers to render in plain text.
    This is included for security - other file types that need to render should be hosted outside the app.
- Streamlit also sets `X-Content-Type-Options:nosniff` for all files rendered from the static directory.
- For apps running on Streamlit Community Cloud:
  - Files available in the Github repo will always be served. Any files generated while the app is running,
    such as based on user interaction (file upload, etc), are not guaranteed to persist across user sessions.
  - Apps which store and serve many files, or large files, may run into resource limits and be shut down.

## Example usage

- Put an image `cat.png` in the folder `./static/`
- Add `enableStaticServing = true` under `[server]` in your `.streamlit/config.toml`
- Any media in the `./static/` folder is served at the relative URL like `app/static/cat.png`

```toml
# .streamlit/config.toml

[server]
enableStaticServing = true
```

```python
# app.py
import streamlit as st

with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")

```

Additional resources:

- [https://docs.streamlit.io/develop/concepts/configuration](https://docs.streamlit.io/develop/concepts/configuration)
- [https://static-file-serving.streamlit.app/](https://static-file-serving.streamlit.app/)

<Cloud height="1000px" name="static-file-serving"/>

---

# Theming overview

Source: https://docs.streamlit.io/develop/concepts/configuration/theming


In this guide, we provide an overview of theming and visual customization of Streamlit apps. Streamlit themes are defined using configuration options, which are most commonly defined in a `.streamlit/config.toml` file. For more information about setting configuration options, see [Working with configuration options](/develop/concepts/configuration/options). For a complete list of configuration options and definitions, see the API reference for [config.toml](/develop/api-reference/configuration/config.toml#theme).

You can configure a light and dark theme for your app that the user can change through the settings menu. The sidebar is separately
configurable from the main app for almost all theming options.

The following options can be set in the `[theme]` table of `config.toml` and can't be set separately in the sidebar, dark-theme, or
light-theme tables:

- **Base color scheme**: Set your custom theme to inherit from Streamlit's light or dark theme, or use an external theming TOML file.
- **Base font**: Set the base font weight and size. (This can be configured separately for heading and code font.)
- **Chart color**: Set series colors for Plotly, Altair, and Vega-Lite charts.
- **Sidebar border**: Set the visibility of the sidebar border.

The following options can be configured separately for the main body of your app and the sidebar. They can also be specified separately for
dark and light themes (`[theme.light]`, `[theme.light.sidebar]`, `[theme.dark]`, `[theme.dark.sidebar]`):

- **Font family**: Set the font family for body text, headings, and code.
- **Font style**: Set the weight and size of heading and code font, and set visibility of link underlines.
- **Text color**: Set the color of body, inline code, and link text.
- **Primary color**: Set the color of interactive elements and highlights.
- **Background color**: Set the color of app, widget, code block, and dataframe header backgrounds.
- **Border radius**: Set the roundness of elements and widgets.
- **Border color**: Set the color and visibility of element, widget, sidebar, and dataframe borders.
- **Basic color palette**: Set the color palette (red, orange, yellow, green, blue, violet, and gray/grey) for things like colored Markdown text and sparklines.

## Example themes

The following light theme is inspired by [Anthropic](https://docs.anthropic.com/en/home).
<Cloud height="500px" name="doc-theming-overview-anthropic-light-inspired"/>

The following dark theme is inspired by [Spotify](https://open.spotify.com/).
<Cloud height="500px" name="doc-theming-overview-spotify-inspired"/>

## Working with theme configuration during development

Most theme configuration options can be updated while an app is running. This makes it easy to iterate on your custom theme. If you change your app's primary color, save your `config.toml` file, and rerun your app, you will immediately see the new color. However, some configuration options (like `[[theme.fontFace]]`) require you to restart the Streamlit server to reflect the updates. If in doubt, when updating your app's configuration, stop the Streamlit server in your terminal and restart your app with the `streamlit run` command.

---


---

**Navigation:** [← Previous](./01-get-started-with-streamlit.md) | [Index](./index.md) | [Next →](./03-customize-colors-and-borders-in-your-streamlit-app.md)
