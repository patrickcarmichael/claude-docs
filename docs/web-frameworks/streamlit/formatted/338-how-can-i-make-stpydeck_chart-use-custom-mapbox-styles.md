---
title: "How can I make st.pydeck_chart use custom Mapbox styles?"
source: https://docs.streamlit.io/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles
section: 338
---

# How can I make st.pydeck_chart use custom Mapbox styles?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles


If you are supplying a Mapbox token, but the resulting `pydeck_chart` doesn't show your custom Mapbox styles, please check that you are adding the Mapbox token to the Streamlit `config.toml` configuration file. Streamlit DOES NOT read Mapbox tokens from inside of a PyDeck specification (i.e. from inside of the Streamlit app). Please see this [forum thread](https://discuss.streamlit.io/t/deprecation-warning-deckgl-pydeck-maps-to-require-mapbox-token-for-production-usage/2982/10) for more information.

---

[← Previous](337-how-to-insert-elements-out-of-order.md) | [Index](index.md) | [Next →](index.md)
