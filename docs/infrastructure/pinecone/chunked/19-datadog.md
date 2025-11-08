**Navigation:** [← Previous](./18-ai-engine.md) | [Index](./index.md) | [Next →](./20-set-environment-variables-for-api-keys.md)

# Datadog
Source: https://docs.pinecone.io/integrations/datadog

Monitoring Pinecone with Datadog

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

Datadog is a monitoring and analytics tool that can be used to determine performance metrics as well as event monitoring for infrastructure and cloud services. Use Datadog to:

* Optimize performance and control usage: Observe and track specific actions (e.g., request count) within Pinecone to identify application requests with high latency or usage. Monitor trends and gain actionable insights to improve resource utilization and reduce spend.
* Automatically alert on metrics: Get alerted when index fullness reaches a certain threshold. You can also create your own customized monitors to alert on specific metrics and thresholds.
* Locate and triage unexpected spikes in usage or latency: Quickly visualize anomalies in usage or latency in Pinecone's Datadog dashboard. View metrics over time to better understand trends and determine the severity of a spike.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

Follow these steps to monitor a Pinecone project with Datadog:

1. Go to the [Pinecone integration](https://app.datadoghq.com/integrations/pinecone) tile in Datadog.
2. Go to the **Configure** tab.
3. Click **+ Add New**.
4. Enter a project name to identify your project in Datadog.
5. Do not select an environment. This is a legacy setting.
6. Enter an [API key](/guides/projects/understanding-projects#api-keys) for the Pinecone project you want to monitor.
7. Enter the [project ID](/guides/projects/understanding-projects#project-ids) of the Pinecone project you want to monitor.
8. Save the configuration.

On the **Monitoring Resources** tab, you'll find dashboards for the pod-based and serverless indexes in your project and recommendations for [configuring monitors](https://docs.datadoghq.com/monitors/configuration/?tab=thresholdalert) using [Pinecone's metrics](/guides/production/monitoring#available-metrics).



# Datavolo
Source: https://docs.pinecone.io/integrations/datavolo



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Datavolo](https://datavolo.io/) helps data teams build multimodal data pipelines to support their AI initiatives. Every organization has their own private data that they need to incorporate into their AI apps, and a predominant pattern to do so has emerged: retrieval augmented generation (RAG).

Datavolo sources, transforms, and enriches data in a continuous, composable and customizable manner, landing the data in Pinecone for retrieval. This ensures organizations can securely access their unstructured data.

<PrimarySecondaryCTA primaryLabel="Get started" primaryHref="https://docs.datavolo.io/docs/product/Integrations/pinecone-setup" />



# Estuary
Source: https://docs.pinecone.io/integrations/estuary



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Estuary](https://estuary.dev/) builds real-time data pipelines that focus on moving data from sources to destinations with millisecond latency. It supports integrations with hundreds of systems including databases, warehouses, SaaS products and streaming solutions.

The Pinecone connector for Estuary enables users to source from these systems and push data to Pinecone, for an always up-to-date view. It incrementally updates source data to ensure that minimal credits are used when reaching out to get embeddings from providers prior to pushing them to Pinecone.

Estuary's Pinecone connector enables a variety of use cases like enabling LLM-based search across your organizations data and building intelligent recommendation systems. It can be set up in 5 minutes, without any engineering effort to maximize efficiency.

<PrimarySecondaryCTA primaryHref={"https://docs.estuary.dev/reference/Connectors/materialization-connectors/pinecone/"} primaryLabel={"Get started"} />



# Fleak
Source: https://docs.pinecone.io/integrations/fleak



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Fleak simplifies the process of building, deploying, and managing data workflows. As a low-code platform, Fleak lets users create and deploy complex workflows using SQL and pre-configured processing nodes. The platform facilitates seamless data processing, microservice interactions, and the inference of large language models (LLMs) within a single, intuitive environment. Fleak makes advanced technology accessible and manageable for Pinecone users without requiring extensive coding hours or infrastructure knowledge.

The platform provides serverless, autoscaling HTTP API endpoints, ensuring that workflows are robust, reliable, and scalable to meet the complex data needs of enterprises. This setup allows businesses to automate and enhance their operations, driving productivity and innovation through powerful, user-friendly tools.

By integrating Pinecone into Fleak's platform, users can access and leverage their vector data to enrich their workflows without additional engineering overhead, enabling seamless data-driven decision-making, advanced analytics, and the integration of AI-driven insights.

<PrimarySecondaryCTA primaryHref={"https://docs.fleak.ai/1.0/getting-started/pinecone-integration"} primaryLabel={"Get started"} />



# FlowiseAI
Source: https://docs.pinecone.io/integrations/flowise



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Flowise is a low-code LLM apps development platform. It supports integrations with dozens of systems, including databases and chat models.

The Pinecone integration with Flowise allows users to build RAG apps, including upserting and querying documents.

<PrimarySecondaryCTA primaryHref={"https://docs.flowiseai.com/integrations/langchain/vector-stores/pinecone"} primaryLabel={"Get started"} />



# Gathr
Source: https://docs.pinecone.io/integrations/gathr



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Gathr](https://www.gathr.one/) is the world's first and only "data to outcome" platform. Leading enterprises use Gathr to build and operationalize data and AI-driven solutions at scale.

Gathr unifies data engineering, machine learning, generative AI, actionable analytics, and process automation on a single platform. With Gen AI capabilities and no-code rapid application development, Gathr significantly boosts productivity for all. The unified experience fosters seamless handoff and collaboration between teams, accelerating the journey from prototype to production.

Users have achieved success with Gathr, from ingesting petabyte-scale data in real time to orchestrating thousands of complex data processing pipelines in months and delivering actionable insights and xOps solutions to multiply business impact. Additionally, Gathr helps enterprises architect Gen AI solutions for use cases like document summarization, sentiment analysis, next best action, insider threat detection, predictive maintenance, custom chatbots, and more.

Gathr Gen AI Fabric is designed to build enterprise-grade Gen AI solutions end-to-end on a unified platform. It offers production-ready building blocks for creating Gen AI solutions, out-of-the-box Gen AI solution templates, and GathrIQ, a data-to-outcome copilot.

One of the building blocks is integration with Vector DB and Knowledge Graphs. Gathr supports reading and writing from Pinecone using a built-in, ready-to-use connector to support use cases requiring knowledge graphs.

<PrimarySecondaryCTA primaryHref={"https://docs.gathr.one/gathr-saas/docs/components/pinecone/"} primaryLabel={"Get started"} />



# Genkit
Source: https://docs.pinecone.io/integrations/genkit



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

The [Genkit](https://firebase.google.com/docs/genkit) Pinecone plugin empowers developers to reduce the complexity of integrating AI components through simple indexers, embedders and retrievers abstractions. Through the Genkit Pinecone plugin, developers can integrate AI models with their own custom logic and data to build AI features optimized for their businesses.

Additionally, developers can analyze unstructured text, generate creative content, select tasks, and send results back to their app as structured type-safe objects.
The plugin provides a common format for content that supports combinations of text, data, and other media. Developers can use Genkit for models that perform any generative task (such as image generation), not just LLMs.

<PrimarySecondaryCTA primaryLabel="Get started" primaryHref="https://firebase.google.com/docs/genkit/plugins/pinecone" />



# GitHub Copilot
Source: https://docs.pinecone.io/integrations/github-copilot



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Access the Pinecone Copilot Extension through our GitHub Marketplace listing. The Pinecone Copilot Extension serves as a seamless bridge between you and your Pinecone data-- providing product information, coding assistance, troubleshooting capabilities and streamlining the debugging process.

This extension offers personalized recommendations right to your fingertips, enabling you to swiftly retrieve relevant data and collaborate effectively with Copilot.

<PrimarySecondaryCTA
  primaryLabel={"Get started"}
  primaryHref={
  "https://github.com/marketplace/pinecone-ai"
}
/>



# Google Cloud Marketplace
Source: https://docs.pinecone.io/integrations/google-cloud-marketplace



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Access Pinecone through our Google Cloud Marketplace listing. Google Cloud Marketplace allows you to manage Pinecone and other third-party software from a centralized location, and simplifies software licensing and procurement with flexible pricing options and multiple deployment methods.

You can set up pay-as-you-go billing for a Pinecone organization through the Google Cloud Marketplace.

<PrimarySecondaryCTA primaryLabel={"Get started"} primaryHref={"https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone"} />



# Haystack
Source: https://docs.pinecone.io/integrations/haystack

Using Haystack and Pinecone to keep your NLP-driven apps up-to-date

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Haystack is the open source Python framework by Deepset for building custom apps with large language models (LLMs). It lets you quickly try out the latest models in natural language processing (NLP) while being flexible and easy to use. Their community of users and builders has helped shape Haystack into what it is today: a complete framework for building production-ready NLP apps.

Haystack and Pinecone integration can be used to keep your NLP-driven apps up-to-date with Haystack's indexing pipelines that help you prepare and maintain your data.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

In this guide we will see how to integrate Pinecone and the popular [Haystack library](https://github.com/deepset-ai/haystack) for *Question-Answering*.

### Install Haystack

We start by installing the latest version of Haystack with all dependencies required for the `PineconeDocumentStore`.

```Python Python theme={null}
pip install -U farm-haystack>=1.3.0 pinecone[grpc] datasets
```

### Initialize the PineconeDocumentStore

We initialize a `PineconeDocumentStore` by providing an API key and environment name. [Create an account](https://app.pinecone.io) to get your free API key.

```Python Python theme={null}
from haystack.document_stores import PineconeDocumentStore

document_store = PineconeDocumentStore(
    api_key='<YOUR_API_KEY>',
    index='haystack-extractive-qa',
    similarity="cosine",
    embedding_dim=384
)
```

```
INFO - haystack.document_stores.pinecone -  Index statistics: name: haystack-extractive-qa, embedding dimensions: 384, record count: 0
```

### Prepare data

Before adding data to the document store, we must download and convert data into the Document format that Haystack uses.

We will use the SQuAD dataset available from Hugging Face Datasets.

```Python Python theme={null}
from datasets import load_dataset


# load the squad dataset
data = load_dataset("squad", split="train")
```

Next, we remove duplicates and unecessary columns.

```Python Python theme={null}

# convert to a pandas dataframe
df = data.to_pandas()

# select only title and context column
df = df[["title", "context"]]

# drop rows containing duplicate context passages
df = df.drop_duplicates(subset="context")
df.head()
```

| title | context                     |                                                   |
| ----- | --------------------------- | ------------------------------------------------- |
| 0     | University\_of\_Notre\_Dame | Architecturally, the school has a Catholic cha... |
| 5     | University\_of\_Notre\_Dame | As at most other universities, Notre Dame's st... |
| 10    | University\_of\_Notre\_Dame | The university is the major seat of the Congre... |
| 15    | University\_of\_Notre\_Dame | The College of Engineering was established in ... |
| 20    | University\_of\_Notre\_Dame | All of Notre Dame's undergraduate students are... |

Then convert these records into the Document format.

```Python Python theme={null}
from haystack import Document

docs = []
for d in df.iterrows():
    d = d[1]
    # create haystack document object with text content and doc metadata
    doc = Document(
        content=d["context"],
        meta={
            "title": d["title"],
            'context': d['context']
        }
    )
    docs.append(doc)
```

This `Document` format contains two fields; *'content'* for the text content or paragraphs, and *'meta'* where we can place any additional information that can later be used to apply metadata filtering in our search.

Now we upsert the documents to Pinecone.

```Python Python theme={null}

# upsert the data document to pinecone index
document_store.write_documents(docs)
```

### Initialize retriever

The next step is to create embeddings from these documents. We will use Haystacks `EmbeddingRetriever` with a SentenceTransformer model (`multi-qa-MiniLM-L6-cos-v1`) which has been designed for question-answering.

```Python Python theme={null}
from haystack.retriever.dense import EmbeddingRetriever

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="multi-qa-MiniLM-L6-cos-v1",
    model_format="sentence_transformers"
)
```

Then we run the `PineconeDocumentStore.update_embeddings` method with the `retriever` provided as an argument. GPU acceleration can greatly reduce the time required for this step.

```Python Python theme={null}
document_store.update_embeddings(
    retriever,
    batch_size=16
)
```

### Inspect documents and embeddings

We can get documents by their ID with the `PineconeDocumentStore.get_documents_by_id` method.

```Python Python theme={null}
d = document_store.get_documents_by_id(ids=['49091c797d2236e73fab510b1e9c7f6b'], return_embedding=True)[0]
```

From here we return can view document content with `d.content` and the document embedding with `d.embedding`.

### Initialize an extractive QA pipeline

An `ExtractiveQAPipeline` contains three key components by default:

* a document store (`PineconeDocumentStore`)
* a retriever model
* a reader model

We use the `deepset/electra-base-squad2` model from the HuggingFace model hub as our reader model.

```Python Python theme={null}
from haystack.nodes import FARMReader

reader = FARMReader(
    model_name_or_path='deepset/electra-base-squad2', 
    use_gpu=True
)
```

We are now ready to initialize the `ExtractiveQAPipeline`.

```Python Python theme={null}
from haystack.pipelines import ExtractiveQAPipeline

pipe = ExtractiveQAPipeline(reader, retriever)
```

### Ask Questions

Using our QA pipeline we can begin querying with `pipe.run`.

```Python Python theme={null}
from haystack.utils import print_answers

query = "What was Albert Einstein famous for?"

# get the answer
answer = pipe.run(
    query=query,
    params={
        "Retriever": {"top_k": 1},
    }
)

# print the answer(s)
print_answers(answer)
```

```
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.53 Batches/s]

Query: What was Albert Einstein famous for?
Answers:
[   <Answer {
    'answer': 'his theories of special relativity and general relativity', 'type': 'extractive', 'score': 0.993550717830658,
    'context': 'Albert Einstein is known for his theories of special relativity and general relativity. He also made important contributions to statistical mechanics,',
    'offsets_in_document': [{'start': 29, 'end': 86}],
    'offsets_in_context': [{'start': 29, 'end': 86}], 
    'document_id': '23357c05e3e46bacea556705de1ea6a5',
    'meta': {
        'context': 'Albert Einstein is known for his theories of special relativity and general relativity. He also made important contributions to statistical mechanics, especially his mathematical treatment of Brownian motion, his resolution of the paradox of specific heats, and his connection of fluctuations and dissipation. Despite his reservations about its interpretation, Einstein also made contributions to quantum mechanics and, indirectly, quantum field theory, primarily through his theoretical studies of the photon.', 'title': 'Modern_history'
    }
}>]
```

```Python Python theme={null}
query = "How much oil is Egypt producing in a day?"

# get the answer
answer = pipe.run(
    query=query,
    params={
        "Retriever": {"top_k": 1},
    }
)

# print the answer(s)
print_answers(answer)
```

```
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.81 Batches/s]

Query: How much oil is Egypt producing in a day?
Answers:
[   <Answer {
    'answer': '691,000 bbl/d', 'type': 'extractive', 'score': 0.9999906420707703,
    'context': 'Egypt was producing 691,000 bbl/d of oil and 2,141.05 Tcf of natural gas (in 2013), which makes Egypt as the largest oil producer not member of the Or',
    'offsets_in_document': [{'start': 20, 'end': 33}],
    'offsets_in_context': [{'start': 20, 'end': 33}],
    'document_id': '57ed9720050a17237e323da5e3969a9b',
    'meta': {
        'context': 'Egypt was producing 691,000 bbl/d of oil and 2,141.05 Tcf of natural gas (in 2013), which makes Egypt as the largest oil producer not member of the Organization of the Petroleum Exporting Countries (OPEC) and the second-largest dry natural gas producer in Africa. In 2013, Egypt was the largest consumer of oil and natural gas in Africa, as more than 20% of total oil consumption and more than 40% of total dry natural gas consumption in Africa. Also, Egypt possesses the largest oil refinery capacity in Africa 726,000 bbl/d (in 2012). Egypt is currently planning to build its first nuclear power plant in El Dabaa city, northern Egypt.', 'title': 'Egypt'
    }
}>]
```

```Python Python theme={null}
query = "What are the first names of the youtube founders?"

# get the answer
answer = pipe.run(
    query=query,
    params={
        "Retriever": {"top_k": 1},
    }
)

# print the answer(s)
print_answers(answer)
```

```
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.83 Batches/s]

Query: What are the first names of the youtube founders?
Answers:
[   <Answer {
    'answer': 'Hurley and Chen', 'type': 'extractive', 'score': 0.9998972713947296,
    'context': 'According to a story that has often been repeated in the media, Hurley and Chen developed the idea for YouTube during the early months of 2005, after ',
    'offsets_in_document': [{'start': 64, 'end': 79}],
    'offsets_in_context': [{'start': 64, 'end': 79}],
    'document_id': 'bd1cbd61ab617d840c5f295e21e80092',
    'meta': {
        'context': 'According to a story that has often been repeated in the media, Hurley and Chen developed the idea for YouTube during the early months of 2005, after they had experienced difficulty sharing videos that had been shot at a dinner party at Chen\'s apartment in San Francisco. Karim did not attend the party and denied that it had occurred, but Chen commented that the idea that YouTube was founded after a dinner party "was probably very strengthened by marketing ideas around creating a story that was very digestible".', 'title': 'YouTube'
    }
}>]
```

We can return multiple answers by setting the `top_k` parameter.

```Python Python theme={null}
query = "Who was the first person to step foot on the moon?"

# get the answer
answer = pipe.run(
    query=query,
    params={
        "Retriever": {"top_k": 3},
    }
)

# print the answer(s)
print_answers(answer)
```

```
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.71 Batches/s]
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.78 Batches/s]
Inferencing Samples: 100%|██████████| 1/1 [00:00<00:00,  3.88 Batches/s]

Query: Who was the first person to step foot on the moon?
Answers:
[   <Answer {
    'answer': 'Armstrong', 'type': 'extractive', 'score': 0.9998227059841156, 
    'context': 'The trip to the Moon took just over three days. After achieving orbit, Armstrong and Aldrin transferred into the Lunar Module, named Eagle, and after ', 
    'offsets_in_document': [{'start': 71, 'end': 80}], 
    'offsets_in_context': [{'start': 71, 'end': 80}], 
    'document_id': 'f74e1bf667e68d72e45437a7895df921', 
    'meta': {
        'context': 'The trip to the Moon took just over three days. After achieving orbit, Armstrong and Aldrin transferred into the Lunar Module, named Eagle, and after a landing gear inspection by Collins remaining in the Command/Service Module Columbia, began their descent. After overcoming several computer overload alarms caused by an antenna switch left in the wrong position, and a slight downrange error, Armstrong took over manual flight control at about 180 meters (590 ft), and guided the Lunar Module to a safe landing spot at 20:18:04 UTC, July 20, 1969 (3:17:04 pm CDT). The first humans on the Moon would wait another six hours before they ventured out of their craft. At 02:56 UTC, July 21 (9:56 pm CDT July 20), Armstrong became the first human to set foot on the Moon.', 'title': 'Space_Race'
        }
    }>, <Answer {
    'answer': 'Frank Borman', 'type': 'extractive', 'score': 0.7770257890224457, 
    'context': 'On December 21, 1968, Frank Borman, James Lovell, and William Anders became the first humans to ride the Saturn V rocket into space on Apollo 8. They ', 
    'offsets_in_document': [{'start': 22, 'end': 34}], 
    'offsets_in_context': [{'start': 22, 'end': 34}], 
    'document_id': '2bc046ba90d94fe201ccde9d20552200', 
    'meta': {
        'context': "On December 21, 1968, Frank Borman, James Lovell, and William Anders became the first humans to ride the Saturn V rocket into space on Apollo 8. They also became the first to leave low-Earth orbit and go to another celestial body, and entered lunar orbit on December 24. They made ten orbits in twenty hours, and transmitted one of the most watched TV broadcasts in history, with their Christmas Eve program from lunar orbit, that concluded with a reading from the biblical Book of Genesis. Two and a half hours after the broadcast, they fired their engine to perform the first trans-Earth injection to leave lunar orbit and return to the Earth. Apollo 8 safely landed in the Pacific ocean on December 27, in NASA's first dawn splashdown and recovery.", 'title': 'Space_Race'
        }
    }>, <Answer {
    'answer': 'Aldrin', 'type': 'extractive', 'score': 0.6680101901292801, 
    'context': ' were, "That\'s one small step for [a] man, one giant leap for mankind." Aldrin joined him on the surface almost 20 minutes later. Altogether, they spe', 
    'offsets_in_document': [{'start': 240, 'end': 246}], 
    'offsets_in_context': [{'start': 72, 'end': 78}], 
    'document_id': 'ae1c366b1eaf5fc9d32a8d81f76bd795', 
    'meta': {
        'context': 'The first step was witnessed by at least one-fifth of the population of Earth, or about 723 million people. His first words when he stepped off the LM\'s landing footpad were, "That\'s one small step for [a] man, one giant leap for mankind." Aldrin joined him on the surface almost 20 minutes later. Altogether, they spent just under two and one-quarter hours outside their craft. The next day, they performed the first launch from another celestial body, and rendezvoused back with Columbia.', 'title': 'Space_Race'
        }
    }>
]
```



# Hugging Face Inference Endpoints
Source: https://docs.pinecone.io/integrations/hugging-face-inference-endpoints

Using Hugging Face Inference Endpoints and Pinecone to generate and index high-quality vector embeddings

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Hugging Face Inference Endpoints offers a secure production solution to easily deploy any Hugging Face Transformers, Sentence-Transformers and Diffusion models from the Hub on dedicated and autoscaling infrastructure managed by Hugging Face.

Coupled with Pinecone, you can use Hugging Face to generate and index high-quality vector embeddings with ease.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

Hugging Face Inference Endpoints allows access to straightforward model inference. Coupled with Pinecone we can generate and index high-quality vector embeddings with ease.

Let's get started by initializing an Inference Endpoint for generating vector embeddings.

### Create an endpoint

We start by heading over to the [Hugging Face Inference Endpoints homepage](https://ui.endpoints.huggingface.co/endpoints) and signing up for an account if needed. After, we should find ourselves on this page:

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=193e39d5e65bb87b3b1b1b0d429180b6" alt="endpoints 0" data-og-width="1622" width="1622" data-og-height="936" height="936" data-path="images/hf-endpoints-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a93797264f78198d1dee10c2a1fe820a 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8f4799ed2133a717e22e78aa2cf0f245 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7afce26d262b3f4a30933214e6274ca0 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d3e1e36538d3684c13b371cb1f2ede96 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=02472896f27429a4f7655faf8abb1c3f 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=df1732e3534af7e1ffb4e55dc6b33245 2500w" />

We click on **Create new endpoint**, choose a model repository (eg name of the model), endpoint name (this can be anything), and select a cloud environment. Before moving on it is *very important* that we set the **Task** to **Sentence Embeddings** (found within the *Advanced configuration* settings).

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=322d411596affb620805d391d824c863" alt="endpoints 1" data-og-width="1622" width="1622" data-og-height="1196" height="1196" data-path="images/hf-endpoints-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=094ffc9c6babf9f1fa1060d214063d5d 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3a794a6a789b7a2082b2147f1d79cc57 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0556363ec9cb927bc76433c4f7525072 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2191bb241e7042f790baac1d5323b18d 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3f1f41f28c98a2c1944d15802cc3ea01 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7ab0e0991b83c12202d8986e8182a292 2500w" />

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=db8b7952c2d42d939b6764cb39f62a7d" alt="endpoints 2" data-og-width="1548" width="1548" data-og-height="354" height="354" data-path="images/hf-endpoints-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8b8ddd85cddf0b44fdfb12c5d828e200 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3cf09f91cc295046fd8cdeef7f95f617 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=59fed1c0984ab4fcdb9ed8cd0a14512d 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=67b3dfd3362eecf6dd0cacaa5988ed8c 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=aa7577163d22caa6dd4032a926acd9f4 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d9ce21fa370f79c7d5acd8a9651aa3e7 2500w" />

Other important options include the *Instance Type*, by default this uses CPU which is cheaper but also slower. For faster processing we need a GPU instance. And finally, we set our privacy setting near the end of the page.

After setting our options we can click **Create Endpoint** at the bottom of the page. This action should take use to the next page where we will see the current status of our endpoint.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=925a8437da312a756edf0a1bdbac16e0" alt="endpoints 3" data-og-width="1548" width="1548" data-og-height="112" height="112" data-path="images/hf-endpoints-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a08a7a0a590037b0f959fd94f5563006 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=bd7b7970fbd20dae84dc2116dd6647f5 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6202139573fbda7e1b2cbe71c0ddd7a9 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2542fa57778a6a81d564e1e39bf5ba6f 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3ff523c988657e3dbdfcc8bc374a374d 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=37ba16c888d5f1dfc1c0ad60480ae57e 2500w" />

Once the status has moved from **Building** to **Running** (this can take some time), we're ready to begin creating embeddings with it.


## Create embeddings

Each endpoint is given an **Endpoint URL**, it can be found on the endpoint **Overview** page. We need to assign this endpoint URL to the `endpoint_url` variable.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=af3da5b0476bec94258c3cc711fd8b47" alt="endpoints 4" data-og-width="1404" width="1404" data-og-height="222" height="222" data-path="images/hf-endpoints-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=26b6d9ed0620c27e4982f99b6427f3df 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=281c535c7fe5e8fa90f1cb267fd922a6 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0a037b4ca662219475cacc73d1243262 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7df385446234a0f87c199b3748fe6f0b 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=eda7a0dd9a7424ab38a6eeb49c5256af 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2bc2d005700830aa2660cfd6afa723a4 2500w" />

```Python Python theme={null}
endpoint = "<ENDPOINT_URL>"
```

We will also need the organization API token, we find this via the organization settings on Hugging Face (`https://huggingface.co/organizations/<ORG_NAME>/settings/profile`). This is assigned to the `api_org` variable.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=41b16cbb97439082bbd4a4c7e76c662d" alt="endpoints 5" data-og-width="2230" width="2230" data-og-height="1120" height="1120" data-path="images/hf-endpoints-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=81ba23ffdce70a192ee85f22d4cb525f 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=be1170a4cc6f68a9ec56252dfcff73b0 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e64873c28eb2937436cde6d91a33990a 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=40ccf67ba795afd1a2b3d1ca7ec39efe 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1d9f9593f03a500ae85698d07e86c5cf 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e154eaafeb63a69100d2a73e55edd2ce 2500w" />

```Python Python theme={null}
api_org = "<API_ORG_TOKEN>"
```

Now we're ready to create embeddings via Inference Endpoints. Let's start with a toy example.

```Python Python theme={null}
import requests


# add the api org token to the headers
headers = {
    'Authorization': f'Bearer {api_org}'
}

# we add sentences to embed like so
json_data = {"inputs": ["a happy dog", "a sad dog"]}

# make the request
res = requests.post(
    endpoint,
    headers=headers,
    json=json_data
)
```

We should see a `200` response.

```Python Python theme={null}
res
```

```
<Response [200]>
```

Inside the response we should find two embeddings...

```Python Python theme={null}
len(res.json()['embeddings'])
```

```
2
```

We can also see the dimensionality of our embeddings like so:

```Python Python theme={null}
dim = len(res.json()['embeddings'][0])
dim
```

```
768
```

We will need more than two items to search through, so let's download a larger dataset. For this we will use Hugging Face datasets.

```Python Python theme={null}
from datasets import load_dataset

snli = load_dataset("snli", split='train')
snli
```

```
Downloading: 100%|██████████| 1.93k/1.93k [00:00<00:00, 992kB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 31.2MB/s]
Downloading: 100%|██████████| 65.9M/65.9M [00:01<00:00, 57.9MB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 43.6MB/s]

Dataset({
    features: ['premise', 'hypothesis', 'label'],
    num_rows: 550152
})
```

SNLI contains 550K sentence pairs, many of these include duplicate items so we will take just one set of these (the *hypothesis*) and deduplicate them.

```Python  theme={null}
passages = list(set(snli['hypothesis']))
len(passages)
```

```
480042
```

We will drop to 50K sentences so that the example is quick to run, if you have time, feel free to keep the full 480K.

```Python Python theme={null}
passages = passages[:50_000]
```


## Create a Pinecone index

With our endpoint and dataset ready, all that we're missing is a vector database. For this, we need to initialize our connection to Pinecone, this requires a [free API key](https://app.pinecone.io/).

```Python Python theme={null}
import pinecone


# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENVIRONMENT")

```

Now we create a new index called `'hf-endpoints'`, the name isn't important *but* the `dimension` must align to our endpoint model output dimensionality (we found this in `dim` above) and the model metric (typically `cosine` is okay, but not for all models).

```Python Python theme={null}
index_name = 'hf-endpoints'


# check if the hf-endpoints index exists
if index_name not in pinecone.list_indexes():
    # create the index if it does not exist
    pinecone.create_index(
        index_name,
        dimension=dim,
        metric="cosine"
    )


# connect to hf-endpoints index we created
index = pinecone.Index(index_name)
```


## Create and index embeddings

Now we have all of our components ready; endpoints, dataset, and Pinecone. Let's go ahead and create our dataset embeddings and index them within Pinecone.

```Python Python theme={null}
from tqdm.auto import tqdm


# we will use batches of 64
batch_size = 64

for i in tqdm(range(0, len(passages), batch_size)):
    # find end of batch
    i_end = min(i+batch_size, len(passages))
    # extract batch
    batch = passages[i:i_end]
    # generate embeddings for batch via endpoints
    res = requests.post(
        endpoint,
        headers=headers,
        json={"inputs": batch}
    )
    emb = res.json()['embeddings']
    # get metadata (just the original text)
    meta = [{'text': text} for text in batch]
    # create IDs
    ids = [str(x) for x in range(i, i_end)]
    # add all to upsert list
    to_upsert = list(zip(ids, emb, meta))
    # upsert/insert these records to pinecone
    _ = index.upsert(vectors=to_upsert)


# check that we have all vectors in index
index.describe_index_stats()
```

```
100%|██████████| 782/782 [11:02<00:00,  1.18it/s]

{'dimension': 768,
 'index_fullness': 0.1,
 'namespaces': {'': {'vector_count': 50000}},
 'total_vector_count': 50000}
```

With everything indexed we can begin querying. We will take a few examples from the *premise* column of the dataset.

```Python Python theme={null}
query = snli['premise'][0]
print(f"Query: {query}")

# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']

# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)

# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: A person on a horse jumps over a broken down airplane.
Answers:
The horse jumps over a toy airplane.
a lady rides a horse over a plane shaped obstacle
A person getting onto a horse.
person rides horse
A woman riding a horse jumps over a bar.
```

These look good, let's try a couple more examples.

```Python Python theme={null}
query = snli['premise'][100]
print(f"Query: {query}")

# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']

# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)

# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: A woman is walking across the street eating a banana, while a man is following with his briefcase.
Answers:
A woman eats a banana and walks across a street, and there is a man trailing behind her.
A woman eats a banana split.
A woman is carrying two small watermelons and a purse while walking down the street.
The woman walked across the street.
A woman walking on the street with a monkey on her back.
```

And one more...

```Python Python theme={null}
query = snli['premise'][200]
print(f"Query: {query}")

# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']

# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)

# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: People on bicycles waiting at an intersection.
Answers:
A pair of people on bikes are waiting at a stoplight.
Bike riders wait to cross the street.
people on bicycles
Group of bike riders stopped in the street.
There are bicycles outside.
```

All of these results look excellent. If you are not planning on running your endpoint and vector DB beyond this tutorial, you can shut down both.


## Clean up

Shut down the endpoint by navigating to the Inference Endpoints **Overview** page and selecting **Delete endpoint**. Delete the Pinecone index with:

```Python Python theme={null}
pinecone.delete_index(index_name)
```

<Note>Once the index is deleted, you cannot use it again.</Note>



# Instill AI
Source: https://docs.pinecone.io/integrations/instill



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Instill AI specializes in developing cutting-edge solutions for data, models, and pipeline orchestration. Their flagship source-available product, Instill Core, is a no-code/low-code platform designed to facilitate the development, deployment, and management of AI workflows. By simplifying the integration of various AI models and data sources, they enable businesses to harness the power of AI without requiring extensive technical expertise. Their solutions cater to a wide range of applications, from predictive analytics and autonomous AI agents to enterprise private knowledge bases, AI assistants, and beyond.

The Pinecone integration with Instill allows developers to incorporate its API for vector upsert and query tasks into AI pipelines. Developers configure their Pinecone component within Instill Core by providing the necessary API key and base URL. They can then perform tasks such as querying vector similarities to retrieve the most relevant results, complete with metadata and similarity scores, or upserting new vector data to keep their datasets up-to-date. This integration enables the addition of knowledge to LLMs via Retrieval Augmented Generation (RAG), significantly enhancing the capabilities of autonomous agents, chatbots, question-answering systems, and multi-agent systems.

<PrimarySecondaryCTA primaryHref={"https://www.instill.tech/docs/component/data/pinecone"} primaryLabel={"Get started"} />



# Jina AI
Source: https://docs.pinecone.io/integrations/jina



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Jina Embeddings leverage powerful models to generate high-quality text embeddings that can process inputs up to 8,000 tokens. Jina Embeddings are designed to be highly versatile, catering to both domain-specific use cases, such as e-commerce, and language-specific needs, including Chinese and German. By providing robust models and the expertise to fine-tune them for specific requirements, Jina AI empowers developers to enhance their search functionalities, improve natural language understanding, and drive more insightful data analysis.

By integrating Pinecone with Jina, you can add knowledge to LLMs via retrieval augmented generation (RAG), greatly enhancing LLM ability for autonomous agents, chatbots, question-answering, and multi-agent systems.

<PrimarySecondaryCTA primaryHref={"https://jina.ai/embeddings/#apiform"} primaryLabel={"Get started"} primaryTarget={"_blank"} secondaryHref={"https://www.pinecone.io/models/jina-embeddings-v2-base-en/"} secondaryLabel={"Try the model"} />



# LangChain
Source: https://docs.pinecone.io/integrations/langchain

Using LangChain and Pinecone to add knowledge to LLMs

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

LangChain provides modules for managing and optimizing the use of large language models (LLMs) in applications. Its core philosophy is to facilitate data-aware applications where the language model interacts with other data sources and its environment. This framework consists of several parts that simplify the entire application lifecycle:

* Write your applications in LangChain/LangChain.js. Get started quickly by using Templates for reference.
* Use LangSmith to inspect, test, and monitor your chains to constantly improve and deploy with confidence.
* Turn any chain into an API with LangServe.

By integrating Pinecone with LangChain, you can add knowledge to LLMs via retrieval augmented generation (RAG), greatly enhancing LLM ability for autonomous agents, chatbots, question-answering, and multi-agent systems.

<PrimarySecondaryCTA primaryHref={"https://github.com/langchain-ai/pinecone-serverless"} primaryLabel={"Get started"} primaryTarget={"_blank"} secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

This guide shows you how to integrate Pinecone, a high-performance vector database, with [LangChain](https://www.langchain.com/), a framework for building applications powered by large language models (LLMs).

Pinecone enables developers to build scalable, real-time recommendation and search systems based on vector similarity search. LangChain, on the other hand, provides modules for managing and optimizing the use of language models in applications. Its core philosophy is to facilitate data-aware applications where the language model interacts with other data sources and its environment.

By integrating Pinecone with LangChain, you can add knowledge to LLMs via [Retrieval Augmented Generation (RAG)](https://www.pinecone.io/learn/series/rag/), greatly enhancing LLM ability for autonomous agents, chatbots, question-answering, and multi-agent systems.

<Note>
  This guide demonstrates only one way out of many that you can use LangChain and Pinecone together. For additional examples, see:

  * [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/)
  * [Retrieval Augmentation for LLMs](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb)
  * [Retrieval Augmented Conversational Agent](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/08-langchain-retrieval-agent.ipynb)
</Note>


## Key concepts

The `PineconeVectorStore` class provided by LangChain can be used to interact with Pinecone indexes. It's important to remember that you must have an existing Pinecone index before you can create a `PineconeVectorStore` object.

### Initializing a vector store

To initialize a `PineconeVectorStore` object, you must provide the name of the Pinecone index and an `Embeddings` object initialized through LangChain. There are two general approaches to initializing a `PineconeVectorStore` object:

1. Initialize without adding records:

```Python Python theme={null}
    import os
    from langchain_pinecone import PineconeVectorStore
    from langchain_openai import OpenAIEmbeddings

    os.environ['OPENAI_API_KEY'] = '<YOUR_OPENAI_API_KEY>'
    os.environ['PINECONE_API_KEY'] = '<YOUR_PINECONE_API_KEY>'

    index_name = "<YOUR_PINECONE_INDEX_NAME>"
    embeddings = OpenAIEmbeddings()

    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
```

You can also use the `from_existing_index` method of LangChain's `PineconeVectorStore` class to initialize a vector store.

2. Initialize while adding records:

The `from_documents` and `from_texts` methods of LangChain's `PineconeVectorStore` class add records to a Pinecone index and return a `PineconeVectorStore` object.

The `from_documents` method accepts a list of LangChain's `Document` class objects, which can be created using LangChain's `CharacterTextSplitter` class. The `from_texts` method accepts a list of strings. Similarly to above, you must provide the name of an existing Pinecone index and an `Embeddings` object.

Both of these methods handle the embedding of the provided text data and the creation of records in your Pinecone index.

```Python Python theme={null}
    import os
    from langchain_pinecone import PineconeVectorStore
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import CharacterTextSplitter

    os.environ['OPENAI_API_KEY'] = '<YOUR_OPENAI_API_KEY>'
    os.environ['PINECONE_API_KEY'] = '<YOUR_PINECONE_API_KEY>'

    index_name = "<YOUR_PINECONE_INDEX_NAME>"
    embeddings = OpenAIEmbeddings()

    # path to an example text file
    loader = TextLoader("../../modules/state_of_the_union.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    vectorstore_from_docs = PineconeVectorStore.from_documents(
        docs,
        index_name=index_name,
        embedding=embeddings
    )

    texts = ["Tonight, I call on the Senate to: Pass the Freedom to Vote Act.", "ne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.", "One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence."]

    vectorstore_from_texts = PineconeVectorStore.from_texts(
        texts,
        index_name=index_name,
        embedding=embeddings
    )
```

### Add more records

Once you have initialized a `PineconeVectorStore` object, you can add more records to the underlying Pinecone index (and thus also the linked LangChain object) using either the `add_documents` or `add_texts` methods.

Like their counterparts that also initialize a `PineconeVectorStore` object, both of these methods also handle the embedding of the provided text data and the creation of records in your Pinecone index.

```Python Python theme={null}
    # path to an example text file
    loader = TextLoader("../../modules/inaugural_address.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

    vectorstore.add_documents(docs)
```

```Python Python theme={null}
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

    vectorstore.add_texts(["More text to embed and add to the index!"])
```

### Perform a similarity search

A `similarity_search` on a `PineconeVectorStore` object returns a list of LangChain `Document` objects most similar to the query provided. While the `similarity_search` uses a Pinecone query to find the most similar results, this method includes additional steps and returns results of a different type.

The `similarity_search` method accepts raw text and automatically embeds it using the `Embedding` object provided when you initialized the `PineconeVectorStore`. You can also provide a `k` value to determine the number of LangChain `Document` objects to return. The default value is `k=4`.

```Python Python theme={null}
    query = "Who is Ketanji Brown Jackson?"
    vectorstore.similarity_search(query)
    
    # Response:
    # [
    #    Document(page_content='Ketanji Onyika Brown Jackson is an American lawyer and jurist who is an associate justice of the Supreme Court of the United...', metadata={'chunk': 0.0, 'source': 'https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson', 'title': 'Ketanji Brown Jackson', 'wiki-id': '6573'}),  
    #    Document(page_content='Jackson was nominated to the Supreme Court by President Joe Biden on February 25, 2022, and confirmed by the U.S. Senate...', metadata={'chunk': 1.0, 'source': 'https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson', 'title': 'Ketanji Brown Jackson', 'wiki-id': '6573'}),  
    #    Document(page_content='Jackson grew up in Miami and attended Miami Palmetto Senior High School. She distinguished herself as a champion debater...', metadata={'chunk': 3.0, 'source': 'https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson', 'title': 'Ketanji Brown Jackson', 'wiki-id': '6573'}),
    #    Document(page_content='After high school, Jackson matriculated at Harvard University to study government, having applied despite her guidance...', metadata={'chunk': 5.0, 'source': 'https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson', 'title': 'Ketanji Brown Jackson', 'wiki-id': '6573'})
    # ]   
```

You can also optionally apply a metadata filter to your similarity search. The filtering query language is the same as for Pinecone queries, as detailed in [Filtering with metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).

```Python Python theme={null}
    query = "Tell me more about Ketanji Brown Jackson."
    vectorstore.similarity_search(query, filter={'source': 'https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson'})
```

### Namespaces

Several methods of the `PineconeVectorStore` class support using [namespaces](/guides/index-data/indexing-overview#namespaces). You can also initialize your `PineconeVectorStore` object with a namespace to restrict all further operations to that space.

```Python Python theme={null}
    index_name = "<YOUR_PINECONE_INDEX_NAME>"
    embeddings = OpenAIEmbeddings()

    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings, namespace="example-namespace")
```

If you initialize your `PineconeVectorStore` object without a namespace, you can specify the target namespace within the operation.

```Python Python theme={null}
    # path to an example text file
    loader = TextLoader("../../modules/congressional_address.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    vectorstore_from_docs = PineconeVectorStore.from_documents(
        docs,
        index_name=index_name,
        embedding=embeddings,
        namespace="example-namespace"
    )

    vectorstore_from_texts = PineconeVectorStore.from_texts(
        texts,
        index_name=index_name,
        embedding=embeddings,
        namespace="example-namespace"
    )

    vectorstore_from_docs.add_documents(docs, namespace="example-namespace")

    vectorstore_from_texts.add_texts(["More text!"], namespace="example-namespace")
```

```Python Python theme={null}
    query = "Who is Ketanji Brown Jackson?"
    vectorstore.similarity_search(query, namespace="example-namespace")
```


## Tutorial

### 1. Set up your environment

Before you begin, install some necessary libraries and set environment variables for your Pinecone and OpenAI API keys:

```Shell  theme={null}
pip install -qU \
  "pinecone[grpc]"==5.1.0 \
  pinecone-datasets==0.7.0 \
  langchain-pinecone==0.1.2 \
  langchain-openai==0.1.23 \
  langchain==0.2.15
```

```Shell  theme={null}

---
**Navigation:** [← Previous](./18-ai-engine.md) | [Index](./index.md) | [Next →](./20-set-environment-variables-for-api-keys.md)
