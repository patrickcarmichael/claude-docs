---
title: "Deploy Streamlit apps in Snowflake"
source: https://docs.streamlit.io/deploy/snowflake
section: 326
---

# Deploy Streamlit apps in Snowflake

Source: https://docs.streamlit.io/deploy/snowflake


Host your apps alongside your data in a single, global platform. Snowflake provides industry-leading features that ensure the highest levels of security for your account, users, data, and apps. If you're looking for an enterprise hosting solution, try Snowflake!

<TileContainer>
<Tile background="lightBlue-70" icon="rocket_launch" link="/get-started/installation/streamlit-in-snowflake" text="Create a free trial account and deploy an app with Streamlit in Snowflake." title="Streamlit in Snowflake Quickstart"/>
<Tile background="lightBlue-70" icon="code" link="https://github.com/Snowflake-Labs/snowflake-demo-streamlit" text="Explore a wide variety of example apps in Snowflake Labs' snowflake-demo-streamlit repository." title="Examples"/>
<Tile background="lightBlue-70" icon="book" link="https://docs.snowflake.com/user-guide-getting-started" text="Learn more in Snowflake's documentation." title="Get started with Snowflake"/>
</TileContainer>

There are three ways to host Streamlit apps in Snowflake:

<InlineCalloutContainer>
<InlineCallout bold="Streamlit in Snowflake." color="lightBlue-70" href="https://docs.snowflake.com/developer-guide/streamlit/about-streamlit" icon="bolt">Run your Streamlit app as a native object in Snowflake. Enjoy an in-browser editor and minimal work to configure your environment. Share your app with other users in your Snowflake account through role-based access control (RBAC). This is a great way to deploy apps internally for your business. Check out Snowflake docs!</InlineCallout>
<InlineCallout bold="Snowflake Native Apps." color="lightBlue-70" href="https://docs.snowflake.com/en/developer-guide/native-apps/adding-streamlit" icon="ac_unit">Package your app with data and share it with other Snowflake accounts. This is a great way to share apps and their underlying data with other organizations who use Snowflake. Check out Snowflake docs!</InlineCallout>
<InlineCallout bold="Snowpark Container Services." color="lightBlue-70" href="https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview" icon="web_asset">Deploy your app in a container that's optimized to run in Snowflake. This is the most flexible option, where you can use any library and assign a public URL to your app. Manage your allowed viewers through your Snowflake account. Check out Snowflake docs!</InlineCallout>
</InlineCalloutContainer>
<Note>

    Using Snowpark Container Services to deploy a Streamlit app requires a compute pool, which is not available in a trial account at this time.

</Note>

---

[← Previous](325-status-and-limitations-of-community-cloud.md) | [Index](index.md) | [Next →](index.md)
