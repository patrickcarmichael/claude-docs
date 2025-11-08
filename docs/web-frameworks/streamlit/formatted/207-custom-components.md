---
title: "Custom components"
source: https://docs.streamlit.io/develop/api-reference/custom-components
section: 207
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
```python
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
```python
</RefCard>
</TileContainer>

### Frontend (TypeScript)

<TileContainer>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib">
<h4>npm support code</h4>

Support code published through npm.

```bash
npm i @streamlit/component-v2-lib
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-component">
<h4>Component</h4>

Type alias for the component function.

```typescript
import { Component } from "@streamlit/component-v2-lib";
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-componentargs">
<h4>ComponentArgs</h4>

Type alias for the component arguments.

```typescript
import { ComponentArgs } from "@streamlit/component-v2-lib";
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-componentstate">
<h4>ComponentState</h4>

Type alias for the component state.

```typescript
import { ComponentState } from "@streamlit/component-v2-lib";
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/component-v2-lib-optionalcomponentcleanupfunction" size="two-third">
<h4>OptionalComponentCleanupFunction</h4>

Type alias for the component cleanup function.

```typescript
import { OptionalComponentCleanupFunction } from "@streamlit/component-v2-lib";
```python
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
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">
<h4>HTML</h4>

Display an HTML string in an iframe.

```python
from st.components.v1 import html
html(
    "<p>Foo bar.</p>"
)
```python
</RefCard>
<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">
<h4>iframe</h4>

Load a remote URL in an iframe.

```python
from st.components.v1 import iframe
iframe(
    "docs.streamlit.io"
)
```python
</RefCard>
</TileContainer>

---

[← Previous](197-connections-and-databases.md) | [Index](index.md) | [Next →](index.md)
