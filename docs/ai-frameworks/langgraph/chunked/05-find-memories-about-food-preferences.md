# Find memories about food preferences

**Navigation:** [← Previous](./04-node-that-uses-the-instructions.md) | [Index](./index.md)

---

# Find memories about food preferences

# (This can be done after putting memories into the store)
memories = store.search(
    namespace_for_memory,
    query="What does the user like to eat?",
    limit=3  # Return top 3 matches
)
```





You can control which parts of your memories get embedded by configuring the `fields` parameter or by specifying the `index` parameter when storing memories:

```python

# Store with specific fields to embed
store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {
        "food_preference": "I love Italian cuisine",
        "context": "Discussing dinner plans"
    },
    index=["food_preference"]  # Only embed "food_preferences" field
)


# Store without embedding (still retrievable, but not searchable)
store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {"system_info": "Last updated: 2024-01-01"},
    index=False
)
```





### Using in LangGraph

With this all in place, we use the `in_memory_store` in LangGraph. The `in_memory_store` works hand-in-hand with the checkpointer: the checkpointer saves state to threads, as discussed above, and the `in_memory_store` allows us to store arbitrary information for access _across_ threads. We compile the graph with both the checkpointer and the `in_memory_store` as follows.

```python
from langgraph.checkpoint.memory import InMemorySaver


# We need this because we want to enable threads (conversations)
checkpointer = InMemorySaver()


# ... Define the graph ...


# Compile the graph with the checkpointer and store
graph = graph.compile(checkpointer=checkpointer, store=in_memory_store)
```





We invoke the graph with a `thread_id`, as before, and also with a `user_id`, which we'll use to namespace our memories to this particular user as we showed above.

```python

# Invoke the graph
user_id = "1"
config = {"configurable": {"thread_id": "1", "user_id": user_id}}


# First let's just say hi to the AI
for update in graph.stream(
    {"messages": [{"role": "user", "content": "hi"}]}, config, stream_mode="updates"
):
    print(update)
```





We can access the `in_memory_store` and the `user_id` in _any node_ by passing `store: BaseStore` and `config: RunnableConfig` as node arguments. Here's how we might use semantic search in a node to find relevant memories:

```python
def update_memory(state: MessagesState, config: RunnableConfig, *, store: BaseStore):

    # Get the user id from the config
    user_id = config["configurable"]["user_id"]

    # Namespace the memory
    namespace = (user_id, "memories")

    # ... Analyze conversation and create a new memory

    # Create a new memory ID
    memory_id = str(uuid.uuid4())

    # We create a new memory
    store.put(namespace, memory_id, {"memory": memory})

```





As we showed above, we can also access the store in any node and use the `store.search` method to get memories. Recall the memories are returned as a list of objects that can be converted to a dictionary.

```python
memories[-1].dict()
{'value': {'food_preference': 'I like pizza'},
 'key': '07e0caf4-1631-47b7-b15f-65515d4c1843',
 'namespace': ['1', 'memories'],
 'created_at': '2024-10-02T17:22:31.590602+00:00',
 'updated_at': '2024-10-02T17:22:31.590605+00:00'}
```





We can access the memories and use them in our model call.

```python
def call_model(state: MessagesState, config: RunnableConfig, *, store: BaseStore):
    # Get the user id from the config
    user_id = config["configurable"]["user_id"]

    # Namespace the memory
    namespace = (user_id, "memories")

    # Search based on the most recent message
    memories = store.search(
        namespace,
        query=state["messages"][-1].content,
        limit=3
    )
    info = "\n".join([d.value["memory"] for d in memories])

    # ... Use memories in the model call
```





If we create a new thread, we can still access the same memories so long as the `user_id` is the same.

```python

# Invoke the graph
config = {"configurable": {"thread_id": "2", "user_id": "1"}}


# Let's say hi again
for update in graph.stream(
    {"messages": [{"role": "user", "content": "hi, tell me about my memories"}]}, config, stream_mode="updates"
):
    print(update)
