---
title: "Connections and databases"
source: https://docs.streamlit.io/develop/api-reference/connections
section: 197
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
```python
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
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">
<Image>alt="screenshot" src="/images/api/connections.SQLConnection.svg" /&gt;

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```python
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
```python
</RefCard>
</TileContainer>

## Secrets

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.secrets" size="half">
<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```python
</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">
<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```python
</YOUR_SECRET_KEY>
</RefCard>

## Deprecated classes

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.snowparkconnection" size="half">{true}&gt;

<h4>SnowparkConnection</h4>

A connection to Snowflake.

```python
conn = st.connection("snowpark")
```python
</RefCard></TileContainer>
</TileContainer>

---

[← Previous](192-session-state.md) | [Index](index.md) | [Next →](index.md)
