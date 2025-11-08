**Navigation:** [← Previous](./06-store-the-initial-value-of-widgets-in-session-stat.md) | [Index](./index.md) | [Next →](./08-build-an-llm-app-using-langchain.md)

---

# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "_pickle-serializable_", we mean calling `pickle.dumps(obj)` should not raise a [`PicklingError`](https://docs.python.org/3/develop/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#👇 results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png"/>
<Warning>

When `runner.enforceSerializableSessionState` is set to `true`, Session State implicitly uses the `pickle` module, which is known to be insecure. Ensure all data saved and retrieved from Session State is trusted because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

### Caveats and limitations

- Streamlit Session State is tied to a WebSocket connection. When a user reloads the browser tab or navigates using a Markdown link, the WebSocket connection and the associated Session State data are reset.
- Only the `st.form_submit_button` has a callback in forms. Other widgets inside a form are not allowed to have callbacks.
- `on_change` and `on_click` events are only supported on input type widgets.
- Modifying the value of a widget via the Session state API, after instantiating it, is not allowed and will raise a `StreamlitAPIException`. For example:

  ```python
  slider = st.slider(
      label='My Slider', min_value=1,
      max_value=10, value=5, key='my_slider')

  st.session_state.my_slider = 7

  # Throws an exception!
  ```

  ![state-modified-instantiated-exception](/images/state_modified_instantiated_exception.png)

- Setting the widget state via the Session State API and using the `value` parameter in the widget declaration is not recommended, and will throw a warning on the first run. For example:

  ```python
  st.session_state.my_slider = 7

  slider = st.slider(
      label='Choose a Value', min_value=1,
      max_value=10, value=5, key='my_slider')
  ```

  ![state-value-api-exception](/images/state_value_api_exception.png)

- Setting the state of button-like widgets: `st.button`, `st.download_button`, and `st.file_uploader` via the Session State API is not allowed. Such type of widgets are by default _False_ and have ephemeral _True_ states which are only valid for a single run. For example:

  ```python
  if 'my_button' not in st.session_state:
      st.session_state.my_button = True

  st.button('My button', key='my_button')

  # Throws an exception!
  ```

  ![state-button-exception](/images/state_button_exception.png)

---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context


* Function signature:

   st.context()



* Function signature:

   context.cookies



* Function signature:

   context.headers



* Function signature:

   context.ip_address



* Function signature:

   context.is_embedded



* Function signature:

   context.locale



* Function signature:

   context.theme

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | type | "light", "dark" |  | The theme type inferred from the background color of the app. |



* Function signature:

   context.timezone



* Function signature:

   context.timezone_offset



* Function signature:

   context.url



---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params

## st.query_params

`st.query_params` provides a dictionary-like interface to access query parameters in your app's URL and is available as of Streamlit 1.30.0. It behaves similarly to `st.session_state` with the notable exception that keys may be repeated in an app's URL. Handling of repeated keys requires special consideration as explained below.

`st.query_params` can be used with both key and attribute notation. For example, `st.query_params.my_key` and `st.query_params["my_key"]`. All keys and values will be set and returned as strings. When you write to `st.query_params`, key-value pair prefixed with `?` is added to the end of your app's URL. Each additional pair is prefixed with `` instead of `?`. Query parameters are cleared when navigating between pages in a multipage app.

For example, consider the following URL:

```javascript
https://your_app.streamlit.app/?first_key=1=two=true
```

The parameters in the URL above will be accessible in `st.query_params` as:

```python
{
    "first_key" : "1",
    "second_key" : "two",
    "third_key" : "true"
}
```

This means you can use those parameters in your app like this:

```python
# You can read query params using key notation
if st.query_params["first_key"] == "1":
    do_something()

# ...or using attribute notation
if st.query_params.second_key == "two":
    do_something_else()

# And you can change a param by just writing to it
st.query_params.first_key = 2  # This gets converted to str automatically
```

### Repeated keys

When a key is repeated in your app's URL (`?a=1=2=3`), dict-like methods will return only the last value. In this example, `st.query_params["a"]` returns `"3"`. To get all keys as a list, use the [`.get_all()`](/develop/api-reference/caching-and-state/st.query_params#stquery_paramsget_all) method shown below. To set the value of a repeated key, assign the values as a list. For example, `st.query_params.a = ["1", "2", "3"]` produces the repeated key given at the beginning of this paragraph.

### Limitation

`st.query_params` can't get or set embedding settings as described in [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options). `st.query_params.embed` and `st.query_params.embed_options` will raise an `AttributeError` or `StreamlitAPIException` when trying to get or set their values, respectively.


* Function signature:

   st.query_params.clear()

* Returns: None



* Function signature:

   st.query_params.from_dict(params)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | params | dict |  | A dictionary used to replace the current query parameters. |



* Function signature:

   st.query_params.get_all(key)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | key | str |  | The label of the query parameter in the URL. |

* Returns: List[str]

    A list of values associated to the given key. May return zero, one,
or multiple values.



* Function signature:

   st.query_params.to_dict()

* Returns: Dict[str,str]

    A dictionary of the current query parameters in the app's URL.



---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.experimental_get_query_params


* Function signature:

   st.experimental_get_query_params()

* Returns: dict

    The current query parameters as a dict. "Query parameters" are the part of the URL that comes
after the first "?".



---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.experimental_set_query_params


* Function signature:

   st.experimental_set_query_params(**query_params)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | **query_params | dict |  | The query parameters to set, as key-value pairs. |



---

# Connections and databases

Source: https://docs.streamlit.io/develop/api-reference/connections


## Setup your connection

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connection" size="half">
<Image>alt="screenshot" src="/images/api/connection.svg" /&gt;

<h4>Create a connection</h4>

Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</Image></RefCard>
</TileContainer>

## Built-in connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.snowflakeconnection" size="half">
<Image>alt="screenshot" src="/images/api/connections.SnowflakeConnection.svg" /&gt;

<h4>SnowflakeConnection</h4>

A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

</Image></RefCard>
<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">
<Image>alt="screenshot" src="/images/api/connections.SQLConnection.svg" /&gt;

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

</Image></RefCard>
</TileContainer>

## Third-party connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.baseconnection" size="half">
<h4>Connection base class</h4>

Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -&gt; MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>
</TileContainer>

## Secrets

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.secrets" size="half">
<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">
<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```

</YOUR_SECRET_KEY>
</RefCard>

## Deprecated classes

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.snowparkconnection" size="half">{true}&gt;

<h4>SnowparkConnection</h4>

A connection to Snowflake.

```python
conn = st.connection("snowpark")
```

</RefCard></TileContainer>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.secrets

## st.secrets

`st.secrets` provides a dictionary-like interface to access secrets stored in a `secrets.toml` file. It behaves similarly to `st.session_state`. `st.secrets` can be used with both key and attribute notation. For example, `st.secrets.your_key` and `st.secrets["your_key"]` refer to the same value. For more information about using `st.secrets`, see [Secrets management](/develop/concepts/connections/secrets-management).

### secrets.toml

By default, secrets can be saved globally or per-project. When both types of secrets are saved, Streamlit will combine the saved values but give precedence to per-project secrets if there are duplicate keys. For information on how to format and locate your `secrets.toml` file for your development environment, see [`secrets.toml`](/develop/api-reference/connections/secrets.toml).

### Configure secrets locations

You can configure where Streamlit searches for secrets through the configuration option, [`secrets.files`](/develop/api-reference/configuration/config.toml#secrets). With this option, you can list additional secrets locations and change the order of precedence. You can specify other TOML files or include Kubernetes style secret files.

#### Example

```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]

[database]
user = "your username"
password = "your password"
```

In your Streamlit app, the following values would be true:

```python
st.secrets["OpenAI_key"] == "your OpenAI key"
"sally" in st.secrets.whitelist
st.secrets["database"]["user"] == "your username"
st.secrets.database.password == "your password"
```

---

Source: https://docs.streamlit.io/develop/api-reference/connections/secrets.toml

## secrets.toml

`secrets.toml` is an optional file you can define for your working directory or global development environment. When `secrets.toml` is defined both globally and in your working directory, Streamlit combines the secrets and gives precendence to the working-directory secrets. For more information, see [Secrets management](/develop/concepts/connections/secrets-management).

### File location

To define your secrets locally or per-project, add `.streamlit/secrets.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be `~/.streamlit/secrets.toml`. For Windows, this will be `%userprofile%/.streamlit/secrets.toml`.