```





When we use the LangGraph Platform, either locally (e.g., in LangGraph Studio) or with LangGraph Platform, the base store is available to use by default and does not need to be specified during graph compilation. To enable semantic search, however, you **do** need to configure the indexing settings in your `langgraph.json` file. For example:

```json
{
    ...
    "store": {
        "index": {
            "embed": "openai:text-embeddings-3-small",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}
```

See the [deployment guide](../cloud/deployment/semantic_search.md) for more details and configuration options.


## Checkpointer libraries

Under the hood, checkpointing is powered by checkpointer objects that conform to [BaseCheckpointSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) interface. LangGraph provides several checkpointer implementations, all implemented via standalone, installable libraries:

- `langgraph-checkpoint`: The base interface for checkpointer savers ([BaseCheckpointSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver)) and serialization/deserialization interface ([SerializerProtocol](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol)). Includes in-memory checkpointer implementation ([InMemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver)) for experimentation. LangGraph comes with `langgraph-checkpoint` included.
- `langgraph-checkpoint-sqlite`: An implementation of LangGraph checkpointer that uses SQLite database ([SqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver) / [AsyncSqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver)). Ideal for experimentation and local workflows. Needs to be installed separately.
- `langgraph-checkpoint-postgres`: An advanced checkpointer that uses Postgres database ([PostgresSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver) / [AsyncPostgresSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver)), used in LangGraph Platform. Ideal for using in production. Needs to be installed separately.





### Checkpointer interface

Each checkpointer conforms to [BaseCheckpointSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) interface and implements the following methods:

- `.put` - Store a checkpoint with its configuration and metadata.
- `.put_writes` - Store intermediate writes linked to a checkpoint (i.e. [pending writes](#pending-writes)).
- `.get_tuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `checkpoint_id`). This is used to populate `StateSnapshot` in `graph.get_state()`.
- `.list` - List checkpoints that match a given configuration and filter criteria. This is used to populate state history in `graph.get_state_history()`

If the checkpointer is used with asynchronous graph execution (i.e. executing the graph via `.ainvoke`, `.astream`, `.abatch`), asynchronous versions of the above methods will be used (`.aput`, `.aput_writes`, `.aget_tuple`, `.alist`).

!!! note

    For running your graph asynchronously, you can use `InMemorySaver`, or async versions of Sqlite/Postgres checkpointers -- `AsyncSqliteSaver` / `AsyncPostgresSaver` checkpointers.





### Serializer

When checkpointers save the graph state, they need to serialize the channel values in the state. This is done using serializer objects.

`langgraph_checkpoint` defines [protocol](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol) for implementing serializers provides a default implementation ([JsonPlusSerializer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer)) that handles a wide variety of types, including LangChain and LangGraph primitives, datetimes, enums and more.

#### Serialization with `pickle`

The default serializer, [`JsonPlusSerializer`](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer), uses ormsgpack and JSON under the hood, which is not suitable for all types of objects.

If you want to fallback to pickle for objects not currently supported by our msgpack encoder (such as Pandas dataframes),
you can use the `pickle_fallback` argument of the `JsonPlusSerializer`:

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer


# ... Define the graph ...
graph.compile(
    checkpointer=InMemorySaver(serde=JsonPlusSerializer(pickle_fallback=True))
)
```

#### Encryption

Checkpointers can optionally encrypt all persisted state. To enable this, pass an instance of [`EncryptedSerializer`](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.encrypted.EncryptedSerializer) to the `serde` argument of any `BaseCheckpointSaver` implementation. The easiest way to create an encrypted serializer is via [`from_pycryptodome_aes`](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.encrypted.EncryptedSerializer.from_pycryptodome_aes), which reads the AES key from the `LANGGRAPH_AES_KEY` environment variable (or accepts a `key` argument):

```python
import sqlite3

from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.checkpoint.sqlite import SqliteSaver

serde = EncryptedSerializer.from_pycryptodome_aes()  # reads LANGGRAPH_AES_KEY
checkpointer = SqliteSaver(sqlite3.connect("checkpoint.db"), serde=serde)
```

```python
from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.checkpoint.postgres import PostgresSaver

serde = EncryptedSerializer.from_pycryptodome_aes()
checkpointer = PostgresSaver.from_conn_string("postgresql://...", serde=serde)
checkpointer.setup()
```

When running on LangGraph Platform, encryption is automatically enabled whenever `LANGGRAPH_AES_KEY` is present, so you only need to provide the environment variable. Other encryption schemes can be used by implementing [`CipherProtocol`](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.CipherProtocol) and supplying it to `EncryptedSerializer`.





## Capabilities

### Human-in-the-loop

First, checkpointers facilitate [human-in-the-loop workflows](agentic_concepts.md#human-in-the-loop) workflows by allowing humans to inspect, interrupt, and approve graph steps. Checkpointers are needed for these workflows as the human has to be able to view the state of a graph at any point in time, and the graph has to be to resume execution after the human has made any updates to the state. See [the how-to guides](../how-tos/human_in_the_loop/add-human-in-the-loop.md) for examples.

### Memory

Second, checkpointers allow for ["memory"](../concepts/memory.md) between interactions. In the case of repeated human interactions (like conversations) any follow up messages can be sent to that thread, which will retain its memory of previous ones. See [Add memory](../how-tos/memory/add-memory.md) for information on how to add and manage conversation memory using checkpointers.

### Time Travel

Third, checkpointers allow for ["time travel"](time-travel.md), allowing users to replay prior graph executions to review and / or debug specific graph steps. In addition, checkpointers make it possible to fork the graph state at arbitrary checkpoints to explore alternative trajectories.

### Fault-tolerance

Lastly, checkpointing also provides fault-tolerance and error recovery: if one or more nodes fail at a given superstep, you can restart your graph from the last successful step. Additionally, when a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.

#### Pending writes

Additionally, when a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.


---
concepts/application_structure.md
---

---
search:
  boost: 2
---


# Application Structure


## Overview

A LangGraph application consists of one or more graphs, a configuration file (`langgraph.json`), a file that specifies dependencies, and an optional `.env` file that specifies environment variables.

This guide shows a typical structure of an application and shows how the required information to deploy an application using the LangGraph Platform is specified.


## Key Concepts

To deploy using the LangGraph Platform, the following information should be provided:

1. A [LangGraph configuration file](#configuration-file-concepts) (`langgraph.json`) that specifies the dependencies, graphs, and environment variables to use for the application.
2. The [graphs](#graphs) that implement the logic of the application.
3. A file that specifies [dependencies](#dependencies) required to run the application.
4. [Environment variables](#environment-variables) that are required for the application to run.


## File Structure

Below are examples of directory structures for applications:

=== "Python (requirements.txt)"

    ```plaintext
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for your graph
    │   │   └── state.py # state definition of your graph
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    ├── requirements.txt # package dependencies
    └── langgraph.json # configuration file for LangGraph
    ```

=== "Python (pyproject.toml)"

    ```plaintext
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for your graph
    │   │   └── state.py # state definition of your graph
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    ├── langgraph.json  # configuration file for LangGraph
    └── pyproject.toml # dependencies for your project
    ```





!!! note

    The directory structure of a LangGraph application can vary depending on the programming language and the package manager used.


## Configuration File {#configuration-file-concepts}

The `langgraph.json` file is a JSON file that specifies the dependencies, graphs, environment variables, and other settings required to deploy a LangGraph application.

See the [LangGraph configuration file reference](../cloud/reference/cli.md#configuration-file) for details on all supported keys in the JSON file.

!!! tip

    The [LangGraph CLI](./langgraph_cli.md) defaults to using the configuration file `langgraph.json` in the current directory.

### Examples

- The dependencies involve a custom local package and the `langchain_openai` package.
- A single graph will be loaded from the file `./your_package/your_file.py` with the variable `variable`.
- The environment variables are loaded from the `.env` file.

```json
{
  "dependencies": ["langchain_openai", "./your_package"],
  "graphs": {
    "my_agent": "./your_package/your_file.py:agent"
  },
  "env": "./.env"
}
```






## Dependencies

A LangGraph application may depend on other Python packages.




You will generally need to specify the following information for dependencies to be set up correctly:

1. A file in the directory that specifies the dependencies (e.g. `requirements.txt`, `pyproject.toml`, or `package.json`).




2. A `dependencies` key in the [LangGraph configuration file](#configuration-file-concepts) that specifies the dependencies required to run the LangGraph application.
3. Any additional binaries or system libraries can be specified using `dockerfile_lines` key in the [LangGraph configuration file](#configuration-file-concepts).


## Graphs

Use the `graphs` key in the [LangGraph configuration file](#configuration-file-concepts) to specify which graphs will be available in the deployed LangGraph application.

You can specify one or more graphs in the configuration file. Each graph is identified by a name (which should be unique) and a path for either: (1) the compiled graph or (2) a function that makes a graph is defined.


## Environment Variables

If you're working with a deployed LangGraph application locally, you can configure environment variables in the `env` key of the [LangGraph configuration file](#configuration-file-concepts).

For a production deployment, you will typically want to configure the environment variables in the deployment environment.


---
concepts/time-travel.md
---

---
search:
  boost: 2
---


# Time Travel ⏱️

When working with non-deterministic systems that make model-based decisions (e.g., agents powered by LLMs), it can be useful to examine their decision-making process in detail:

1. 🤔 **Understand reasoning**: Analyze the steps that led to a successful result.
2. 🐞 **Debug mistakes**: Identify where and why errors occurred.
3. 🔍 **Explore alternatives**: Test different paths to uncover better solutions.

LangGraph provides [time travel functionality](../how-tos/human_in_the_loop/time-travel.md) to support these use cases. Specifically, you can resume execution from a prior checkpoint — either replaying the same state or modifying it to explore alternatives. In all cases, resuming past execution produces a new fork in the history.

!!! tip

    For information on how to use time travel, see [Use time travel](../how-tos/human_in_the_loop/time-travel.md) and [Time travel using Server API](../cloud/how-tos/human_in_the_loop_time_travel.md).


---

**Navigation:** [← Previous](./04-node-that-uses-the-instructions.md) | [Index](./index.md)