Optionally, you can change where Streamlit searches for secrets through the configuration option, [`secrets.files`](/develop/api-reference/configuration/config.toml#secrets).

### File format

`secrets.toml` is a [TOML](https://toml.io/en/) file.

#### Example

```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]

[database]
user = "your username"
password = "your password"
```

In your Streamlit app, the following values would be true:

```python
st.secrets["OpenAI_key"] == "your OpenAI key"
"sally" in st.secrets.whitelist
st.secrets["database"]["user"] == "your username"
st.secrets.database.password == "your password"
```

---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connection

<Tip>

This page only contains the `st.connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connection(name, type=None, max_entries=None, ttl=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | str |  | The connection name used for secrets lookup in secrets.toml. Streamlit uses secrets under [connections.] for the connection. type will be inferred if name is one of the following: "snowflake", "snowpark", or "sql". |
   | type | str, connection class, or None |  | The type of connection to create. This can be one of the following:  None (default): Streamlit will infer the connection type from name. If the type is not inferable from name, the type must be specified in secrets.toml instead. "snowflake": Streamlit will initialize a connection with SnowflakeConnection. "snowpark": Streamlit will initialize a connection with SnowparkConnection. This is deprecated. "sql": Streamlit will initialize a connection with SQLConnection. A string path to an importable class: This must be a dot-separated module path ending in the importable class. Streamlit will import the class and initialize a connection with it. The class must extend st.connections.BaseConnection. An imported class reference: Streamlit will initialize a connection with the referenced class, which must extend st.connections.BaseConnection. |
   | max_entries | int or None |  | The maximum number of connections to keep in the cache. If this is None (default), the cache is unbounded. Otherwise, when a new entry is added to a full cache, the oldest cached entry is removed. |
   | ttl | float, timedelta, or None |  | The maximum number of seconds to keep results in the cache. If this is None (default), cached results do not expire with time. |
   | **kwargs | any |  | Connection-specific keyword arguments that are passed to the connection's ._connect() method. **kwargs are typically combined with (and take precedence over) key-value pairs in secrets.toml. To learn more, see the specific connection's documentation. |

* Returns: Subclass of BaseConnection

    An initialized connection object of the specified type.



For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo"/>

---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowflakeconnection

<Tip>

This page only contains the `st.connections.SnowflakeConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, see [Connect Streamlit to Snowflake](/develop/tutorials/databases/snowflake) and [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connections.SnowflakeConnection(connection_name, **kwargs)



* Function signature:

   SnowflakeConnection.cursor()

* Returns: snowflake.connector.cursor.SnowflakeCursor

    A cursor object for the connection.



* Function signature:

   SnowflakeConnection.query(sql, *, ttl=None, show_spinner="Running `snowflake.query(...)`.", params=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | sql | str |  | The read-only SQL query to execute. |
   | ttl | float, int, timedelta or None |  | The maximum number of seconds to keep results in the cache. If this is None (default), cached results do not expire with time. |
   | show_spinner | boolean or string | to | Whether to enable the spinner. When a cached query is executed, no spinner is displayed because the result is immediately available. When a new query is executed, the default is to show a spinner with the message "Running snowflake.query(...)." If this is False, no spinner displays while executing the query. If this is a string, the string will be used as the message for the spinner. |
   | params | list, tuple, dict or None | s | List of parameters to pass to the Snowflake Connector for Python Cursor.execute() method. This connector supports binding data to a SQL statement using qmark bindings. For more information and examples, see the Snowflake Connector for Python documentation. This defaults to None. |

* Returns: pandas.DataFrame

    The result of running the query, formatted as a pandas DataFrame.



* Function signature:

   SnowflakeConnection.raw_connection

* Returns: snowflake.connector.connection.SnowflakeConnection

    The connection object.



* Function signature:

   SnowflakeConnection.reset()

* Returns: None



* Function signature:

   SnowflakeConnection.session()

* Returns: snowflake.snowpark.Session

    A new Snowpark session for this connection.



* Function signature:

   SnowflakeConnection.write_pandas(df, table_name, database=None, schema=None, chunk_size=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | df | pandas.DataFrame |  | The pandas.DataFrame object containing the data to be copied into the table. |
   | table_name | str |  | Name of the table where the data should be copied to. |
   | database | str |  | Name of the database containing the table. By default, the function writes to the database that is currently in use in the session.  Note If you specify this parameter, you must also specify the schema parameter. |
   | schema | str |  | Name of the schema containing the table. By default, the function writes to the table in the schema that is currently in use in the session. |
   | chunk_size | int |  | Number of elements to insert at a time. By default, the function inserts all elements in one chunk. |
   | **kwargs | Any |  | Additional keyword arguments for snowflake.connector.pandas_tools.write_pandas(). |

* Returns: tuple[bool, int, int]

    A tuple containing three values:

A boolean value that is True if the write was successful.
An integer giving the number of chunks of data that were copied.
An integer giving the number of rows that were inserted.



---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.sqlconnection

<Tip>

This page only contains the `st.connections.SQLConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connections.SQLConnection(connection_name, **kwargs)



* Function signature:

   SQLConnection.connect()

* Returns: sqlalchemy.engine.Connection

    A new SQLAlchemy connection object.



* Function signature:

   SQLConnection.query(sql, *, show_spinner="Running `sql.query(...)`.", ttl=None, index_col=None, chunksize=None, params=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | sql | str |  | The read-only SQL query to execute. |
   | show_spinner | boolean or string | to | Enable the spinner. The default is to show a spinner when there is a "cache miss" and the cached resource is being created. If a string, the value of the show_spinner param will be used for the spinner text. |
   | ttl | float, int, timedelta or None | None | The maximum number of seconds to keep results in the cache, or None if cached results should not expire. The default is None. |
   | index_col | str, list of str, or None | None | Column(s) to set as index(MultiIndex). Default is None. |
   | chunksize | int or None | None | If specified, return an iterator where chunksize is the number of rows to include in each chunk. Default is None. |
   | params | list, tuple, dict or None | None | List of parameters to pass to the execute method. The syntax used to pass parameters is database driver dependent. Check your database driver documentation for which of the five syntax styles, described in PEP 249 paramstyle, is supported. Default is None. |
   | **kwargs | dict |  | Additional keyword arguments are passed to pandas.read_sql. |

* Returns: pandas.DataFrame

    The result of running the query, formatted as a pandas DataFrame.



* Function signature:

   SQLConnection.reset()

* Returns: None



* Function signature:

   SQLConnection.driver

* Returns: str

    The name of the driver. For example, "pyodbc" or "psycopg2".



* Function signature:

   SQLConnection.engine

* Returns: sqlalchemy.engine.base.Engine

    The underlying SQLAlchemy Engine.



* Function signature:

   SQLConnection.session

* Returns: sqlalchemy.orm.Session

    A SQLAlchemy Session.



---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.baseconnection

<Tip>

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connections.BaseConnection(connection_name, **kwargs)



* Function signature:

   BaseConnection.reset()

* Returns: None



---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.experimental_connection

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>
<Tip>

This page only contains the `st.experimental_connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>
[Function 'streamlit.experimental_connection' not found]

---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowparkconnection

<Tip>

This page only contains the `st.connections.SnowparkConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connections.SnowparkConnection(connection_name, **kwargs)



---

Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.experimentalbaseconnection

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>
<Tip>

This page only contains information on the `st.connections.ExperimentalBaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

* Function signature:

   st.connections.ExperimentalBaseConnection(connection_name, **kwargs)



---

# Custom components

Source: https://docs.streamlit.io/develop/api-reference/custom-components


Streamlit custom components extend your app beyond built-in widgets with custom UI elements. V2 components offer better performance and multiple callbacks without iframes, while V1 components run in iframes with single callbacks.

## V2 custom components

### Backend (Python)

<TileContainer>
<RefCard href="/develop/api-reference/custom-components/st.components.v2.component">
<h4>Register</h4>

Register a custom component.

```python
my_component = st.components.v2.component(
    html=HTML,
    js=JS
)
my_component()
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/st.components.v2.types.bidicomponentcallable">
<h4>Mount</h4>

Mount a custom component.

```python
my_component = st.components.v2.component(
    html=HTML,
    js=JS
)
my_component()
```

</RefCard>
</TileContainer>

### Frontend (TypeScript)

<TileContainer>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib">
<h4>npm support code</h4>

Support code published through npm.

```bash
npm i @streamlit/component-v2-lib
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-component">
<h4>Component</h4>

Type alias for the component function.

```typescript
import { Component } from "@streamlit/component-v2-lib";
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-componentargs">
<h4>ComponentArgs</h4>

Type alias for the component arguments.

```typescript
import { ComponentArgs } from "@streamlit/component-v2-lib";
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-componentstate">
<h4>ComponentState</h4>

Type alias for the component state.

```typescript
import { ComponentState } from "@streamlit/component-v2-lib";
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-optionalcomponentcleanupfunction" size="two-third">
<h4>OptionalComponentCleanupFunction</h4>

Type alias for the component cleanup function.

```typescript
import { OptionalComponentCleanupFunction } from "@streamlit/component-v2-lib";
```

</RefCard>
</TileContainer>

## V1 custom components

<TileContainer>
<RefCard href="/develop/api-reference/custom-components/st.components.v1.declare_component">
<h4>Declare a component</h4>

Create and register a custom component.

```python
from st.components.v1 import declare_component
declare_component(
    "custom_slider",
    "/frontend",
)
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">
<h4>HTML</h4>

Display an HTML string in an iframe.

```python
from st.components.v1 import html
html(
    "<p>Foo bar.</p>"
)
```

</RefCard>
<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">
<h4>iframe</h4>

Load a remote URL in an iframe.

```python
from st.components.v1 import iframe
iframe(
    "docs.streamlit.io"
)
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v2.types.bidicomponentcallable


* Function signature:

   BidiComponentCallable(*args, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | key | str or None |  | An optional string to use as the unique key for the component instance. If this is omitted, an internal key is generated for the component instance based on its mounting parameters. No two Streamlit elements may have the same key. When a key is defined, the component's state is available in Session State via the key.  Note If you want to access this key in your component's frontend, you must pass it explicitly within the data parameter. The key parameter in BidiComponentCallable is not the same as the key property in ComponentArgs in the component's frontend code. The frontend key is automatically generated to be unique among all instances of all components and to avoid collisions with classes and IDs in the app's DOM. |
   | data | Any or None |  | Data to pass to the component. This can be one of the following:  A JSON-serializable object, like Dict[str, str | int] or List[str]. An Arrow-serializable object, like pandas.DataFrame. Raw bytes. A dictionary of JSON-serializable and Arrow-serializable objects. The dictionary's keys must be Python primitives.  Because this data is sent to the frontend, it must be serializable by one of the supported serialization methods (JSON, Arrow, or raw bytes). You can't pass arbitrary Python objects. Arrow-serialization is only supported at the top level of the data parameter or one level deep in a dictionary. Raw bytes are only supported at the top level. |
   | default | dict[str, Any] or None | state | Default state values for the component. Each key in the dictionary must correspond to a valid state attribute with an on__change callback. This callback can be empty, but must be included as a parameter when the component is mounted. Trigger values do not support manual defaults. All trigger and state values defined by an associated callback are initialized to None by default. |
   | width | "stretch", "content", or int |  | Width of the component. This can be one of the following:  "stretch" (default): The component is wrapped in a  with CSS style width: 100%;. "content": The component is wrapped in a  with CSS style width: fit-content;. An integer specifying the width in pixels: The component is wrapped in a  with the specified pixel width.  You are responsible for ensuring the component's inner HTML content is responsive to the  wrapper. |
   | height | "content", "stretch", or int |  | Height of the component. This can be one of the following:  "content" (default): The component is wrapped in a  with CSS style height: auto;. "stretch": The component is wrapped in a  with CSS style height: 100%;. An integer specifying the height in pixels: The component is wrapped in a  with the specified pixel height. If the component content is larger than the specified height, scrolling is enabled.   Note Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. If you want to disable scrolling for a fixed-height component, include an inner  wrapper in your component's HTML to control the overflow behavior.  You are responsible for ensuring the component's inner HTML content is responsive to the  wrapper. |
   | isolate_styles | bool |  | Whether to sandbox the component styles in a shadow root. If this is True (default), the component's HTML is mounted inside a shadow DOM and, in your component's JavaScript, parentElement returns a ShadowRoot. If this is False, the component's HTML is mounted directly into the app's DOM tree, and parentElement returns a regular HTMLElement. |
   | **callbacks | Callable or None |  | Callbacks with the naming pattern on__change for each state and trigger key. For example, if your component has a state key of "value" and a trigger key of "click", its callbacks can include on_value_change and on_click_change. Only names that follow this pattern are recognized. Custom components don't currently support callbacks with arguments. Callbacks are required for any state values defined in the default parameter. Otherwise, a callback is optional. To ensure your component's result always returns the expected attributes, you can pass empty callbacks like lambda: None. |

* Returns: BidiComponentResult

    Component state object that exposes state and trigger values.



* Function signature:

   BidiComponentResult

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | &amp;lt;state_keys&amp;gt; | Any |  | All state values from the component. State values are persistent across app reruns until explicitly changed. You can have multiple state keys as attributes. |
   | &amp;lt;trigger_keys&amp;gt; | Any |  | All trigger values from the component. Trigger values are transient and reset to None after one script run. You can have multiple trigger keys as attributes. |



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v2.component


* Function signature:

   st.components.v2.component(name, *, html=None, css=None, js=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | str |  | A short, descriptive identifier for the component. This is used internally by Streamlit to manage instances of the component. Component names must be unique across an app. The names of imported components are prefixed by their module name to avoid collisions. If you register multiple components with the same name, a warning is logged and the last-registered component is used. Because this can lead to unexpected behavior, ensure that component names are unique. If you intend to have multiple instances of a component in one app, avoid wrapping a component definition together with its mounting command so you don't re-register your component with each instance. |
   | html | str or None |  | Inline HTML markup for the component root. This can be one of the following strings:  Raw HTML. This doesn't require any , , or  tags; just provide the inner HTML. A path or glob to an HTML file, relative to the component's asset directory.  If any HTML depends on data passed at mount time, use a placeholder element and populate it via JavaScript. Alternatively, you can append a new element to the parent. For more information, see Example 2. html and js can't both be None. At least one of them must be provided. |
   | css | str or None |  | Inline CSS. This can be one of the following strings:  Raw CSS (without a  block). A path or glob to a CSS file, relative to the component's asset directory. |
   | js | str or None |  | Inline JavaScript. This can be one of the following strings:  Raw JavaScript (without a  block). A path or glob to a JS file, relative to the component's asset directory.  html and js can't both be None. At least one of them must be provided. |

* Returns: BidiComponentCallable

    The component's mounting command.
This callable accepts the component parameters like key and
data and returns a BidiComponentResult object with the
component's state. The mounting command can be included in a
user-friendly wrapper function to provide a simpler API. A mounting
command can be called multiple times in an app to create multiple
instances of the component.



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/component-v2-lib

## `@streamlit/component-v2-lib`

The [`@streamlit/component-v2-lib`](https://www.npmjs.com/package/@streamlit/component-v2-lib) package provides TypeScript type definitions and utilities for building Streamlit custom components using the v2 API.

### Installation

Install the package from npm:

```bash
npm i @streamlit/component-v2-lib
```

### Package Information

- **Package name**: `@streamlit/component-v2-lib`
- **Registry**: [npm](https://www.npmjs.com/package/@streamlit/component-v2-lib)
- **Purpose**: TypeScript type aliases and utilities for custom components v2

This package enables type-safe development when creating custom Streamlit components with modern JavaScript frameworks.

---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/component-v2-lib-component


* Function signature:

   Component&amp;lt;TComponentState extends ComponentState = ComponentState, TDataShape = unknown&amp;gt; = (componentArgs: ComponentArgs&amp;lt;TComponentState, TDataShape&amp;gt;) =&amp;gt; OptionalComponentCleanupFunction

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | componentArgs | ComponentArgs&amp;lt;TComponentState, TDataShape&amp;gt; |  | The inputs and utilities provided by Streamlit to your component. |

* Returns: OptionalComponentCleanupFunction

    An optional cleanup function that Streamlit will call when the component is unmounted.



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/component-v2-lib-componentargs


* Function signature:

   ComponentArgs&amp;lt;TComponentState = ComponentState, TDataShape = unknown,&amp;gt;

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | TDataShape |  | The data payload sent from Python through the component's mounting command. This is the primary input for your component, typed by the component author via the TDataShape generic. |
   | key | string |  | A stable identifier for this component instance generated by Streamlit. This key is independent from the key parameter passed to the component's mounting command in Python. This frontend key is automatically generated to be unique among all instances of all components and to avoid collisions with classes and IDs in the app's DOM. Important If a component is mounted without a key parameter in Python, and one of the parameters in the mounting command changes, then this frontend key may change between app runs. |
   | name | string |  | The component's name, as registered by Streamlit on the Python side. This is the same as the name parameter passed to st.components.v2.component. |
   | parentElement | HTMLElement or ShadowRoot |  | The host element for your component. Your HTML, JavaScript, and CSS are mounted inside this container. This is a ShadowRoot if isolate_styles is set to true in the component definition, otherwise it's an HTMLElement. |



* Function signature:

   setStateValue(name, value)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | string |  | The state key to set. If you are using TypeScript, this should be a key from TComponentState.To assign a value to a state key, in the component's mounting command in Python, an on__change callback isn't required. However, the presence of a callback will ensure that the state key is always present in the result. |
   | value | Any |  | The value to associate with the key. Type must match the corresponding property type in your TComponentState interface. |

* Returns: None



* Function signature:

   setTriggerValue(name, value)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | string |  | The trigger key to set. If you are using TypeScript, this should be a key from TComponentState.To assign a value to a trigger key, in the component's mounting command in Python, an on__change callback isn't required. However, the presence of a callback will ensure that the trigger key is always present in the result. |
   | value | Any |  | The value for this trigger. If you are using TypeScript, this should match the corresponding property type in your TComponentState interface. |

* Returns: None



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/component-v2-lib-componentstate


* Function signature:

   ComponentState = Record&amp;lt;string, unknown&amp;gt;



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/component-v2-lib-optionalcomponentcleanupfunction


* Function signature:

   OptionalComponentCleanupFunction = ComponentCleanupFunction | void



* Function signature:

   ComponentCleanupFunction = () =&gt; void



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.declare_component


* Function signature:

   st.components.v1.declare_component(name, path=None, url=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | str |  | A short, descriptive name for the component, like "slider". |
   | path | str, Path, or None |  | The path to serve the component's frontend files from. The path should be absolute. If path is None (default), Streamlit will serve the component from the location in url. Either path or url must be specified. If both are specified, then url will take precedence. |
   | url | str or None |  | The URL that the component is served from. If url is None (default), Streamlit will serve the component from the location in path. Either path or url must be specified. If both are specified, then url will take precedence. |

* Returns: CustomComponent

    A CustomComponent that can be called like a function.
Calling the component will create a new instance of the component
in the Streamlit app.



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html


* Function signature:

   st.components.v1.html(html, width=None, height=None, scrolling=False, *, tab_index=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | html | str |  | The HTML string to embed in the iframe. |
   | width | int | element | The width of the iframe in CSS pixels. By default, this is the app's default element width. |
   | height | int |  | The height of the frame in CSS pixels. By default, this is 150. |
   | scrolling | bool |  | Whether to allow scrolling in the iframe. If this False (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is True, Streamlit shows a scrollbar when the content is larger than the iframe. |
   | tab_index | int or None | behavior | Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation. This can be one of the following values:  None (default): Uses the browser's default behavior. -1: Removes the iframe from sequential navigation, but still allows it to be focused programmatically. 0: Includes the iframe in sequential navigation in the order it appears in the document but after all elements with a positive tab_index. Positive integer: Includes the iframe in sequential navigation. Elements are navigated in ascending order of their positive tab_index.  For more information, see the tabindex documentation on MDN. |



---

Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.iframe


* Function signature:

   st.components.v1.iframe(src, width=None, height=None, scrolling=False, *, tab_index=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | src | str |  | The URL of the page to embed. |
   | width | int | element | The width of the iframe in CSS pixels. By default, this is the app's default element width. |
   | height | int |  | The height of the frame in CSS pixels. By default, this is 150. |
   | scrolling | bool |  | Whether to allow scrolling in the iframe. If this False (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is True, Streamlit shows a scrollbar when the content is larger than the iframe. |
   | tab_index | int or None | behavior | Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation. This can be one of the following values:  None (default): Uses the browser's default behavior. -1: Removes the iframe from sequential navigation, but still allows it to be focused programmatically. 0: Includes the iframe in sequential navigation in the order it appears in the document but after all elements with a positive tab_index. Positive integer: Includes the iframe in sequential navigation. Elements are navigated in ascending order of their positive tab_index.  For more information, see the tabindex documentation on MDN. |



---

# Configuration

Source: https://docs.streamlit.io/develop/api-reference/configuration


<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">
<h4>Configuration file</h4>

Configures the default settings for your app.

```
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.get_option">
<h4>Get config option</h4>

Retrieve a single configuration option.

```python
st.get_option("theme.primaryColor")
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_option">
<h4>Set config option</h4>

Set a single configuration option. (This is very limited.)

```python
st.set_option("deprecation.showPyplotGlobalUse", False)
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">
<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/configuration/config.toml

## config.toml

`config.toml` is an optional file you can define for your working directory or global development environment. When `config.toml` is defined both globally and in your working directory, Streamlit combines the configuration options and gives precedence to the working-directory configuration. Additionally, you can use environment variables and command-line options to override additional configuration options. For more information, see [Configuration options](/develop/concepts/configuration/options).

### File location

To define your configuration locally or per-project, add `.streamlit/config.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be `~/.streamlit/config.toml`. For Windows, this will be `%userprofile%/.streamlit/config.toml`.

### File format

`config.toml` is a [TOML](https://toml.io/en/) file.

#### Example

```toml
[client]
showErrorDetails = "none"

[theme]
primaryColor = "#F63366"
backgroundColor = "black"
```

### Available configuration options

Below are all the sections and options you can have in your `.streamlit/config.toml` file. To see all configurations, use the following command in your terminal or CLI:

```bash
streamlit config show
```

#### Global

```toml
[global]

# By default, Streamlit displays a warning when a user sets both a widget
# default value in the function defining the widget and a widget value via
# the widget's key in `st.session_state`.
#
# If you'd like to turn off this warning, set this to True.
#
# Default: false
disableWidgetStateDuplicationWarning = false

# If True, will show a warning when you run a Streamlit-enabled script
# via "python my_script.py".
#
# Default: true
showWarningOnDirectExecution = true
```

#### Logger

```toml
[logger]

# Level of logging for Streamlit's internal logger: "error", "warning",
# "info", or "debug".
#
# Default: "info"
level = "info"

# String format for logging messages. If logger.datetimeFormat is set,
# logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`.
#
# See Python's documentation for available attributes:
# https://docs.python.org/3/library/logging.html#formatter-objects
#
# Default: "%(asctime)s %(message)s"
messageFormat = "%(asctime)s %(message)s"
```

#### Client

```toml
[client]

# Controls whether uncaught app exceptions and deprecation warnings
# are displayed in the browser. This can be one of the following:
#
# - "full"       : In the browser, Streamlit displays app deprecation
#                  warnings and exceptions, including exception types,
#                  exception messages, and associated tracebacks.
# - "stacktrace" : In the browser, Streamlit displays exceptions,
#                  including exception types, generic exception messages,
#                  and associated tracebacks. Deprecation warnings and
#                  full exception messages will only print to the
#                  console.
# - "type"       : In the browser, Streamlit displays exception types and
#                  generic exception messages. Deprecation warnings, full
#                  exception messages, and associated tracebacks only
#                  print to the console.
# - "none"       : In the browser, Streamlit displays generic exception
#                  messages. Deprecation warnings, full exception
#                  messages, associated tracebacks, and exception types
#                  will only print to the console.
# - True         : This is deprecated. Streamlit displays "full"
#                  error details.
# - False        : This is deprecated. Streamlit displays "stacktrace"
#                  error details.
#
# Default: "full"
showErrorDetails = "full"

# Change the visibility of items in the toolbar, options menu,
# and settings dialog (top right of the app).
#
# Allowed values:
# - "auto"      : Show the developer options if the app is accessed through
#                 localhost or through Streamlit Community Cloud as a developer.
#                 Hide them otherwise.
# - "developer" : Show the developer options.
# - "viewer"    : Hide the developer options.
# - "minimal"   : Show only options set externally (e.g. through
#                 Streamlit Community Cloud) or through st.set_page_config.
#                 If there are no options left, hide the menu.
#
# Default: "auto"
toolbarMode = "auto"

# Controls whether to display the default sidebar page navigation in a
# multi-page app. This only applies when app's pages are defined by the
# `pages/` directory.
#
# Default: true
showSidebarNavigation = true
```

#### Runner

```toml
[runner]

# Allows you to type a variable or string by itself in a single line of
# Python code to write it to the app.
#
# Default: true
magicEnabled = true

# Handle script rerun requests immediately, rather than waiting for
# script execution to reach a yield point.
#
# This makes Streamlit much more responsive to user interaction, but it
# can lead to race conditions in apps that mutate session_state data
# outside of explicit session_state assignment statements.
#
# Default: true
fastReruns = true

# Raise an exception after adding unserializable data to Session State.
#
# Some execution environments may require serializing all data in Session
# State, so it may be useful to detect incompatibility during development,
# or when the execution environment will stop supporting it in the future.
#
# Default: false
enforceSerializableSessionState = false

# Adjust how certain 'options' widgets like radio, selectbox, and
# multiselect coerce Enum members.
#
# This is useful when the Enum class gets re-defined during a script
# re-run. For more information, check out the docs:
# https://docs.streamlit.io/develop/concepts/design/custom-classes#enums
#
# Allowed values:
# - "off"          : Disables Enum coercion.
# - "nameOnly"     : Enum classes can be coerced if their member names match.
# - "nameAndValue" : Enum classes can be coerced if their member names AND
#                    member values match.
#
# Default: "nameOnly"
enumCoercion = "nameOnly"
```

#### Server

```toml
[server]

# List of directories to watch for changes.
#
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify additional
# directories to watch. Paths must be absolute.
#
# Default: []
folderWatchList = []

# List of directories to ignore for changes.
#
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify exceptions within
# watched directories. Paths can be absolute or relative to the current
# working directory.
#
# Example: ['/home/user1/env', 'relative/path/to/folder']
#
# Default: []
folderWatchBlacklist = []

# Change the type of file watcher used by Streamlit, or turn it off
# completely.
#
# Allowed values:
# - "auto"     : Streamlit will attempt to use the watchdog module, and
#                falls back to polling if watchdog isn't available.
# - "watchdog" : Force Streamlit to use the watchdog module.
# - "poll"     : Force Streamlit to always use polling.
# - "none"     : Streamlit will not watch files.
#
# Default: "auto"
fileWatcherType = "auto"

# Symmetric key used to produce signed cookies. If deploying on multiple
# replicas, this should be set to the same value across all replicas to ensure
# they all share the same secret.
#
# Default: randomly generated secret key.
cookieSecret = "a-random-key-appears-here"

# If false, will attempt to open a browser window on start.
#
# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or
# (2) we are running in the Streamlit Atom plugin.
headless = false

# Whether to show a terminal prompt for the user's email address when
# they run Streamlit (locally) for the first time. If you set
# `server.headless=True`, Streamlit will not show this prompt.
#
# Default: true
showEmailPrompt = true

# Automatically rerun script when the file is modified on disk.
#
# Default: false
runOnSave = false

# The address where the server will listen for client and browser
# connections.
#
# Use this if you want to bind the server to a specific address.
# If set, the server will only be accessible from this address, and not from
# any aliases (like localhost).
#
# Default: (unset)
address =

# The port where the server will listen for browser connections.
#
# Default: 8501
port = 8501

# The base path for the URL where Streamlit should be served from.
#
# Default: ""
baseUrlPath = ""

# Enables support for Cross-Origin Resource Sharing (CORS) protection,
# for added security.
#
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
#
# Default: true
enableCORS = true

# Allowed list of origins.
#
# If CORS protection is enabled (`server.enableCORS=True`), use this
# option to set a list of allowed origins that the Streamlit server will
# accept traffic from.
#
# This config option does nothing if CORS protection is disabled.
#
# Example: ['http://example.com', 'https://streamlit.io']
#
# Default: []
corsAllowedOrigins = []

# Enables support for Cross-Site Request Forgery (XSRF) protection, for
# added security.
#
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
#
# Default: true
enableXsrfProtection = true

# Max size, in megabytes, for files uploaded with the file_uploader.
#
# Default: 200
maxUploadSize = 200

# Max size, in megabytes, of messages that can be sent via the WebSocket
# connection.
#
# Default: 200
maxMessageSize = 200

# Enables support for websocket compression.
#
# Default: false
enableWebsocketCompression = false

# The interval (in seconds) at which the server pings the client to keep
# the websocket connection alive.
#
# The default value should work for most deployments. However, if you're
# experiencing frequent disconnections in certain proxy setups (e.g.,
# "Connection error" messages), you may want to try adjusting this value.
#
# Note: When you set this option, Streamlit automatically sets the ping
# timeout to match this interval. For Tornado &gt;=6.5, a value less than 30
# may cause connection issues.
websocketPingInterval =

# Enable serving files from a `static` directory in the running app's
# directory.
#
# Default: false
enableStaticServing = false

# TTL in seconds for sessions whose websockets have been disconnected.
#
# The server may choose to clean up session state, uploaded files, etc
# for a given session with no active websocket connection at any point
# after this time has passed. If you are using load balancing or
# replication in your deployment, you must enable session stickiness
# in your proxy to guarantee reconnection to the existing session. For
# more information, see https://docs.streamlit.io/replication.
#
# Default: 120
disconnectedSessionTTL = 120

# Server certificate file for connecting via HTTPS.
# Must be set at the same time as "server.sslKeyFile".
#
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For a production environment, we
# recommend performing SSL termination through a load balancer or reverse
# proxy.']
sslCertFile =

# Cryptographic key file for connecting via HTTPS.
# Must be set at the same time as "server.sslCertFile".
#
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For a production environment, we
# recommend performing SSL termination through a load balancer or reverse
# proxy.']
sslKeyFile =
```

#### Browser

```toml
[browser]

# Internet address where users should point their browsers in order to
# connect to the app. Can be IP address or DNS name and path.
#
# This is used to:
# - Set the correct URL for CORS and XSRF protection purposes.
# - Show the URL on the terminal
# - Open the browser
#
# Default: "localhost"
serverAddress = "localhost"

# Whether to send usage statistics to Streamlit.
#
# Default: true
gatherUsageStats = true

# Port where users should point their browsers in order to connect to the
# app.
#
# This is used to:
# - Set the correct URL for XSRF protection purposes.
# - Show the URL on the terminal (part of `streamlit run`).
# - Open the browser automatically (part of `streamlit run`).
#
# This option is for advanced use cases. To change the port of your app, use
# `server.Port` instead.
#
# Default: whatever value is set in server.port.
serverPort = 8501
```

#### Mapbox

```toml
[mapbox]

# If you'd like to show maps using Mapbox rather than Carto, use this
# to pass the Mapbox API token.
#
# THIS IS DEPRECATED.
#
# Instead of this, you should use either the MAPBOX_API_KEY environment
# variable or PyDeck's `api_keys` argument.
#
# This option will be removed on or after 2026-05-01.
#
# Default: ""
token = ""
```

#### Theme

To define switchable light and dark themes, the configuration options in the
`[theme]` table can be used in separate `[theme.dark]` and `[theme.light]`
tables, except for the following options:

- `base`
- `fontFaces`
- `baseFontSize`
- `baseFontWeight`
- `showSidebarBorder`
- `chartCategoricalColors`
- `chartSequentialColors`

```toml
[theme]

# The theme that your custom theme inherits from.
#
# This can be one of the following:
# - "light": Streamlit's default light theme.
# - "dark" : Streamlit's default dark theme.
# - A local file path to a TOML theme file: A local custom theme, like
#   "themes/custom.toml".
# - A URL to a TOML theme file: An externally hosted custom theme, like
#   "https://example.com/theme.toml".
#
# A TOML theme file must contain a [theme] table with theme options.
# Any theme options defined in the app's config.toml file will override
# those defined in the TOML theme file.
base =

# Primary accent color.
primaryColor =

# Background color of the app.
backgroundColor =

# Background color used for most interactive widgets.
secondaryBackgroundColor =

# Color used for almost all text.
textColor =

# Red color used in the basic color palette.
#
# By default, this is #ff4b4b for the light theme and #ff2b2b for the
# dark theme.
#
# If `redColor` is provided, and `redBackgroundColor` isn't, then
# `redBackgroundColor` will be derived from `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
redColor =

# Orange color used in the basic color palette.
#
# By default, this is #ffa421 for the light theme and #ff8700 for the
# dark theme.
#
# If `orangeColor` is provided, and `orangeBackgroundColor` isn't, then
# `orangeBackgroundColor` will be derived from `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
orangeColor =

# Yellow color used in the basic color palette.
#
# By default, this is #faca2b for the light theme and #ffe312 for the
# dark theme.
#
# If `yellowColor` is provided, and `yellowBackgroundColor` isn't, then
# `yellowBackgroundColor` will be derived from `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
yellowColor =

# Blue color used in the basic color palette.
#
# By default, this is #1c83e1 for the light theme and #0068c9 for the
# dark theme.
#
# If a `blueColor` is provided, and `blueBackgroundColor` isn't, then
# `blueBackgroundColor` will be derived from `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
blueColor =

# Green color used in the basic color palette.
#
# By default, this is #21c354 for the light theme and #09ab3b for the
# dark theme.
#
# If `greenColor` is provided, and `greenBackgroundColor` isn't, then
# `greenBackgroundColor` will be derived from `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
greenColor =

# Violet color used in the basic color palette.
#
# By default, this is #803df5 for both the light and dark themes.
#
# If a `violetColor` is provided, and `violetBackgroundColor` isn't, then
# `violetBackgroundColor` will be derived from `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
violetColor =

# Gray color used in the basic color palette.
#
# By default, this is #a3a8b8 for the light theme and #555867 for the
# dark theme.
#
# If `grayColor` is provided, and `grayBackgroundColor` isn't, then
# `grayBackgroundColor` will be derived from `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
grayColor =

# Red background color used in the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ff2b2b with 10% opacity for light theme and
# #ff6c6c with 20% opacity for dark theme.
redBackgroundColor =

# Orange background color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffa421 with 10% opacity for the light theme and
# #ff8700 with 20% opacity for the dark theme.
orangeBackgroundColor =

# Yellow background color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffff12 with 10% opacity for the light theme and
# #ffff12 with 20% opacity for the dark theme.
yellowBackgroundColor =

# Blue background color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #1c83ff with 10% opacity for the light theme and
# #3d9df3 with 20% opacity for the dark theme.
blueBackgroundColor =

# Green background color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #21c354 with 10% opacity for the light theme and
# #3dd56d with 20% opacity for the dark theme.
greenBackgroundColor =

# Violet background color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #9a5dff with 10% opacity for light theme and
# #9a5dff with 20% opacity for dark theme.
violetBackgroundColor =

# Gray background color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #31333f with 10% opacity for the light theme and
# #808495 with 20% opacity for the dark theme.
grayBackgroundColor =

# Red text color used for the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor`, darkened by 15%
# for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark
# theme.
redTextColor =

# Orange text color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark
# theme.
orangeTextColor =

# Yellow text color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark
# theme.
yellowTextColor =

# Blue text color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark
# theme.
blueTextColor =

# Green text color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #158237 for the light theme and #5ce488 for the dark
# theme.
greenTextColor =

# Violet text color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #583f84 for the light theme and #b27eff for the dark
# theme.
violetTextColor =

# Gray text color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #31333f with 60% opacity for the light theme and
# #fafafa with 60% opacity for the dark theme.
grayTextColor =

# Color used for all links.
#
# This defaults to the resolved value of `blueTextColor`.
linkColor =

# Whether or not links should be displayed with an underline.
linkUnderline =

# Text color used for code blocks.
#
# This defaults to the resolved value of `greenTextColor`.
codeTextColor =

# Background color used for code blocks.
codeBackgroundColor =

# The font family for all text, except code blocks.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "Nunito:https://fonts.googleapis.com/css2?family=Nunito=swap")
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# For example, you can use the following:
#
# font = "cool-font, fallback-cool-font, sans-serif"
font =

# An array of fonts to use in your app.
#
# Each font in the array is a table (dictionary) that can have the
# following attributes, closely resembling CSS font-face definitions:
# - family
# - url
# - weight (optional)
# - style (optional)
# - unicodeRange (optional)
#
# To host a font with your app, enable static file serving with
# `server.enableStaticServing=true`.
#
# You can define multiple [[theme.fontFaces]] tables, including multiple
# tables with the same family if your font is defined by multiple files.
#
# For example, a font hosted with your app may have a [[theme.fontFaces]]
# table as follows:
#
# [[theme.fontFaces]]
# family = "font_name"
# url = "app/static/font_file.woff"
# weight = "400"
# style = "normal"
fontFaces =

# The root font size (in pixels) for the app.
#
# This determines the overall scale of text and UI elements. This is a
# positive integer.
#
# If this isn't set, the font size will be 16px.
baseFontSize =

# The root font weight for the app.
#
# This determines the overall weight of text and UI elements. This is an
# integer multiple of 100. Values can be between 100 and 600, inclusive.
#
# If this isn't set, the font weight will be set to 400 (normal weight).
baseFontWeight =

# The font family to use for headings.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "Nunito:https://fonts.googleapis.com/css2?family=Nunito=swap")
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# If this isn't set, Streamlit uses `theme.font` for headings.
headingFont =

# One or more font sizes for h1-h6 headings.
#
# If no sizes are set, Streamlit will use the default sizes for h1-h6
# headings. Heading font sizes set in [theme] are not inherited by
# [theme.sidebar]. The following sizes are used by default:
# [
#     "2.75rem", # h1 (1.5rem for sidebar)
#     "2.25rem", # h2 (1.25rem for sidebar)
#     "1.75rem", # h3 (1.125rem for sidebar)
#     "1.5rem", # h4 (1rem for sidebar)
#     "1.25rem", # h5 (0.875rem for sidebar)
#     "1rem", # h6 (0.75rem for sidebar)
# ]
#
# If you specify an array with fewer than six sizes, the unspecified
# heading sizes will be the default values. For example, you can use the
# following array to set the font sizes for h1-h3 headings while keeping
# h4-h6 headings at their default sizes:
# headingFontSizes = ["3rem", "2.875rem", "2.75rem"]
#
# Setting a single value (not in an array) will set the font size for all
# h1-h6 headings to that value:
# headingFontSizes = "2.75rem"
#
# Font sizes can be specified in pixels or rem, but rem is recommended.
headingFontSizes =

# One or more font weights for h1-h6 headings.
#
# If no weights are set, Streamlit will use the default weights for h1-h6
# headings. Heading font weights set in [theme] are not inherited by
# [theme.sidebar]. The following weights are used by default:
# [
#     700, # h1 (bold)
#     600, # h2 (semi-bold)
#     600, # h3 (semi-bold)
#     600, # h4 (semi-bold)
#     600, # h5 (semi-bold)
#     600, # h6 (semi-bold)
# ]
#
# If you specify an array with fewer than six weights, the unspecified
# heading weights will be the default values. For example, you can use
# the following array to set the font weights for h1-h2 headings while
# keeping h3-h6 headings at their default weights:
# headingFontWeights = [800, 700]
#
# Setting a single value (not in an array) will set the font weight for
# all h1-h6 headings to that value:
# headingFontWeights = 500
headingFontWeights =

# The font family to use for code (monospace) in the sidebar.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono=swap")
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
codeFont =

# The font size (in pixels or rem) for code blocks and code text.
#
# This applies to font in code blocks, `st.json`, and `st.help`. It
# doesn't apply to inline code, which is set by default to 0.75em.
#
# If this isn't set, the code font size will be 0.875rem.
codeFontSize =

# The font weight for code blocks and code text.
#
# This applies to font in inline code, code blocks, `st.json`, and
# `st.help`. This is an integer multiple of 100. Values can be between
# 100 and 600, inclusive.
#
# If this isn't set, the code font weight will be 400 (normal weight).
codeFontWeight =

# The radius used as basis for the corners of most UI elements.
#
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
#
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =

# The radius used as basis for the corners of buttons.
#
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
#
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
#
# If this isn't set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =

# The color of the border around elements.
borderColor =

# The color of the border around dataframes and tables.
#
# If this isn't set, Streamlit uses `theme.borderColor` instead.
dataframeBorderColor =

# The background color of the dataframe's header.
#
# This color applies to all non-interior cells of the dataframe. This
# includes the header row, the row-selection column (if present), and
# the bottom row of data editors with a dynamic number of rows. If this
# isn't set, Streamlit uses a mix of `theme.backgroundColor` and
# `theme.secondaryBackgroundColor`.
dataframeHeaderBackgroundColor =

# Whether to show a border around input widgets.
showWidgetBorder =

# Whether to show a vertical separator between the sidebar and the main
# content area.
showSidebarBorder =

# An array of colors to use for categorical chart data.
#
# This is a list of one or more color strings which are applied in order
# to categorical data. These colors apply to Plotly, Altair, and
# Vega-Lite charts.
#
# Invalid colors are skipped, and colors repeat cyclically if there are
# more categories than colors. If no chart categorical colors are set,
# Streamlit uses a default set of colors.
#
# For light themes, the following colors are the default:
# [
#     "#0068c9", # blue80
#     "#83c9ff", # blue40
#     "#ff2b2b", # red80
#     "#ffabab", # red40
#     "#29b09d", # blueGreen80
#     "#7defa1", # green40
#     "#ff8700", # orange80
#     "#ffd16a", # orange50
#     "#6d3fc0", # purple80
#     "#d5dae5", # gray40
# ]
# For dark themes, the following colors are the default:
# [
#     "#83c9ff", # blue40
#     "#0068c9", # blue80
#     "#ffabab", # red40
#     "#ff2b2b", # red80
#     "#7defa1", # green40
#     "#29b09d", # blueGreen80
#     "#ffd16a", # orange50
#     "#ff8700", # orange80
#     "#6d3fc0", # purple80
#     "#d5dae5", # gray40
# ]
chartCategoricalColors =

# An array of ten colors to use for sequential or continuous chart data.
#
# The ten colors create a gradient color scale. These colors apply to
# Plotly, Altair, and Vega-Lite charts.
#
# Invalid color strings are skipped. If there are not exactly ten
# valid colors specified, Streamlit uses a default set of colors.
#
# For light themes, the following colors are the default:
# [
#     "#e4f5ff", #blue10
#     "#c7ebff", #blue20
#     "#a6dcff", #blue30
#     "#83c9ff", #blue40
#     "#60b4ff", #blue50
#     "#3d9df3", #blue60
#     "#1c83e1", #blue70
#     "#0068c9", #blue80
#     "#0054a3", #blue90
#     "#004280", #blue100
# ]
# For dark themes, the following colors are the default:
# [
#     "#004280", #blue100
#     "#0054a3", #blue90
#     "#0068c9", #blue80
#     "#1c83e1", #blue70
#     "#3d9df3", #blue60
#     "#60b4ff", #blue50
#     "#83c9ff", #blue40
#     "#a6dcff", #blue30
#     "#c7ebff", #blue20
#     "#e4f5ff", #blue10
# ]
chartSequentialColors =
```

#### Sidebar theme

To define switchable light and dark themes, the configuration options in the
`[theme.sidebar]` table can be used in separate `[theme.dark.sidebar]` and
`[theme.light.sidebar]`.

```toml
[theme.sidebar]

# Primary accent color.
primaryColor =

# Background color of the app.
backgroundColor =

# Background color used for most interactive widgets.
secondaryBackgroundColor =

# Color used for almost all text.
textColor =

# Red color used in the basic color palette.
#
# By default, this is #ff4b4b for the light theme and #ff2b2b for the
# dark theme.
#
# If `redColor` is provided, and `redBackgroundColor` isn't, then
# `redBackgroundColor` will be derived from `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
redColor =

# Orange color used in the basic color palette.
#
# By default, this is #ffa421 for the light theme and #ff8700 for the
# dark theme.
#
# If `orangeColor` is provided, and `orangeBackgroundColor` isn't, then
# `orangeBackgroundColor` will be derived from `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
orangeColor =

# Yellow color used in the basic color palette.
#
# By default, this is #faca2b for the light theme and #ffe312 for the
# dark theme.
#
# If `yellowColor` is provided, and `yellowBackgroundColor` isn't, then
# `yellowBackgroundColor` will be derived from `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
yellowColor =

# Blue color used in the basic color palette.
#
# By default, this is #1c83e1 for the light theme and #0068c9 for the
# dark theme.
#
# If a `blueColor` is provided, and `blueBackgroundColor` isn't, then
# `blueBackgroundColor` will be derived from `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
blueColor =

# Green color used in the basic color palette.
#
# By default, this is #21c354 for the light theme and #09ab3b for the
# dark theme.
#
# If `greenColor` is provided, and `greenBackgroundColor` isn't, then
# `greenBackgroundColor` will be derived from `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
greenColor =

# Violet color used in the basic color palette.
#
# By default, this is #803df5 for both the light and dark themes.
#
# If a `violetColor` is provided, and `violetBackgroundColor` isn't, then
# `violetBackgroundColor` will be derived from `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
violetColor =

# Gray color used in the basic color palette.
#
# By default, this is #a3a8b8 for the light theme and #555867 for the
# dark theme.
#
# If `grayColor` is provided, and `grayBackgroundColor` isn't, then
# `grayBackgroundColor` will be derived from `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
grayColor =

# Red background color used in the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ff2b2b with 10% opacity for light theme and
# #ff6c6c with 20% opacity for dark theme.
redBackgroundColor =

# Orange background color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffa421 with 10% opacity for the light theme and
# #ff8700 with 20% opacity for the dark theme.
orangeBackgroundColor =

# Yellow background color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffff12 with 10% opacity for the light theme and
# #ffff12 with 20% opacity for the dark theme.
yellowBackgroundColor =

# Blue background color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #1c83ff with 10% opacity for the light theme and
# #3d9df3 with 20% opacity for the dark theme.
blueBackgroundColor =

# Green background color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #21c354 with 10% opacity for the light theme and
# #3dd56d with 20% opacity for the dark theme.
greenBackgroundColor =

# Violet background color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #9a5dff with 10% opacity for light theme and
# #9a5dff with 20% opacity for dark theme.
violetBackgroundColor =

# Gray background color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #31333f with 10% opacity for the light theme and
# #808495 with 20% opacity for the dark theme.
grayBackgroundColor =

# Red text color used for the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor`, darkened by 15%
# for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark
# theme.
redTextColor =

# Orange text color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark
# theme.
orangeTextColor =

# Yellow text color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark
# theme.
yellowTextColor =

# Blue text color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark
# theme.
blueTextColor =

# Green text color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #158237 for the light theme and #5ce488 for the dark
# theme.
greenTextColor =

# Violet text color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #583f84 for the light theme and #b27eff for the dark
# theme.
violetTextColor =

# Gray text color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #31333f with 60% opacity for the light theme and
# #fafafa with 60% opacity for the dark theme.
grayTextColor =

# Color used for all links.
#
# This defaults to the resolved value of `blueTextColor`.
linkColor =

# Whether or not links should be displayed with an underline.
linkUnderline =

# Text color used for code blocks.
#
# This defaults to the resolved value of `greenTextColor`.
codeTextColor =

# Background color used for code blocks.
codeBackgroundColor =

# The font family for all text, except code blocks.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "Nunito:https://fonts.googleapis.com/css2?family=Nunito=swap")
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# For example, you can use the following:
#
# font = "cool-font, fallback-cool-font, sans-serif"
font =

# The font family to use for headings.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "Nunito:https://fonts.googleapis.com/css2?family=Nunito=swap")
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# If this isn't set, Streamlit uses `theme.font` for headings.
headingFont =

# One or more font sizes for h1-h6 headings.
#
# If no sizes are set, Streamlit will use the default sizes for h1-h6
# headings. Heading font sizes set in [theme] are not inherited by
# [theme.sidebar]. The following sizes are used by default:
# [
#     "2.75rem", # h1 (1.5rem for sidebar)
#     "2.25rem", # h2 (1.25rem for sidebar)
#     "1.75rem", # h3 (1.125rem for sidebar)
#     "1.5rem", # h4 (1rem for sidebar)
#     "1.25rem", # h5 (0.875rem for sidebar)
#     "1rem", # h6 (0.75rem for sidebar)
# ]
#
# If you specify an array with fewer than six sizes, the unspecified
# heading sizes will be the default values. For example, you can use the
# following array to set the font sizes for h1-h3 headings while keeping
# h4-h6 headings at their default sizes:
# headingFontSizes = ["3rem", "2.875rem", "2.75rem"]
#
# Setting a single value (not in an array) will set the font size for all
# h1-h6 headings to that value:
# headingFontSizes = "2.75rem"
#
# Font sizes can be specified in pixels or rem, but rem is recommended.
headingFontSizes =

# One or more font weights for h1-h6 headings.
#
# If no weights are set, Streamlit will use the default weights for h1-h6
# headings. Heading font weights set in [theme] are not inherited by
# [theme.sidebar]. The following weights are used by default:
# [
#     700, # h1 (bold)
#     600, # h2 (semi-bold)
#     600, # h3 (semi-bold)
#     600, # h4 (semi-bold)
#     600, # h5 (semi-bold)
#     600, # h6 (semi-bold)
# ]
#
# If you specify an array with fewer than six weights, the unspecified
# heading weights will be the default values. For example, you can use
# the following array to set the font weights for h1-h2 headings while
# keeping h3-h6 headings at their default weights:
# headingFontWeights = [800, 700]
#
# Setting a single value (not in an array) will set the font weight for
# all h1-h6 headings to that value:
# headingFontWeights = 500
headingFontWeights =

# The font family to use for code (monospace) in the sidebar.
#
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of "<font>:<url>" (like
#   "'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono=swap")
# - A comma-separated list of these (as a single string) to specify
# fallbacks
codeFont =

# The font size (in pixels or rem) for code blocks and code text.
#
# This applies to font in code blocks, `st.json`, and `st.help`. It
# doesn't apply to inline code, which is set by default to 0.75em.
#
# If this isn't set, the code font size will be 0.875rem.
codeFontSize =

# The font weight for code blocks and code text.
#
# This applies to font in inline code, code blocks, `st.json`, and
# `st.help`. This is an integer multiple of 100. Values can be between
# 100 and 600, inclusive.
#
# If this isn't set, the code font weight will be 400 (normal weight).
codeFontWeight =

# The radius used as basis for the corners of most UI elements.
#
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
#
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =

# The radius used as basis for the corners of buttons.
#
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
#
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
#
# If this isn't set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =

# The color of the border around elements.
borderColor =

# The color of the border around dataframes and tables.
#
# If this isn't set, Streamlit uses `theme.borderColor` instead.
dataframeBorderColor =

# The background color of the dataframe's header.
#
# This color applies to all non-interior cells of the dataframe. This
# includes the header row, the row-selection column (if present), and
# the bottom row of data editors with a dynamic number of rows. If this
# isn't set, Streamlit uses a mix of `theme.backgroundColor` and
# `theme.secondaryBackgroundColor`.
dataframeHeaderBackgroundColor =

# Whether to show a border around input widgets.
showWidgetBorder =
```

#### Secrets

```toml
[secrets]

# List of locations where secrets are searched.
#
# An entry can be a path to a TOML file or directory path where
# Kubernetes style secrets are saved. Order is important, import is
# first to last, so secrets in later files will take precedence over
# earlier ones.
#
# Default: [ <path>local environment's secrets.toml file&gt;, <path>project's secrets.toml file&gt;,]
files = [ "~/.streamlit/secrets.toml", "~/project directory/.streamlit/secrets.toml",]
```</path></path></url></font></url></font></url></font></url></font></url></font></url></font>

---

Source: https://docs.streamlit.io/develop/api-reference/configuration/st.get_option


* Function signature:

   st.get_option(key)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | key | str |  | The config option key of the form "section.optionName". To see all available options, run streamlit config show in a terminal. |



---

Source: https://docs.streamlit.io/develop/api-reference/configuration/st.set_option


* Function signature:

   st.set_option(key, value)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | key | str |  | The config option key of the form "section.optionName". To see all available options, run streamlit config show in a terminal. |
   | value | None |  | The new value to assign to this config option. |



---

Source: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config


* Function signature:

   st.set_page_config(page_title=None, page_icon=None, layout=None, initial_sidebar_state=None, menu_items=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | page_title | str or None |  | The page title, shown in the browser tab. If this is None (default), the page title is inherited from the previous call of st.set_page_config. If this is None and no previous call exists, the page title is inferred from the page source. If a page source is a Python file, its inferred title is derived from the filename. If a page source is a callable object, its inferred title is derived from the callable's name. |
   | page_icon | Anything supported by st.image (except list), str, or None |  | The page favicon. If page_icon is None (default), the page icon is inherited from the previous call of st.set_page_config. If this is None and no previous call exists, the favicon is a monochrome Streamlit logo. In addition to the types supported by st.image (except list), the following strings are valid:  A single-character emoji. For example, you can set page_icon="🦈".  An emoji short code. For example, you can set page_icon=":shark:". For a list of all supported codes, see https://share.streamlit.io/streamlit/emoji-shortcodes.  The string literal, "random". You can set page_icon="random" to set a random emoji from the supported list above.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, page_icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library.    Note Colors are not supported for Material icons. When you use a Material icon for favicon, it will be black, regardless of browser theme. |
   | layout | "centered", "wide", or None |  | How the page content should be laid out. If this is None (default), the page layout is inherited from the previous call of st.set_page_config. If this is None and no previous call exists, the page layout is "centered". "centered" constrains the elements into a centered column of fixed width. "wide" uses the entire screen. |
   | initial_sidebar_state | "auto", "expanded", "collapsed", or None |  | How the sidebar should start out. If this is None (default), the sidebar state is inherited from the previous call of st.set_page_config. If no previous call exists, the sidebar state is "auto". The folowing states are supported:  "auto": The sidebar is hidden on small devices and shown otherwise. "expanded": The sidebar is shown initially. "collapsed": The sidebar is hidden initially.  In most cases, "auto" provides the best user experience across devices of different sizes. |
   | menu_items | dict |  | Configure the menu that appears on the top-right side of this app. The keys in this dict denote the menu item to configure. The following keys can have string or None values:  "Get help": The URL this menu item should point to. "Report a Bug": The URL this menu item should point to. "About": A markdown string to show in the About dialog.  A URL may also refer to an email address e.g. mailto:john@example.com. If you do not include a key, its menu item will be hidden (unless it was set by a previous call to st.set_page_config). To remove an item that was specified in a previous call to st.set_page_config, set its value to None in the dictionary. |



---

# App testing

Source: https://docs.streamlit.io/develop/api-reference/app-testing


Streamlit app testing framework enables developers to build and run headless tests that execute their app code directly, simulate user input, and inspect rendered outputs for correctness.

The provided class, AppTest, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest. A typical pattern is to build a suite of tests for an app that ensure consistent functionality as the app evolves, and run the tests locally and/or in a CI environment like Github Actions.

## The AppTest class

<TileContainer>
<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest" size="full">
<h3>st.testing.v1.AppTest</h3>

`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception

at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

</RefCard>
<RefCard href="">

{/** TODO: Bug fix. The second RefCard does not render. Empty card is a workaround. **/}

</RefCard>
<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file" size="full">
<h3>AppTest.from_file</h3>

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string" size="full">
<h3>AppTest.from_string</h3>

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest

app_script = """
import streamlit as st

word_of_the_day = st.text_input("What's the word of the day?", key="word")
if word_of_the_day == st.secrets["WORD"]:
    st.success("That's right!")
elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
    st.warn("Try again.")
"""

at = AppTest.from_string(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function" size="full">
<h3>AppTest.from_function</h3>

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest

def app_script ():
    import streamlit as st

    word_of_the_day = st.text_input("What's the word of the day?", key="word")
    if word_of_the_day == st.secrets["WORD"]:
        st.success("That's right!")
    elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
        st.warn("Try again.")

at = AppTest.from_function(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>
</TileContainer>

## Testing-element classes

<TileContainer>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock" size="half">
<h4>Block</h4>

A representation of container elements, including:

- `st.chat_message`
- `st.columns`
- `st.sidebar`
- `st.tabs`
- The main body of the app.

```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement" size="half">
<h4>Element</h4>

The base class for representation of all elements, including:

- `st.title`
- `st.header`
- `st.markdown`
- `st.dataframe`

```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton" size="third">
<h4>Button</h4>

A representation of `st.button` and `st.form_submit_button`.

```python
at.button[0].click().run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput" size="third">
<h4>ChatInput</h4>

A representation of `st.chat_input`.

```python
at.chat_input[0].set_value("What is Streamlit?").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox" size="third">
<h4>Checkbox</h4>

A representation of `st.checkbox`.

```python
at.checkbox[0].check().run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker" size="third">
<h4>ColorPicker</h4>

A representation of `st.color_picker`.

```python
at.color_picker[0].pick("#FF4B4B").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput" size="third">
<h4>DateInput</h4>

A representation of `st.date_input`.

```python
release_date = datetime.date(2023, 10, 26)
at.date_input[0].set_value(release_date).run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect" size="third">
<h4>Multiselect</h4>

A representation of `st.multiselect`.

```python
at.multiselect[0].select("New York").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput" size="third">
<h4>NumberInput</h4>

A representation of `st.number_input`.

```python
at.number_input[0].increment().run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio" size="third">
<h4>Radio</h4>

A representation of `st.radio`.

```python
at.radio[0].set_value("New York").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider" size="third">
<h4>SelectSlider</h4>

A representation of `st.select_slider`.

```python
at.select_slider[0].set_range("A","C").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox" size="third">
<h4>Selectbox</h4>

A representation of `st.selectbox`.

```python
at.selectbox[0].select("New York").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider" size="third">
<h4>Slider</h4>

A representation of `st.slider`.

```python
at.slider[0].set_range(2,5).run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea" size="third">
<h4>TextArea</h4>

A representation of `st.text_area`.

```python
at.text_area[0].input("Streamlit is awesome!").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput" size="third">
<h4>TextInput</h4>

A representation of `st.text_input`.

```python
at.text_input[0].input("Streamlit").run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput" size="third">
<h4>TimeInput</h4>

A representation of `st.time_input`.

```python
at.time_input[0].increment().run()
```

</RefCard>
<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle" size="third">
<h4>Toggle</h4>

A representation of `st.toggle`.

```python
at.toggle[0].set_value("True").run()
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest

<h1>{{display: "none"}}&gt;</h1>

---

# Testing element classes

Source: https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes


## st.testing.v1.element_tree.Block

The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.


* Function signature:

   st.testing.v1.element_tree.Element(proto, root)



* Function signature:

   st.testing.v1.element_tree.Button(proto, root)



* Function signature:

   st.testing.v1.element_tree.ChatInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Checkbox(proto, root)



* Function signature:

   st.testing.v1.element_tree.ColorPicker(proto, root)



* Function signature:

   st.testing.v1.element_tree.DateInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Multiselect(proto, root)



* Function signature:

   st.testing.v1.element_tree.NumberInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Radio(proto, root)



* Function signature:

   st.testing.v1.element_tree.SelectSlider(proto, root)



* Function signature:

   st.testing.v1.element_tree.Selectbox(proto, root)



* Function signature:

   st.testing.v1.element_tree.Slider(proto, root)



* Function signature:

   st.testing.v1.element_tree.TextArea(proto, root)



* Function signature:

   st.testing.v1.element_tree.TextInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.TimeInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Toggle(proto, root)



---

# Command-line interface

Source: https://docs.streamlit.io/develop/api-reference/cli


When you install Streamlit, a command-line (CLI) tool gets installed
as well. The purpose of this tool is to run Streamlit apps, change Streamlit configuration options,
and help you diagnose and fix issues.

## Available commands

- [`streamlit cache clear`](/develop/api-reference/cli/cache): Clear the on-disk cache.
- [`streamlit config show`](/develop/api-reference/cli/config): Show all configuration options.
- [`streamlit docs`](/develop/api-reference/cli/docs): Open the Streamlit docs.
- [`streamlit hello`](/develop/api-reference/cli/hello): Run an example Streamlit app.
- [`streamlit help`](/develop/api-reference/cli/help): Show the available CLI commands.
- [`streamlit init`](/develop/api-reference/cli/init): Create the files for a new Streamlit app.
- [`streamlit run`](/develop/api-reference/cli/run): Run your Streamlit app.
- [`streamlit version`](/develop/api-reference/cli/version): Show the version of Streamlit.

### Run your app

The most important command is `streamlit run`, which is summarized for convenience here:

```bash
streamlit run your_script.py
```

At any time, in your terminal, you can stop the server with **Ctrl+C**.

---

Source: https://docs.streamlit.io/develop/api-reference/cli/cache

## `$ streamlit cache clear`

Clear persisted files from the on-disk [Streamlit cache](/develop/api-reference/caching-and-state), if present.

### Syntax

```
streamlit cache clear
```

---

Source: https://docs.streamlit.io/develop/api-reference/cli/config

## `$ streamlit config show`

Print all the available configuration options, including their descriptions, default values, and current values. For more information about configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml).

### Syntax

```
streamlit config show
```

---

Source: https://docs.streamlit.io/develop/api-reference/cli/docs

## `$ streamlit docs`

Open the Streamlit docs in your default browser.

### Syntax

```
streamlit docs
```

---

Source: https://docs.streamlit.io/develop/api-reference/cli/hello

## `$ streamlit hello`

Run the Hello app, an example Streamlit app included with the Streamlit library.

### Syntax

```
streamlit hello
```

### Options

The `hello` command accepts configuration options (just like the `run` command does). Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

- `--theme.primaryColor=blue`
- `--theme.primaryColor="blue"`
- `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Example

#### Example 1: Run the Hello app with default settings

To verify that Streamlit is installed correctly, this command runs an example app included in the Streamlit library. From any directory, execute the following:

```
streamlit hello
```

Streamlit will start the Hello app and open it in your default browser. The source for the Hello app can be [viewed in GitHub](https://github.com/streamlit/streamlit/tree/develop/lib/streamlit/hello).

#### Example 2: Run the Hello app with a custom config option value

To run the Hello app with a blue accent color, from any directory, execute the following:

```
streamlit hello --theme.primaryColor=blue
```</value></option></section>

---

Source: https://docs.streamlit.io/develop/api-reference/cli/help

## `$ streamlit help`

Print the available commands for the Streamlit CLI tool. This command is equivalent to executing `streamlit --help`.

### Syntax

```
streamlit help
```

---

Source: https://docs.streamlit.io/develop/api-reference/cli/init

## `$ streamlit init`

This command creates the files for a new Streamlit app.

### Syntax

```
streamlit init <directory>
```

### Arguments

`<directory>` (Optional): The directory location of the new project. If no directory is provided, the current working directory will be used.

### Examples

#### Example 1: Create project files the current working directory

1. In your current working directory (CWD), execute the following:

   ```bash
   streamlit init
   ```

   Streamlit creates the following files:

   ```
   CWD/
   ├── requirements.txt
   └── streamlit_app.py
   ```

2. In your terminal, Streamlit prompts, `❓ Run the app now? [Y/n]`. Enter `Y` for yes.

   This is equivalent to executing `streamlit run streamlit_app.py` from your current working directory.

3. Begin editing your `streamlit_app.py` file and save your changes.

#### Example 2: Create project files in another directory

1. In your current working directory (CWD), execute the following:

   ```bash
   streamlit init project
   ```

   Streamlit creates the following files:

   ```
   CWD/
   └── project/
       ├── requirements.txt
       └── streamlit_app.py
   ```

2. In your terminal, Streamlit prompts, `❓ Run the app now? [Y/n]`. Enter `Y` for yes.

   This is equivalent to executing `streamlit run project/streamlit_app.py` from your current working directory.

3. Begin editing your `streamlit_app.py` file and save your changes.</directory></directory>

---

Source: https://docs.streamlit.io/develop/api-reference/cli/run

## `$ streamlit run`

This command starts your Streamlit app.

### Syntax

```
streamlit run [<entrypoint>or directory&gt;] [-- config options] [script args]
```

### Arguments

`<entrypoint>or directory&gt;` (optional): The path to your entrypoint file or directory for your Streamlit app.

- **If not provided**: Streamlit will try to run `streamlit_app.py` from the current working directory.
- **If a directory path is provided**: Streamlit will try to run `streamlit_app.py` in the specified directory.
- **If a file path is provided**: Streamlit will run the specified file.

In a multipage app with `st.navigation`, your entrypoint file acts as a router between your pages. Otherwise, your entrypoint file is your app's homepage.

### Options

Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

- `--theme.primaryColor=blue`
- `--theme.primaryColor="blue"`
- `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Script arguments

If you need to pass arguments directly to your script, you can pass them as positional arguments. If you use `sys.argv` to read your arguments, `sys.argv` returns a list of all arguments and does _not_ include any configuration options. Python interprets all arguments as strings.

- `sys.argv[0]` returns the the path to your entrypoint file, even if you did not explicitly provide it.
- `sys.argv[1:]` returns a list of arguments in order and does not include any configuration options.

### Examples

- If your app is named `streamlit_app.py` in your working directory, you can run it with the following command:

  ```
  streamlit run
  ```

- If your app has a different name and is in your working directory, run it like the following command:

  ```
  streamlit run your_app.py
  ```

- If your app is named `streamlit_app.py` in a subdirectory, you can run it like the following command:

  ```
  streamlit run your_subdirectory
  ```

- If your app has a different name and is in a subdirectory, run it like the following command:

  ```
  streamlit run your_subdirectory/your_app.py
  ```

- If your app is saved in a public GitHub repo or gist, run it like the following command:

  ```
  streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
  ```

- If you need to set one or more configuration options, run it like the following command:

  ```
  streamlit run your_app.py --client.showErrorDetails=False --theme.primaryColor=blue
  ```

  Or if using the default `streamlit_app.py`:

  ```
  streamlit run --client.showErrorDetails=False --theme.primaryColor=blue
  ```

- If you need to pass an argument to your script, run it like the following command:

  ```
  streamlit run your_app.py "my list" of arguments
  ```

  Within your script, the following statements will be true:

  ```
  sys.argv[0] == "your_app.py"
  sys.argv[1] == "my list"
  sys.argv[2] == "of"
  sys.argv[3] == "arguments"
  ```</value></option></section></entrypoint></entrypoint>

---

Source: https://docs.streamlit.io/develop/api-reference/cli/version

## `$ streamlit version`

Print Streamlit's version number. This command is equivalent to executing `streamlit --version`.

### Syntax

```
streamlit version
```

---

# Tutorials

Source: https://docs.streamlit.io/develop/tutorials


Our tutorials include step-by-step examples of building different types of apps in Streamlit.

<TileContainer layout="list">
<RefCard href="/develop/tutorials/authentication">
<h5>Add user authentication</h5>

Add user authentication with Streamlit's built-in support for OpenID Connect.

</RefCard>
<RefCard href="/develop/tutorials/chat-and-llm-apps">
<h5>Chat apps and LLMs</h5>

Work with LLMs and create chat apps.

</RefCard>
<RefCard href="/develop/tutorials/configuration-and-theming">
<h5>Configuration and theming</h5>

Customize the appearance of your app.

</RefCard>
<RefCard href="/develop/tutorials/databases">
<h5>Connect to data sources</h5>

Connect to popular datasources.

</RefCard>
<RefCard href="/develop/tutorials/elements">
<h5>Work with Streamlit's core elements</h5>

Work with core elements like dataframes and charts.

</RefCard>
<RefCard href="/develop/tutorials/execution-flow">
<h5>Use core features to work with Streamlit's execution model</h5>

Build simple apps and walk through examples to learn about Streamlit's core features and execution model.

</RefCard>
<RefCard href="/develop/tutorials/multipage">
<h5>Create multipage apps</h5>

Create multipage apps, navigation, and flows.

</RefCard>
</TileContainer>

When you're done developing your app, see our [deployment tutorials](/deploy/tutorials), too!

---

# Authenticate users and personalize your app

Source: https://docs.streamlit.io/develop/tutorials/authentication


Streamlit supports user authentication with the OpenID Connect (OIDC) protocol. You can use any OIDC provider. Whether you want to create a social login or manage your enterprise users, Streamlit makes it simple to authenticate your users.

<TileContainer layout="list">
<RefCard href="/develop/tutorials/authentication/google">
<h5>Google Auth Platform</h5>
        Google is one of the most popular identity providers for social logins. You can use the Google Auth Platform with any Google account, including personal and organization accounts.
    </RefCard>
<RefCard href="/develop/tutorials/authentication/microsoft">
<h5>Microsoft Entra</h5>
        Microsoft is popular for both social and business logins. You can include personal, school, or work accounts in your integration.
    </RefCard>
</TileContainer>

---

# Use the Google Auth Platform to authenticate users

Source: https://docs.streamlit.io/develop/tutorials/authentication/google


Google is one of the most popular identity providers for social logins. You can use the Google Auth Platform with both private and organizational Google accounts. This tutorial configures authentication for anyone with a Google account. For more information, see Google's overview of the [Google Auth Platform](https://support.google.com/cloud/topic/15540269?hl=en=3473162=576431444945556851-NC) and [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect#discovery).

## Prerequisites

- This tutorial requires the following Python libraries:

  ```text
  streamlit&gt;=1.42.0
  Authlib&gt;=1.3.2
  ```

- You should have a clean working directory called `your-repository`.
- You must have a Google account and accept the terms of [Google Cloud](https://console.cloud.google.com/) to use their authentication service.
- You must have a project in Google Cloud within which to create your application.
  For more information about managing your projects in Google Cloud, see [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in Google's documentation.

## Summary

In this tutorial, you'll build an app that users can log in to with their Google accounts. When they log in, they'll see a personalized greeting with their name and have the option to log out.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

`.streamlit/secrets.toml`

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

`app.py`

```python
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)
```

</Collapse>

---

# Use Microsoft Entra to authenticate users

Source: https://docs.streamlit.io/develop/tutorials/authentication/microsoft


[Microsoft Identity Platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview) is a service within Microsoft Entra that lets you build applications to authenticate users. Your applications can use personal, work, and school accounts managed by Microsoft.

## Prerequisites

- This tutorial requires the following Python libraries:

  ```text
  streamlit&gt;=1.42.0
  Authlib&gt;=1.3.2
  ```

- You should have a clean working directory called `your-repository`.
- You must have a Microsoft Azure account, which includes Microsoft Entra ID.

## Summary

In this tutorial, you'll build an app that users can log in to with their personal Microsoft accounts. When they log in, they'll see a personalized greeting with their name and have the option to log out.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

`.streamlit/secrets.toml`

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/consumers/v2.0/.well-known/openid-configuration"
```

`app.py`

```python
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)
```

</Collapse>

---

# Build LLM apps

Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps


<TileContainer layout="list">
<RefCard href="/develop/tutorials/llms/build-conversational-apps">
<h5>Build a basic chat app</h5>

Build a simple OpenAI chat app to get started with Streamlit's chat elements.

</RefCard>
<RefCard href="/develop/tutorials/llms/llm-quickstart">
<h5>Build an LLM app using LangChain</h5>

Build a chat app using the LangChain framework with OpenAI.

</RefCard>
<RefCard href="/develop/tutorials/chat-and-llm-apps/chat-response-feedback">
<h5>Get chat response feedback</h5>

Buid a chat app and let users rate the responses.
(<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;thumb_up</i></RefCard>
<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;thumb_down</i></TileContainer>)



---

# Build a basic LLM chat app

Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps


## Introduction

The advent of large language models like GPT has revolutionized the ease of developing chat-based applications. Streamlit offers several [Chat elements](/develop/api-reference/chat), enabling you to build Graphical User Interfaces (GUIs) for conversational agents or chatbots. Leveraging [session state](/develop/concepts/architecture/session-state) along with these elements allows you to construct anything from a basic chatbot to a more advanced, ChatGPT-like experience using purely Python code.

In this tutorial, we'll start by walking through Streamlit's chat elements, `st.chat_message` and `st.chat_input`. Then we'll proceed to construct three distinct applications, each showcasing an increasing level of complexity and functionality:

1. First, we'll [Build a bot that mirrors your input](#build-a-bot-that-mirrors-your-input) to get a feel for the chat elements and how they work. We'll also introduce [session state](/develop/concepts/architecture/session-state) and how it can be used to store the chat history. This section will serve as a foundation for the rest of the tutorial.
2. Next, you'll learn how to [Build a simple chatbot GUI with streaming](#build-a-simple-chatbot-gui-with-streaming).
3. Finally, we'll [Build a ChatGPT-like app](#build-a-chatgpt-like-app) that leverages session state to remember conversational context, all within less than 50 lines of code.

Here's a sneak peek of the LLM-powered chatbot GUI with streaming we'll build in this tutorial:

<Cloud height="700px" name="doc-chat-llm"/>

Play around with the above demo to get a feel for what we'll build in this tutorial. A few things to note:

- There's a chat input at the bottom of the screen that's always visible. It contains some placeholder text. You can type in a message and press Enter or click the run button to send it.
- When you enter a message, it appears as a chat message in the container above. The container is scrollable, so you can scroll up to see previous messages. A default avatar is displayed to your messages' left.
- The assistant's responses are streamed to the frontend and are displayed with a different default avatar.

Before we start building, let's take a closer look at the chat elements we'll use.

## Chat elements

Streamlit offers several commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

[`st.chat_message`](/develop/api-reference/chat/st.chat_message) lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. [`st.chat_input`](/develop/api-reference/chat/st.chat_input) lets you display a chat input widget so the user can type in a message.

For an overview of the API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk"/>

### st.chat_message

`st.chat_message` lets you insert a multi-element chat message container into your app. The returned container can contain any Streamlit element, including charts, tables, text, and more. To add elements to the returned container, you can use `with` notation.

`st.chat_message`'s first parameter is the `name` of the message author, which can be either `"user"` or `"assistant"` to enable preset styling and avatars, like in the demo above. You can also pass in a custom string to use as the author name. Currently, the name is not shown in the UI but is only set as an accessibility label. For accessibility reasons, you should not use an empty string.

Here's an minimal example of how to use `st.chat_message` to display a welcome message:

```python
import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")
```

<Image src="/images/knowledge-base/chat-message-hello.png"/>
<br/>

Notice the message is displayed with a default avatar and styling since we passed in `"user"` as the author name. You can also pass in `"assistant"` as the author name to use a different default avatar and styling, or pass in a custom name and avatar. See the [API reference](/develop/api-reference/chat/st.chat_message) for more details.

```python
import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))
```

<Cloud height="450px" name="doc-chat-message-user1"/>

While we've used the preferred `with` notation in the above examples, you can also just call methods directly in the returned objects. The below example is equivalent to the one above:

```python
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
```

So far, we've displayed predefined messages. But what if we want to display messages based on user input?

### st.chat_input

`st.chat_input` lets you display a chat input widget so the user can type in a message. The returned value is the user's input, which is `None` if the user hasn't sent a message yet. You can also pass in a default prompt to display in the input widget. Here's an example of how to use `st.chat_input` to display a chat input widget and show the user's input:

```python
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
```

<Cloud height="350px" name="doc-chat-input"/>

Pretty straightforward, right? Now let's combine `st.chat_message` and `st.chat_input` to build a bot the mirrors or echoes your input.

## Build a bot that mirrors your input

In this section, we'll build a bot that mirrors or echoes your input. More specifically, the bot will respond to your input with the same message. We'll use `st.chat_message` to display the user's input and `st.chat_input` to accept user input. We'll also use [session state](/develop/concepts/architecture/session-state) to store the chat history so we can display it in the chat message container.

First, let's think about the different components we'll need to build our bot:

- Two chat message containers to display messages from the user and the bot, respectively.
- A chat input widget so the user can type in a message.
- A way to store the chat history so we can display it in the chat message containers. We can use a list to store the messages, and append to it every time the user or bot sends a message. Each entry in the list will be a dictionary with the following keys: `role` (the author of the message), and `content` (the message content).

```python
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

In the above snippet, we've added a title to our app and a for loop to iterate through the chat history and display each message in the chat message container (with the author role and message content). We've also added a check to see if the `messages` key is in `st.session_state`. If it's not, we initialize it to an empty list. This is because we'll be adding messages to the list later on, and we don't want to overwrite the list every time the app reruns.

Now let's accept user input with `st.chat_input`, display the user's message in the chat message container, and add it to the chat history.

```python
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
```

We used the `:=` operator to assign the user's input to the `prompt` variable and checked if it's not `None` in the same line. If the user has sent a message, we display the message in the chat message container and append it to the chat history.

All that's left to do is add the chatbot's responses within the `if` block. We'll use the same logic as before to display the bot's response (which is just the user's prompt) in the chat message container and add it to the history.

```python
response = f"Echo: {prompt}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
```

Putting it all together, here's the full code for our simple chatbot GUI and the result:

<Collapse title="View full code">{false}&gt;

```python
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
```

</Collapse>

---


---

**Navigation:** [← Previous](./06-store-the-initial-value-of-widgets-in-session-stat.md) | [Index](./index.md) | [Next →](./08-build-an-llm-app-using-langchain.md)
