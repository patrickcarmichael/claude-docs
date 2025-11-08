**Navigation:** [← Previous](./11-supported-frameworks-on-vercel.md) | [Index](./index.md) | [Next →](./13-vercel-integrations.md)

---

# Add a domain

Copy page

Ask AI about this page

Last updated September 24, 2025

Assigning a custom domain to your project guarantees that visitors to your application will have a tailored experience that aligns with your brand.

On Vercel, this domain can have any format of your choosing:

*   `acme.com` ([apex domain](/docs/domains/working-with-domains#apex-domain))
*   `blog.acme.com` ([subdomain](/docs/domains/working-with-domains#subdomain))
*   `*.acme.com` ([wildcard domain](/docs/domains/working-with-domains#wildcard-domain))

If you already own a domain, you can point it to Vercel, or transfer it over. If you don't own one yet, you can purchase a new one. For this tutorial, feel free to use that one domain you bought 11 months ago and haven’t got around to using yet!

For more information on domains at Vercel, see [Domains overview](/docs/domains).

### [Next steps](#next-steps)

Now that your site is deployed, you can to personalize it by setting up a custom domain. With Vercel you can either buy a new domain or use an existing domain.

*   [Buy a new domain](/docs/getting-started-with-vercel/buy-domain)
*   [Use an existing domain](/docs/getting-started-with-vercel/use-existing)

--------------------------------------------------------------------------------
title: "Import an existing project"
description: "Create a new project on Vercel by importing your existing frontend project, built on any of our supported frameworks."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/import"
--------------------------------------------------------------------------------

# Import an existing project

Copy page

Ask AI about this page

Last updated September 24, 2025

### Using CLI?

Use the following snippet to deploy your existing project with Vercel CLI:

terminal

```
vercel --cwd [path-to-project]
```

Your existing project can be any web project that outputs static HTML content (such as a website that contains HTML, CSS, and JavaScript). When you use any of Vercel's [supported frameworks](/docs/frameworks), we'll automatically detect and set the optimal build and deployment configurations for your framework.

1.  ### [Connect to your Git provider](#connect-to-your-git-provider)
    
    On the [New Project](/new) page, under the Import Git Repository section, select the Git provider that you would like to import your project from.
    
    Follow the prompts to sign in to either your [GitHub](/docs/git/vercel-for-github), [GitLab](/docs/git/vercel-for-gitlab), or [BitBucket](/docs/git/vercel-for-bitbucket) account.
    
2.  ### [Import your repository](#import-your-repository)
    
    Find the repository in the list that you would like to import and select Import.
    
3.  ### [Optionally, configure any settings](#optionally-configure-any-settings)
    
    Vercel will automatically detect the framework and any necessary build settings. However, you can also configure the Project settings at this point including the [build and output settings](/docs/deployments/configure-a-build#build-and-development-settings) and [Environment Variables](/docs/environment-variables). These can also be set later.
    
    *   To update the [framework](/docs/deployments/configure-a-build#framework-preset), [build command](/docs/deployments/configure-a-build#build-command), [output directory](/docs/deployments/configure-a-build#output-directory), [install command](/docs/deployments/configure-a-build#install-command), or [development command](/docs/deployments/configure-a-build#development-command), expand the Build & Output Settings section and update as needed.
    *   To set environment variables, expand the Environment Variables section and either paste or copy them in.
    *   You can also configure additional properties by adding a [vercel.json](/docs/project-configuration) to your project. You can either do this now, before you deploy, or add it later and redeploy your project.
4.  ### [Deploy your project](#deploy-your-project)
    
    Press the Deploy button. Vercel will create the Project and deploy it based on the chosen configurations.
    
5.  ### [Enjoy the confetti!](#enjoy-the-confetti!)
    
    To view your deployment, select the Project in the dashboard and then select the Domain. This page is now visible to anyone who has the URL.
    
    ![Accessing auto-generated domain](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-light.png&w=3840&q=75)![Accessing auto-generated domain](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-dark.png&w=3840&q=75)
    
    Accessing auto-generated domain
    

## [Next Steps](#next-steps)

Next, learn how to assign a domain to your new deployment.

[

Add a domain

](/docs/getting-started-with-vercel/domains)

--------------------------------------------------------------------------------
title: "Next Steps"
description: "Discover the next steps to take on your Vercel journey. Unlock new possibilities and harness the full potential of your projects."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/next-steps"
--------------------------------------------------------------------------------

# Next Steps

Copy page

Ask AI about this page

Last updated September 24, 2025

Congratulations on getting started with Vercel!

Now, let's explore what's next on your journey. At this point, you can either continue learning more about Vercel's many features, or you can dive straight in and get to work. The choice is yours!

[

Dive into my dashboard

Manage your projects, domains, and more.

![Your Dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdashboard-light.png&w=3840&q=75)

![Your Dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdashboard-dark.png&w=3840&q=75)

](/dashboard)

Alternatively, you can start learning about many of the products and features that Vercel provides:

## [Infrastructure](#infrastructure)

Learn about Vercel's CDN and implement scalable infrastructure in your app using Functions. Get started today by implementing a Vercel Function in your app:

*   [Vercel functions quickstart](/docs/functions/quickstart)

## [Storage](#storage)

Vercel offers a suite of managed, serverless storage products that integrate with your frontend framework.

Learn more about [which storage option is right for you](/docs/storage#choosing-a-storage-product) and get started with implementing them:

*   [Vercel Blob](/docs/vercel-blob/server-upload)
*   [Vercel Edge Config](/docs/edge-config/get-started)

## [Observability](#observability)

Vercel provides a suite of observability tools to allow you to monitor, analyze, and manage your site.

*   [Monitoring](/docs/observability/monitoring)
*   [Web Analytics](/docs/analytics/quickstart)
*   [Speed Insights](/docs/speed-insights/quickstart)

## [Security](#security)

Vercel takes security seriously. It uses HTTPS by default for secure data transmission, regularly updates its platform to mitigate potential vulnerabilities, limits system access for increased safety, and offers built-in DDoS mitigation. This layered approach ensures robust protection for your sites and applications.

*   [Security overview](/docs/security)
*   [DDoS Mitigation](/docs/security/ddos-mitigation)

--------------------------------------------------------------------------------
title: "Projects and deployments"
description: "Streamline your workflow with Vercel's project and deployment management. Boost productivity and scale effortlessly."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/projects-deployments"
--------------------------------------------------------------------------------

# Projects and deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

To get started with Vercel, it's helpful to understand projects and deployments:

*   Projects: A [project](/docs/projects/overview) is the application that you have deployed to Vercel. You can have multiple projects connected to a single repository (for example, a [monorepo](/docs/monorepos)), and multiple [deployments](/docs/deployments) for each project. You can view all your projects on the [dashboard](/dashboard), and configure your settings through the [project dashboard](/docs/projects/project-dashboard).
*   Deployments: A [deployment](/docs/deployments) is the result of a successful [build](/docs/deployments/builds#) of your project. A deployment is triggered when you import an existing project or template, or when you push a Git commit through your [connected integration](/docs/git) or use `vercel deploy` from the [CLI](/docs/cli). Every deployment [generates a URL automatically](/docs/deployments/generated-urls).

### [More resources](#more-resources)

To get started you'll create a new project by either deploying a template or importing and deploying an existing project:

*   [Deploy a template](/docs/getting-started-with-vercel/template)
*   [Import an existing project](/docs/getting-started-with-vercel/import)

--------------------------------------------------------------------------------
title: "Use a template"
description: "Create a new project on Vercel by using a template"
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/template"
--------------------------------------------------------------------------------

# Use a template

Copy page

Ask AI about this page

Last updated September 24, 2025

### Using CLI?

Clone the template to your local machine and use the following snippet to deploy the template with Vercel CLI:

terminal

```
vercel --cwd [path-to-project]
```

Accelerate your development on Vercel with [Templates](/templates). This guide will show you how to use templates to fast-track project setup, leverage popular frontend frameworks, and maximize Vercel's features.

1.  ### [Find a template](#find-a-template)
    
    From [https://vercel.com/templates](/templates), select the template you’d like to deploy. You can use the filters to select a template based on use case, framework, and other requirements.
    
    Not sure which one to use? How about [exploring Next.js](https://vercel.com/templates/next.js/nextjs-boilerplate).
    
    ![Viewing the templates marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Ftemplates-light.png&w=3840&q=75)![Viewing the templates marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Ftemplates-dark.png&w=3840&q=75)
    
    Viewing the templates marketplace
    
2.  ### [Deploy the template to Vercel](#deploy-the-template-to-vercel)
    
    Once you've selected a template, Click Deploy on the template page to start the process.
    
    ![Deploying your chosen template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploying-template-light.png&w=1080&q=75)![Deploying your chosen template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploying-template-dark.png&w=1080&q=75)
    
    Deploying your chosen template
    
3.  ### [Connect your Git provider](#connect-your-git-provider)
    
    To ensure you can easily update your project after deploying it, Vercel will create a new repository with your chosen [Git provider](/docs/git). Every push to that Git repository will be deployed automatically.
    
    First, select the Git provider that you'd like to connect to. Once you’ve signed in, you’ll need to set the scope and repository name. At this point, Vercel will clone a copy of the source code into your Git account.
    
    ![Connecting your Git provider and creating a new repository](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fgit-provider-light.png&w=1920&q=75)![Connecting your Git provider and creating a new repository](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fgit-provider-dark.png&w=1920&q=75)
    
    Connecting your Git provider and creating a new repository
    
4.  ### [Project deployment](#project-deployment)
    
    Once the project has been cloned to your git provider, Vercel will automatically start deploying the project. This starts with [building your project](/docs/deployments/builds), then [assigning the domain](/docs/deployments/generated-urls), and finally celebrating your deployed project with confetti.
    
    ![Deploying a template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploy-template-light.png&w=1920&q=75)![Deploying a template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploy-template-dark.png&w=1920&q=75)
    
    Deploying a template
    
5.  ### [View your dashboard](#view-your-dashboard)
    
    At this point, you’ve created a production deployment, with its very own domain assigned. If you continue to your [dashboard](/dashboard), you can click on the domain to preview a live, accessible URL that is instantly available on the internet.
    
    ![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-light.png%3Flightbox&w=3840&q=75)![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-dark.png%3Flightbox&w=3840&q=75)
    
    Viewing your deployment information
    
    Zoom Image
    
    ![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-light.png%3Flightbox&w=3840&q=75)![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-dark.png%3Flightbox&w=3840&q=75)
    
    Viewing your deployment information
    
6.  ### [Clone the project to your machine](#clone-the-project-to-your-machine)
    
    Finally, you'll want to clone the source files to your local machine so that you can make some changes later. To do this from your dashboard, select the Git repository button and clone the repository.
    

Because you used a template, we’ve automatically included any additional environment set up as part of the template. You can customize your project by configuring environment variables and build options.

  

Environment Variables are key-value pairs that can be defined in your project settings for each [Environment](/docs/environment-variables#environments). Teams can also use [shared environment variables](/docs/environment-variables/shared-environment-variables) that are linked between multiple projects.

  

Vercel automatically configures builds settings based on your framework, but you can [customize the build](/docs/deployments/configure-a-build) in your project settings or within a [vercel.json](/docs/project-configuration) file.

## [Next Steps](#next-steps)

Next, learn how to assign a domain to your new deployment.

[

Add a domain

](/docs/getting-started-with-vercel/domains)

--------------------------------------------------------------------------------
title: "Use an existing domain"
description: "Seamlessly integrate your existing domain with Vercel. Maximize flexibility and maintain your established online presence."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/use-existing"
--------------------------------------------------------------------------------

# Use an existing domain

Copy page

Ask AI about this page

Last updated September 24, 2025

### Using CLI?

Use this snippet to add a domain that you own to a Vercel project:

terminal

```
vercel domains add [domain] [project]
```

Already have a domain you love? Seamlessly integrate it with Vercel to leverage the platform's powerful features and infrastructure. Whether you're migrating an existing project or want to maintain your established online presence, you can use the steps below to add your custom domain.

1.  ### [Go to your project's domains settings](#go-to-your-project's-domains-settings)
    
    Select your project and select the Settings tab. Then, select the Domains menu item or click on this [link](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdomains&title=Go+to+Domains) and select your project
    
2.  ### [Add your existing domain to your project](#add-your-existing-domain-to-your-project)
    
    From the Domains page, enter the domain you wish to add to the project.
    
    If you add an apex domain (e.g. `example.com`) to the project, Vercel will prompt you to add the `www`subdomain prefix, the apex domain, and [some basic redirection options](/docs/domains/deploying-and-redirecting).
    
    For more information on which redirect option to choose, see [Redirecting `www` domains](/docs/domains/deploying-and-redirecting#redirecting-www-domains).
    
3.  ### [Configure your DNS records](#configure-your-dns-records)
    
    Configure the DNS records of your domain with your registrar so it can be used with your Project. The dashboard will automatically display different methods for configuring it:
    
    *   If the domain is in use by another Vercel account, you will need to [verify access to the domain](/docs/domains/add-a-domain#verify-domain-access), with a TXT record
    *   If you're using an [Apex domain](/docs/domains/add-a-domain#apex-domains) (e.g. example.com), you will need to configure it with an A record
    *   If you're using a [Subdomain](/docs/domains/add-a-domain#subdomains) (e.g. docs.example.com), you will need to configure it with a CNAME record
    
    Both apex domains and subdomains can also be configured using the [Nameservers](/docs/domains/add-a-domain#vercel-nameservers) method. Wildcard domains must use the nameservers method for verification. For more information see [Add a custom domain](/docs/domains/add-a-domain).
    

## [Next steps](#next-steps)

Next, learn how to take advantage of Vercel's collaboration features as part of your developer workflow:

[

Use Vercel in your developer workflow

](/docs/getting-started-with-vercel/collaborate)

--------------------------------------------------------------------------------
title: "Deploying Git Repositories with Vercel"
description: "Vercel allows for automatic deployments on every branch push and merges onto the production branch of your GitHub, GitLab, and Bitbucket projects."
last_updated: "null"
source: "https://vercel.com/docs/git"
--------------------------------------------------------------------------------

# Deploying Git Repositories with Vercel

Copy page

Ask AI about this page

Last updated October 2, 2025

Vercel allows for automatic deployments on every branch push and merges onto the [production branch](#production-branch) of your [GitHub](/docs/git/vercel-for-github), [GitLab](/docs/git/vercel-for-gitlab), [Bitbucket](/docs/git/vercel-for-bitbucket) and [Azure DevOps Pipelines](/docs/git/vercel-for-azure-pipelines) projects.

Using Git with Vercel provides the following benefits:

*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production#) for every push.
*   [Production deployments](/docs/deployments/environments#production-environment) for the most recent changes from the [production branch](#production-branch).
*   Instant rollbacks when reverting changes assigned to a custom domain.

When working with Git, have a branch that works as your production branch, often called `main`. After you create a pull request (PR) to that branch, Vercel creates a unique deployment you can use to preview any changes. Once you are happy with the changes, you can merge your PR into the `main` branch, and Vercel will create a production deployment.

You can choose to use a different branch as the [production branch](#production-branch).

## [Supported Git Providers](#supported-git-providers)

*   [GitHub Free](https://github.com/pricing)
*   [GitHub Team](https://github.com/pricing)
*   [GitHub Enterprise Cloud](https://docs.github.com/en/get-started/learning-about-github/githubs-products#github-enterprise)
*   [GitHub Enterprise Server](https://vercel.com/guides/how-can-i-use-github-actions-with-vercel)
*   [GitLab Free](https://about.gitlab.com/pricing/)
*   [GitLab Premium](https://about.gitlab.com/pricing/)
*   [GitLab Ultimate](https://about.gitlab.com/pricing/)
*   [GitLab Enterprise](https://about.gitlab.com/enterprise/)
*   [Self-Managed GitLab](https://vercel.com/guides/how-can-i-use-gitlab-pipelines-with-vercel)
*   [Bitbucket Free](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Standard](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Premium](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Data Center (Self-Hosted)](https://vercel.com/guides/how-can-i-use-bitbucket-pipelines-with-vercel)
*   [Azure DevOps Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines)

If your provider is not listed here, you can also use the [Vercel CLI to deploy](https://vercel.com/guides/using-vercel-cli-for-custom-workflows) with any git provider.

## [Deploying a Git repository](#deploying-a-git-repository)

Setting up your GitHub, GitLab, or Bitbucket repository on Vercel is only a matter of clicking the ["New Project"](/new) button on the top right of your dashboard and following the steps.

For Azure DevOps repositories, use the [Vercel Deployment Extension](/docs/git/vercel-for-azure-pipelines)

After clicking it, you'll be presented with a list of Git repositories that the Git account you've signed up with has write access to.

To select a different Git namespace or provider, you can use the dropdown list on the top left of the section.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Findex%2Frepo-list-light.png&w=1200&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Findex%2Frepo-list-dark.png&w=1200&q=75)

A list of Git repositories your Git account has access to.

You can also:

*   Select a third-party Git repository by clicking on [Import Third-Party Git Repository](/new/git/third-party) on the bottom of the section.
*   Select a pre-built solution from the section on the right.

After you've selected the Git repository or template you want to use for your new project, you'll be taken to a page where you can configure your project before it's deployed.

You can:

*   Customize the project's name
*   Select [a Framework Preset](/docs/deployments/configure-a-build#framework-preset)
*   Select the root directory of your project
*   Configure [Build Output Settings](/docs/deployments/configure-a-build#build-command)
*   Set [Environment Variables](/docs/environment-variables)

When your settings are correct, you can select the Deploy button to initiate a deployment.

### [Creating a deployment from a Git reference](#creating-a-deployment-from-a-git-reference)

You can initiate new deployments directly from the Vercel Dashboard using a Git reference. This approach is ideal when automatic deployments are interrupted or unavailable.

To create a deployment from a Git reference:

1.  From your [dashboard](/dashboard), select the project you'd like to create a deployment for
    
2.  Select the Deployments tab. Once on the Deployments page, select the Create Deployment button
    
3.  Depending on how you would like to deploy, enter the following:
    
    *   Targeted Deployments: Provide the unique ID (SHA) of a commit to build a deployment based on that specific commit
    *   Branch-Based Deployments: Provide the full name of a branch when you want to build the most recent changes from that specific branch (for example, `https://github.com/vercel/examples/tree/deploy`)
4.  Select Create Deployment. Vercel will build and deploy your commit or branch as usual
    

When the same commit appears in multiple branches, Vercel will prompt you to choose the appropriate branch configuration. This choice is crucial as it affects settings like environment variables linked to each branch.

## [Deploying private Git repositories](#deploying-private-git-repositories)

As an additional security measure, commits on private Git repositories (and commits of forks that are targeting those Git repositories) will only be deployed if the commit author also has access to the respective project on Vercel.

Depending on whether the owner of the connected Vercel project is a Hobby or a Pro team, the behavior changes as mentioned in the sections below.

This only applies to commit authors on GitHub organizations, GitLab groups and non-personal Bitbucket workspaces. It does not apply to collaborators on personal Git accounts.

For public Git repositories, [a different behavior](/docs/git#deploying-forks-of-public-git-repositories) applies.

### [Using Pro teams](#using-pro-teams)

To deploy commits under a Vercel Pro team, the commit author must be a member of the team containing the Vercel project connected to the Git repository.

Membership is verified by finding the Vercel user associated with the commit author through [Login Connections](/docs/accounts#login-methods-and-connections). If a Vercel user is found, it checks if the account is a member of the Pro team.

If the commit author is not a member, the deployment will be prevented, and the commit author can request to join the team. The team owners will be notified and can accept or decline the membership request on the [Members](/docs/accounts/team-members-and-roles) page in the team Settings.

If the request is declined, the commit will remain undeployed. If the commit author is accepted as a member of the Pro team, their most recent commit will automatically resume deployment to Vercel.

Commit authors are automatically considered part of the Pro team on Vercel if one of the existing members has connected their account on Vercel with the Git account that created the commit.

### [Using Hobby teams](#using-hobby-teams)

You cannot deploy to a Hobby team from a private repository in a GitHub organization, GitLab group, or Bitbucket workspace. Consider making the repository public or upgrading to [Pro](/docs/plans/pro).

To deploy commits under a Hobby team, the commit author must be the owner of the Hobby team containing the Vercel project connected to the Git repository. This is verified by comparing the [Login Connections](/docs/accounts#login-methods-and-connections) Hobby team's owner with the commit author.

If the commit author is not the owner of the destination Hobby team, the deployment will be prevented, and a recommendation to transfer the project to a Pro team will be displayed on the Git provider.

After transferring the project to a Pro team, commit authors can be added as members of that team. The behavior mentioned in the [section above](/docs/git#using-pro-teams) will then apply to them whenever they commit.

## [Deploying forks of public Git repositories](#deploying-forks-of-public-git-repositories)

When a public repository is forked, commits from it will usually deploy automatically. However, when you receive a pull request from a fork of your repository, Vercel will require authorization from you or a [team member](/docs/accounts/team-members-and-roles) to deploy the pull request. This is a security measure that protects you from leaking sensitive project information. A link to authorize the deployment will be posted as a comment on the pull request.

The authorization step will be skipped if the commit author is already a [team member](/docs/accounts/team-members-and-roles) on Vercel.

## [Production branch](#production-branch)

A [Production deployment](/docs/deployments/environments#production-environment) will be created each time you merge to the production branch.

### [Default configuration](#default-configuration)

When you create a new Project from a Git repository on Vercel, the Production Branch will be selected in the following order:

*   The `main` branch.
*   If not present, the `master` branch ([more details](https://vercel.com/blog/custom-production-branch#a-note-on-the-master-branch)).
*   \[Only for Bitbucket\]: If not present, the "production branch" setting of your Git repository is used.
*   If not present, the Git repository's default branch.

### [Customizing the production branch](#customizing-the-production-branch)

On the Environments page in the Project Settings, you can change your production branch:

*   Click on the Production environment and go to Branch Tracking
*   Change the name of the branch and click Save

Whenever a new commit is then pushed to the branch you configured here, a [production deployment](/docs/deployments/environments#production-environment) will be created for you.

## [Preview branches](#preview-branches)

While the [production branch](/docs/git#production-branch) is a single Git branch that contains the code that is served to your visitors, all other branches are deployed as pre-production branches (either preview branches, or if you have configured them, custom environments branches).

For example, if your production branch is `main`, then [by default](/docs/git#using-custom-environments) all the Git branches that are not `main` are considered preview branches. That means there can be many preview branches, but only a single production branch.

To learn more about previews, see the [Preview Deployments](/docs/deployments/environments#preview-environment-pre-production) page.

By default, every preview branch automatically receives its own domain similar to the one shown below, whenever a commit is pushed to it. To learn more about generated URLs, see the [Accessing Deployments through Generated URLs](/docs/deployments/generated-urls#generated-from-git) page.

### [Multiple preview phases](#multiple-preview-phases)

For most use cases, the default preview behavior mentioned above is enough. If you'd like your changes to pass through multiple phases of preview branches instead of just one, you can accomplish it by [assigning Domains](/docs/domains/working-with-domains/assign-domain-to-a-git-branch) and [Environment Variables](/docs/environment-variables#preview-environment-variables) to specific Preview Branches.

For example, you could create a phase called "Staging" where you can accumulate Preview changes before merging them onto production by following these steps:

1.  Create a Git branch called "staging" in your Git repository.
2.  Add a domain of your choice (like `staging.example.com`) on your Vercel project and assign it to the "staging" Git branch [like this](/docs/domains/working-with-domains/assign-domain-to-a-git-branch).
3.  Add Environment Variables that you'd like to use for your new Staging phase on your Vercel project [like this](/docs/environment-variables#preview-environment-variables).
4.  Push to the "staging" Git branch to update your Staging phase and automatically receive the domain and environment variables you've defined.
5.  Once you're happy with your changes, you would then merge the respective Preview Branch into your production branch. However, unlike with the default Preview behavior, you'd then keep the branch around instead of deleting it, so that you can push to it again in the future.

Alternatively, teams on the Pro plan can use [custom environments](/docs/deployments/environments#custom-environments).

### [Using custom environments](#using-custom-environments)

[Custom environments](/docs/deployments/environments#custom-environments) allow you to create and define a pre-production environment. As part of creating a custom environment, you can match specific branches or branch names, including `main`, to automatically deploy to that environment. You can also attach a domain to the environment.

--------------------------------------------------------------------------------
title: "Deploying Azure DevOps Pipelines with Vercel"
description: "​Vercel for Azure DevOps allows you to deploy Azure Pipelines to Vercel automatically."
last_updated: "null"
source: "https://vercel.com/docs/git/vercel-for-azure-pipelines"
--------------------------------------------------------------------------------

# Deploying Azure DevOps Pipelines with Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

The [Vercel Deployment Extension](https://marketplace.visualstudio.com/items?itemName=Vercel.vercel-deployment-extension) allows you to automatically deploy to Vercel from [Azure DevOps](https://azure.microsoft.com/en-us/products/devops) [Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops). You can add the extension to your Azure DevOps Projects through the [Visual Studio marketplace](https://marketplace.visualstudio.com/).

Once the Vercel extension is set up, your Azure DevOps project is connected to your [Vercel Project](/docs/projects/overview). You can then use your Azure Pipeline(s) inside your Azure DevOps project to trigger a [Vercel Deployment](/docs/deployments).

This page will help you use the extension in your own use case. You can:

*   Follow the [quickstart](#quickstart) to set up the extension and trigger a production deployment based on commits to the `main` branch
*   Use the [full-featured pipeline](#full-featured-azure-pipeline-creation) for a similar setup as [Vercel's other git integrations](/docs/git). This includes preview deployment creation on pull requests and production deployments on merging to the `main` branch
*   Review the [extension task reference](#extension-task-reference) to customize the pipeline for your specific use case

## [Quickstart](#quickstart)

At the end of this quickstart, your Azure DevOps Pipeline will trigger a Vercel production deployment whenever you commit a change to the `main` branch of your code. To get this done, we will follow these steps:

1.  Create a Vercel Personal Access Token
2.  Create secret variables
3.  Set up the Vercel Deployment Extension from the Visual Studio marketplace
4.  Set up a basic Azure Pipeline to trigger production deployments on Vercel
5.  Test your workflow

Once you have the Vercel Deployment extension set up, you only need to modify your Azure DevOps Pipeline (Steps 4 and 5) to change the deployment workflow to fit your use case.

### [Prerequisites](#prerequisites)

An **empty** Vercel Project with no Git integration

An [Azure DevOps project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project) that contains the code that you would like to deploy on Vercel

To create an empty Vercel project:

1.  Use the [Vercel CLI](/docs/cli/project) with the `add` command

terminal

```
vercel project add
```

1.  Or through the [dashboard](/docs/projects/overview#creating-a-project) and then disconnect the [Git integration](/docs/projects/overview#git) that you would have set up

### [Extension and Pipeline set up](#extension-and-pipeline-set-up)

1.  ### [Create a Vercel Personal Access Token](#create-a-vercel-personal-access-token)
    
    *   Follow [Creating an Access Token](/docs/rest-api#creating-an-access-token) to create an access token with the scope of access set to the team where your Vercel Project is located
    *   Copy this token to a secure location
2.  ### [Create secret variables](#create-secret-variables)
    
    For security purposes, you should use the above created token in your Azure Pipeline through [secret variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).
    
    *   For this quickstart, we will create the secret variables when we create the pipeline. Once created, these variables will always be accessible to that pipeline
    *   Otherwise, you can create them before you create the pipeline in a [variable group](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops&tabs=yaml%2Cbash#set-a-secret-variable-in-a-variable-group) or a [key vault](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops&tabs=yaml%2Cbash#link-secrets-from-an-azure-key-vault) as long as you make sure that your Azure Project has the right access
3.  ### [Set up the Vercel Deployment Extension](#set-up-the-vercel-deployment-extension)
    
    *   Go to the [Vercel Deployment Extension Visual Studio marketplace page](https://marketplace.visualstudio.com/items?itemName=Vercel.vercel-deployment-extension)
    *   Click Get it free and select the Azure DevOps organization where your Azure Project is located
4.  ### [Set up a basic Azure Pipeline](#set-up-a-basic-azure-pipeline)
    
    This step assumes that your code exists as a repository in your Azure Project's Repos and that your Vercel Project is named `azure-devops-extension`.
    
    ![Azure DevOps Pipeline creation at the review stage to create variables and save/edit your pipeline](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2FAzure-pipeline-light.png&w=3840&q=75)![Azure DevOps Pipeline creation at the review stage to create variables and save/edit your pipeline](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2FAzure-pipeline-dark.png&w=3840&q=75)
    
    Azure DevOps Pipeline creation at the review stage to create variables and save/edit your pipeline
    
    *   From your Azure DevOps Project, select Pipelines from the left side bar
    *   Select the New Pipeline button
    *   Select where your code is located (In this example, we uploaded the code as an Azure Repos Git. Select Azure Repos Git and then select your uploaded repository)
    *   Select Node.js for the pipeline configuration
    *   In the Review your pipeline YAML step, select Variables on the top right
        *   Select New Variable, use `VERCEL_TOKEN` as the name and the value of the Vercel Personal Access Token you created earlier. Check the secret option. Select Ok
    *   Close the Variables window and paste the following code to replace the code in `azure-pipelines.yml` that you can rename to `vercel-pipeline.yml`
    
    vercel-pipeline.yml
    
    ```
    trigger:
    - main
     
    pool:
      vmImage: ubuntu-latest
     
    steps:
    - task: vercel-deployment-task@1
      inputs:
        vercelProjectId: 'prj_mtYj0MP83muZkYDs2DIDfasdas' //Example Vercel Project ID
        vercelOrgId: '3Gcd2ASTsPxwxTsYBwJTB11p' //Example Vercel Personal Account ID
        vercelToken: $(VERCEL_TOKEN)
        production: true
    ```
    
    #### [Value of `vercelProjectId`](#value-of-vercelprojectid)
    
    Look for Project ID located on the Vercel Project's Settings page at Project Settings > General.
    
    #### [Value of `vercelOrgId`](#value-of-vercelorgid)
    
    *   If your Project is located under your Hobby team, look for Your ID under your Vercel Personal Account [Settings](https://vercel.com/account)
    *   If your Project is located under a Team, look for Team ID under Team Settings > General
    *   Select Save and Run
    *   This should trigger a production deployment in your Vercel Project as no code was committed before
5.  ### [Test your workflow](#test-your-workflow)
    
    *   Make a change in your code inside Azure Repos from the `main` branch and commit the change
    *   This should trigger another deployment in your Vercel Project

Your Azure DevOps project is now connected to your Vercel project with automatic production deployments on the `main` branch. You can update or create pipelines in the Azure DevOps project to customize the Vercel deployment behavior by using the [options](#extension-task-reference) of the Vercel Deployment Extension.

## [Full-featured Azure Pipeline creation](#full-featured-azure-pipeline-creation)

In a production environment, you will often want the following to happen:

*   Trigger preview deployments for pull requests to the `main` branch
*   Trigger production deployments only for commits to the `main` branch

Before you update your pipeline file to enable preview deployments, you need to configure Azure DevOps with pull requests.

### [Triggers and comments on pull requests](#triggers-and-comments-on-pull-requests)

In order to allow pull requests in your Azure repository to create a deployment and report back with a comment, you need the following:

*   An Azure DevOps Personal Access Token
*   A build validation policy for your branch

### [Create an Azure DevOps Personal Access Token](#create-an-azure-devops-personal-access-token)

1.  Go to your [Azure DevOps account](https://dev.azure.com) and select the user settings icon on the top right
2.  Select Personal access tokens from the menu option
3.  Select the New Token button
4.  After completing the basic token information such as Name, Organization, and Expiration, select the Custom defined option under Scopes
5.  At the bottom of the form, select Show all scopes
6.  Browse down the scopes list until Pull Request Threads. Select the Read & Write checkbox
7.  Select Create at the bottom of the form
8.  Make sure you copy the token to a secure location before you close the prompt

### [Create a build validation policy](#create-a-build-validation-policy)

![Azure Build Validation under Branch Policies of Project settings](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2FAzure-build-policy-light.png&w=3840&q=75)![Azure Build Validation under Branch Policies of Project settings](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2FAzure-build-policy-dark.png&w=3840&q=75)

Azure Build Validation under Branch Policies of Project settings

1.  Go to your Azure DevOps Project's page
2.  Select Project settings in the lower left corner
3.  From the Project settings left side bar, select Repositories under Repos
4.  Select the repository where your vercel pipeline is set up
5.  Select the Policies tab on the right side
6.  Scroll down to Branch Policies, and select the `main` branch
7.  Scroll down to Build Validation and select on the + button to create a new validation policy
8.  Select the pipeline you created earlier and keep the policy marked as Required so that commits directly to main are prevented
9.  Select Save

Create a pull request to the `main` branch. This will trigger the pipeline, run the deployment and comment back on the pull request with the deployment URL.

### [Update your pipeline](#update-your-pipeline)

*   From your Azure DevOps Project, select Pipelines from the left side bar
*   Select the pipeline that you want to edit by selecting the icon
*   Select the Variables button and add a new secret variable called `AZURE_TOKEN` with the value of the Azure DevOps Personal Access Token you created earlier. Select Ok
*   Close the Variables window and paste the following code to replace the code in `vercel-pipelines.yml`

vercel-pipeline.yml

```
trigger:
- main
 
pool:
  vmImage: ubuntu-latest
 
variables:
  isMain: $[eq(variables['Build.SourceBranch'], 'refs/heads/main')]
 
steps:
- task: vercel-deployment-task@1
  name: 'Deploy'
  inputs:
    condition: or(eq(variables.isMain, true), eq(variables['Build.Reason'], 'PullRequest'))
    vercelProjectId: 'azure-devops-extension'
    vercelOrgId: '3Gcd2ASTsPxwxTsYBwJTB11p' //Example Vercel Personal Account ID
    vercelToken: $(VERCEL_TOKEN)
    production: $(isMain)
- task: vercel-azdo-pr-comment-task@1
  inputs:
    azureToken: $(AZURE_TOKEN)
    deploymentTaskMessage: $(Deploy.deploymentTaskMessage)
```

*   Select Save

The `vercel-deployment-task` creates an [output variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables) called `deploymentTaskMessage`. By setting the `name:` of the step to `'Deploy'`, you can access it using `$(Deploy.deploymentTaskMessage)` which you can then assign to the input option `deploymentTaskMessage` of the `vercel-azdo-pr-comment-task` task step.

### [Create a pull request and test](#create-a-pull-request-and-test)

*   Create a new branch in your Azure DevOps repository and push a commit
*   Open a pull request against the `main` branch
*   This will trigger a pipeline execution and create a preview deployment on Vercel
*   Once the deployment has completed, you will see a comment on the pull request in Azure DevOps with the preview URL

## [Extension task reference](#extension-task-reference)

Here, you can find a list of available properties for each of the available tasks in the Vercel Deployment Extension.

### [`vercel-deployment-task`](#vercel-deployment-task)

#### [Input properties](#input-properties)

| Property | Required | Type | Description |
| --- | --- | --- | --- |
| `vercelProjectId` | No | string | The [ID of your Vercel Project](#value-of-vercelprojectid). It can alternatively be set as the environment variable VERCEL\_PROJECT\_ID |
| `vercelOrgId` | No | string | The [ID of your Vercel Org](#value-of-vercelorgid). It can alternatively be set as the environment variable VERCEL\_ORG\_ID |
| `vercelToken` | No | string | A [Vercel personal access](/docs/rest-api#creating-an-access-token) token with deploy permissions for your Vercel Project. It can alternatively be set as the environment variable VERCEL\_TOKEN |
| `vercelCWD` | No | string | The working directory where the Vercel deployment task will run. When omitted, the task will run in the current directory (default value is `System.DefaultWorkingDirectory`). It can alternatively be set as the environment variable VERCEL\_CWD |
| `production` | No | boolean | Boolean value specifying if the task should create a production deployment. When omitted or set to `false`, the task will create preview deployments |
| `debug` | No | boolean | Boolean value that enables the `--debug` option for the internal Vercel CLI operations |

#### [Output variables](#output-variables)

| Variable | Type | Description |
| --- | --- | --- |
| `deploymentTaskMessage` | string | The message output taken from the deployment. It can be used in tasks that follow |

### [`vercel-azdo-pr-comment-task`](#vercel-azdo-pr-comment-task)

#### [Input properties](#input-properties)

| Property | Required | Type | Description |
| --- | --- | --- | --- |
| `azureToken` | Yes | string | An [Azure personal access token](#create-an-azure-devops-personal-access-token) with the Git `PullRequestContribute` permission for your Azure DevOps Organization |
| `deploymentTaskMessage` | Yes | string | The message that will added as a comment on the pull request. It is normally created by the Vercel Deployment Task |

--------------------------------------------------------------------------------
title: "Deploying Bitbucket Projects with Vercel"
description: "​Vercel for Bitbucket automatically deploys your Bitbucket projects with Vercel, providing Preview Deployment URLs, and automatic Custom Domain updates."
last_updated: "null"
source: "https://vercel.com/docs/git/vercel-for-bitbucket"
--------------------------------------------------------------------------------

# Deploying Bitbucket Projects with Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel for Bitbucket automatically deploys your Bitbucket projects with [Vercel](/), providing [Preview Deployment URLs](/docs/deployments/environments#preview-environment-pre-production#preview-urls), and automatic [Custom Domain](/docs/domains/add-a-domain) updates.

## [Supported Bitbucket Products](#supported-bitbucket-products)

*   [Bitbucket Free](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Standard](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Premium](https://www.atlassian.com/software/bitbucket/pricing)
*   [Bitbucket Data Center (Self-Hosted)](#using-bitbucket-pipelines)

## [Deploying a Bitbucket Repository](#deploying-a-bitbucket-repository)

The [Deploying a Git repository](/docs/git#deploying-a-git-repository) guide outlines how to create a new Vercel Project from a Bitbucket repository, and enable automatic deployments on every branch push.

## [Changing the Bitbucket Repository of a Project](#changing-the-bitbucket-repository-of-a-project)

If you'd like to connect your Vercel Project to a different Bitbucket repository or disconnect it, you can do so from the [Git section](/docs/projects/overview#git) in the Project Settings.

### [A Deployment for Each Push](#a-deployment-for-each-push)

Vercel for Bitbucket will deploy each push by default. This includes pushes and pull requests made to branches. This allows those working within the project to preview the changes made before they are pushed to production.

With each new push, if Vercel is already building a previous commit on the same branch, the current build will complete and any commit pushed during this time will be queued. Once the first build completes, the most recent commit will begin deployment and the other queued builds will be cancelled. This ensures that you always have the latest changes deployed as quickly as possible.

### [Updating the Production Domain](#updating-the-production-domain)

If [Custom Domains](/docs/projects/custom-domains) are set from a project domains dashboard, pushes and merges to the [Production Branch](/docs/git#production-branch) (commonly "main") will be made live to those domains with the latest deployment made with a push.

If you decide to revert a commit that has already been deployed to production, the previous [Production Deployment](/docs/deployments/environments#production-environment) from a commit will automatically be made available at the [Custom Domain](/docs/projects/custom-domains) instantly; providing you with instant rollbacks.

### [Preview URLs for Each Pull Request](#preview-urls-for-each-pull-request)

The latest push to any [pull request](https://www.atlassian.com/git/tutorials/making-a-pull-request) will automatically be made available at a unique preview URL based on the project name, branch, and team or username. These URLs will be given through a comment on each pull request.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fbitbucket-comment.png&w=1920&q=75)

A preview URL created from a pull request.

### [System environment variables](#system-environment-variables)

You may want to use different workflows and APIs based on Git information. To support this, the following [System Environment Variables](/docs/environment-variables/system-environment-variables) are exposed to your Deployments:

  

### [VERCEL\_GIT\_PROVIDER](#VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from. In the case of Bitbucket, the value is always `bitbucket`.

### [VERCEL\_GIT\_REPO\_SLUG](#VERCEL_GIT_REPO_SLUG)

The slug of the Bitbucket repository that was deployed.

.env

```
VERCEL_GIT_REPO_SLUG=my-site
```

### [VERCEL\_GIT\_REPO\_OWNER](#VERCEL_GIT_REPO_OWNER)

The Bitbucket user or team that the project belongs to.

.env

```
VERCEL_GIT_REPO_OWNER=acme
```

### [VERCEL\_GIT\_REPO\_ID](#VERCEL_GIT_REPO_ID)

The ID of the Bitbucket repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_ID=9e072df2-521e-4409-a01c-c984569fea20
```

### [VERCEL\_GIT\_COMMIT\_REF](#VERCEL_GIT_COMMIT_REF)

The Bitbucket branch that the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VERCEL\_GIT\_COMMIT\_SHA](#VERCEL_GIT_COMMIT_SHA)

The Bitbucket sha of the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VERCEL\_GIT\_COMMIT\_MESSAGE](#VERCEL_GIT_COMMIT_MESSAGE)

The message accompanying the Bitbucket commit that was deployed.

.env

```
VERCEL_GIT_COMMIT_MESSAGE=Add John Doe to about page
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The name of the commit author on Bitbucket.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_LOGIN=John Doe
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VERCEL_GIT_COMMIT_AUTHOR_NAME)

Bitbucket profile URL of the commit author.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_NAME=https://bitbucket.org/%7B45585b19-b616-401e-89d3-1a47fddb7033%7D/
```

### [VERCEL\_GIT\_PULL\_REQUEST\_ID](#VERCEL_GIT_PULL_REQUEST_ID)

The Bitbucket pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VERCEL_GIT_PULL_REQUEST_ID=23
```

We require some permissions through our Vercel for Bitbucket integration. Below are listed the permissions required and a description for what they are used for.

### [Repository Permissions](#repository-permissions)

Repository permissions allow us to interact with repositories belonging to or associated with (if permitted) the connected account.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Web Hooks` | Y | N | Allows us to react to various Bitbucket events. |
| `Issues` | Y | Y | Allows us to interact with Pull Requests as with the `Pull Requests` permissions due to Bitbucket requiring both for access. |
| `Repository` | N | N | Allows us to access admin features of a Bitbucket repository. |
| `Pull requests` | Y | Y | Allows us create deployments for each Pull Request (PR) and comment on those PR's with status updates. |

#### [Organization Permissions](#organization-permissions)

Organization permissions allow us to offer an enhanced experience through information about the connected organization.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Team` | Y | N | Allows us to offer a better team onboarding experience. |

#### [User Permissions](#user-permissions)

User permissions allow us to offer an enhanced experience through information about the connected user.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Account` | Y | N | Allows us to associate an email with a Bitbucket account. |

We use the permissions above in order to provide you with the best possible deployment experience. If you have any questions or concerns about any of the permission scopes, please [contact Vercel Support](/help#issues).

To sign up on Vercel with a different Bitbucket account, sign out of your current Bitbucket account. Then, restart the Vercel [signup process](/signup).

## [Missing Git repository](#missing-git-repository)

When importing or connecting a Bitbucket repository, we require that you have **Admin** access to the corresponding repository, so that we can configure a webhook and automatically deploy pushed commits.

If a repository is missing when you try to import or connect it, make sure that you have [Admin access configured for the repository](https://support.atlassian.com/bitbucket-cloud/docs/grant-repository-access-to-users-and-groups/).

## [Silence comments](#silence-comments)

By default, comments from the Vercel bot will appear on your pull requests and commits. You can silence these comments in your project's settings:

1.  From the Vercel [dashboard](/dashboard), select your project
2.  From the Settings tab, select Git
3.  Under Connected Git Repository, toggle the switches to your preference

It is currently not possible to prevent comments for specific branches.

## [Using Bitbucket Pipelines](#using-bitbucket-pipelines)

You can use Bitbucket Pipelines to build and deploy your Vercel Application.

`vercel build` allows you to build your project inside Bitbucket Pipelines, without exposing your source code to Vercel. Then, `vercel deploy --prebuilt` skips the build step on Vercel and uploads the previously generated `.vercel/output` folder to Vercel from the Bitbucket Pipeline.

[Learn more about how to configure Bitbucket Pipelines and Vercel](https://vercel.com/guides/how-can-i-use-bitbucket-pipelines-with-vercel) for custom CI/CD workflows.

--------------------------------------------------------------------------------
title: "Deploying GitHub Projects with Vercel"
description: "Vercel for GitHub automatically deploys your GitHub projects with Vercel, providing Preview Deployment URLs, and automatic Custom Domain updates."
last_updated: "null"
source: "https://vercel.com/docs/git/vercel-for-github"
--------------------------------------------------------------------------------

# Deploying GitHub Projects with Vercel

Copy page

Ask AI about this page

Last updated October 8, 2025

Vercel for GitHub automatically deploys your GitHub projects with [Vercel](/), providing [Preview Deployment URLs](/docs/deployments/environments#preview-environment-pre-production#preview-urls), and automatic [Custom Domain](/docs/domains/working-with-domains) updates.

## [Supported GitHub Products](#supported-github-products)

*   [GitHub Free](https://github.com/pricing)
*   [GitHub Team](https://github.com/pricing)
*   [GitHub Enterprise Cloud](https://docs.github.com/en/get-started/learning-about-github/githubs-products#github-enterprise)
*   [GitHub Enterprise Server](#using-github-actions) (When used with GitHub Actions)

## [Deploying a GitHub Repository](#deploying-a-github-repository)

The [Deploying a Git repository](/docs/git#deploying-a-git-repository) guide outlines how to create a new Vercel Project from a GitHub repository, and enable automatic deployments on every branch push.

## [Changing the GitHub Repository of a Project](#changing-the-github-repository-of-a-project)

If you'd like to connect your Vercel Project to a different GitHub repository or disconnect it, you can do so from the [Git section](/docs/projects/overview#git) in the Project Settings.

### [A Deployment for Each Push](#a-deployment-for-each-push)

Vercel for GitHub will deploy every push by default. This includes pushes and pull requests made to branches. This allows those working within the repository to preview changes made before they are pushed to production.

With each new push, if Vercel is already building a previous commit on the same branch, the current build will complete and any commit pushed during this time will be queued. Once the first build completes, the most recent commit will begin deployment and the other queued builds will be cancelled. This ensures that you always have the latest changes deployed as quickly as possible.

You can disable this feature for GitHub by configuring the [github.autoJobCancellation](/docs/project-configuration/git-configuration#github.autojobcancelation) option in your `vercel.json` file.

### [Updating the Production Domain](#updating-the-production-domain)

If [Custom Domains](/docs/projects/custom-domains) are set from a project domains dashboard, pushes and merges to the [Production Branch](/docs/git#production-branch) (commonly "main") will be made live to those domains with the latest deployment made with a push.

If you decide to revert a commit that has already been deployed to production, the previous [Production Deployment](/docs/deployments/environments#production-environment) from a commit will automatically be made available at the [Custom Domain](/docs/projects/custom-domains) instantly; providing you with instant rollbacks.

### [Preview URLs for the Latest Changes for Each Pull Request](#preview-urls-for-the-latest-changes-for-each-pull-request)

The latest push to any pull request will automatically be made available at a unique [preview URL](/docs/deployments/environments#preview-environment-pre-production#preview-urls) based on the project name, branch, and team or username. These URLs will be provided through a comment on each pull request. Vercel also supports Comments on preview deployments made from PRs on GitHub. [Learn more about Comments on preview deployments in GitHub here](/docs/deployments/environments#preview-environment-pre-production#github-integration).

### [Deployment Authorizations for Forks](#deployment-authorizations-for-forks)

If you receive a pull request from a fork of your repository, Vercel will require authorization from you or a [team member](/docs/rbac/managing-team-members) to deploy the pull request.

This behavior protects you from leaking sensitive project information such as environment variables and the [OIDC Token](/docs/oidc).

You can disable [Git Fork Protection](/docs/projects/overview#git-fork-protection) in the Security section of your Project Settings.

Vercel for GitHub uses the deployment API to bring you an extended user interface both in GitHub, when showing deployments, and Slack, if you have notifications setup using the [Slack GitHub app](https://slack.github.com).

You will see all of your deployments, production or preview, from within GitHub on its own page.

Due to using GitHub's Deployments API, you will also be able to integrate with other services through [GitHub's checks](https://help.github.com/en/articles/about-status-checks). Vercel will provide the deployment URL to the checks that require it, for example; to a testing suite such as [Checkly](https://checklyhq.com/docs/cicd/github/).

### [Configuring for GitHub](#configuring-for-github)

To configure the Vercel for GitHub integration, see [the configuration reference for Git](/docs/project-configuration/git-configuration).

### [System environment variables](#system-environment-variables)

You may want to use different workflows and APIs based on Git information. To support this, the following [System Environment Variables](/docs/environment-variables/system-environment-variables) are exposed to your Deployments:

  

### [VERCEL\_GIT\_PROVIDER](#VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from. In the case of GitHub, the value is always `github`.

### [VERCEL\_GIT\_REPO\_SLUG](#VERCEL_GIT_REPO_SLUG)

The origin repository of the app on GitHub.

.env

```
VERCEL_GIT_REPO_SLUG=my-site
```

### [VERCEL\_GIT\_REPO\_OWNER](#VERCEL_GIT_REPO_OWNER)

The GitHub organization that owns the repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_OWNER=acme
```

### [VERCEL\_GIT\_REPO\_ID](#VERCEL_GIT_REPO_ID)

The ID of the GitHub repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_ID=117716146
```

### [VERCEL\_GIT\_COMMIT\_REF](#VERCEL_GIT_COMMIT_REF)

The GitHub branch that the deployment was made from.

.env

```
VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VERCEL\_GIT\_COMMIT\_SHA](#VERCEL_GIT_COMMIT_SHA)

The GitHub [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VERCEL\_GIT\_COMMIT\_MESSAGE](#VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the GitHub commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The GitHub username belonging to the author of the commit that the project was deployed by.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VERCEL_GIT_COMMIT_AUTHOR_NAME)

The GitHub name belonging to the author of the commit that the project was deployed by.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VERCEL\_GIT\_PULL\_REQUEST\_ID](#VERCEL_GIT_PULL_REQUEST_ID)

The GitHub pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VERCEL_GIT_PULL_REQUEST_ID=23
```

We require some permissions through our Vercel for GitHub integration. Below are listed the permissions required and a description for what they are used for.

### [Repository Permissions](#repository-permissions)

Repository permissions allow us to interact with repositories belonging to or associated with (if permitted) the connected account.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Administration` | Y | Y | Allows us to create repositories on the user's behalf. |
| `Checks` | Y | Y | Allows us to add checks against source code on push. |
| `Contents` | Y | Y | Allows us to fetch and write source code for new project templates for the connected user or organization. |
| `Deployments` | Y | Y | Allows us to synchronize deployment status between GitHub and the Vercel infrastructure. |
| `Pull Requests` | Y | Y | Allows us create deployments for each Pull Request (PR) and comment on those PR's with status updates. |
| `Issues` | Y | Y | Allows us to interact with Pull Requests as with the `Pull Requests` permissions due to GitHub requiring both for access. |
| `Metadata` | Y | N | Allows us to read basic repository metadata to provide a detailed dashboard. |
| `Web Hooks` | Y | Y | Allows us to react to various GitHub events. |
| `Commit Statuses` | Y | Y | Allows us to synchronize commit status between GitHub and Vercel. |

### [Organization Permissions](#organization-permissions)

Organization permissions allow us to offer an enhanced experience through information about the connected organization.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Members` | Y | N | Allows us to offer a better team onboarding experience. |

### [User Permissions](#user-permissions)

User permissions allow us to offer an enhanced experience through information about the connected user.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `Email addresses` | Y | N | Allows us to associate an email with a GitHub account. |

We use the permissions above in order to provide you with the best possible deployment experience. If you have any questions or concerns about any of the permission scopes, please [contact Vercel Support](/help#issues).

To sign up on Vercel with a different GitHub account, sign out of your current GitHub account.

Then, restart the Vercel [signup process](/signup).

## [Missing Git repository](#missing-git-repository)

When importing or connecting a GitHub repository, we require that you have **Collaborator** access to the corresponding repository, so that we can configure a webhook and automatically deploy pushed commits.

If a repository is missing when you try to import or connect it, make sure that you have **Collaborator** access configured for the repository. For an organization or a team, this [page](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/viewing-people-with-access-to-your-repository) explains how to view the permissions of the members. For personal GitHub accounts, this [page](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories) explains how to manage access.

## [Silence GitHub comments](#silence-github-comments)

By default, comments from the Vercel GitHub bot will appear on your pull requests and commits. You can silence these comments in your project's settings:

1.  From the Vercel [dashboard](/dashboard), select your project
2.  From the Settings tab, select Git
3.  Under Connected Git Repository, toggle the switches to your preference

If you had previously used the, now deprecated, [`github.silent`](/docs/project-configuration/git-configuration#github.silent) property in your project configuration, we'll automatically adjust the setting for you.

It is currently not possible to prevent comments for specific branches.

## [Silence deployment notifications on pull requests](#silence-deployment-notifications-on-pull-requests)

By default, Vercel notifies GitHub of deployments using [the `deployment_status` webhook event](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#deployment_status). This creates an entry in the activity log of GitHub's pull request UI.

Because Vercel also adds a comment to the pull request with a link to the deployment, unwanted noise can accumulate from the list of deployment notifications added to a pull request.

You can disable `deployment_status` events by:

*   [Going to the Git settings for your project](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fgit&title=Project+Git+settings)
*   Disabling the `deployment_status` Events toggle

Before doing this, ensure that you aren't depending on `deployment_status` events in your GitHub Actions workflows. If you are, we encourage [migrating to `repository_dispatch` events](#migrating-from-deployment_status).

## [Using GitHub Actions](#using-github-actions)

You can use GitHub Actions to build and deploy your Vercel Application. This approach is necessary to enable Vercel with GitHub Enterprise Server (GHES) with Vercel, as GHES cannot use Vercel’s built-in Git integration.

1.  Create a GitHub Action to build your project and deploy it to Vercel. Make sure to install the Vercel CLI (`npm install --global vercel@latest`) and pull your environment variables `vercel pull --yes --environment=preview --token=${{ secrets.VERCEL_TOKEN }}`
2.  Use `vercel build` to build your project inside GitHub Actions, without exposing your source code to Vercel
3.  Then use `vercel deploy --prebuilt` to skip the build step on Vercel and upload the previously generated `.vercel/output` folder from your GitHub Action to Vercel

You'll need to make GitHub Actions for preview (non-`main` pushes) and production (`main` pushes) deployments. [Learn more about how to configure GitHub Actions and Vercel](https://vercel.com/guides/how-can-i-use-github-actions-with-vercel) for custom CI/CD workflows.

### [Repository dispatch events](#repository-dispatch-events)

This event will only trigger a workflow run if the workflow file exists on the default branch (e.g. `main`). If you'd like to test the workflow prior to merging to `main`, we recommend adding a [`workflow_dispatch` trigger](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#workflow_dispatch).

Vercel sends [`repository_dispatch` events](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch) to GitHub when the status of your deployment changes. These events can trigger GitHub Actions, enabling continuous integration tasks dependent on Vercel deployments.

GitHub Actions can trigger on the following events:

```
on:
  repository_dispatch:
    - 'vercel.deployment.ready'
    - 'vercel.deployment.success'
    - 'vercel.deployment.error'
    - 'vercel.deployment.canceled'
    # canceled as a result of the ignored build script
    - 'vercel.deployment.ignored'
    # canceled as a result of automatic deployment skipping https://vercel.com/docs/monorepos#skipping-unaffected-projects
    - 'vercel.deployment.skipped'
    - 'vercel.deployment.pending'
    - 'vercel.deployment.failed'
    - 'vercel.deployment.promoted'
```

`repository_dispatch` events contain a JSON payload with information about the deployment, such as deployment `url` and deployment `environment`. GitHub Actions can access this payload through `github.event.client_payload`. For example, accessing the URL of your triggering deployment through `github.event.client_payload.url`.

Read more and see the [full schema](https://github.com/vercel/repository-dispatch/blob/main/packages/repository-dispatch/src/types.ts) in [our `repository-dispatch` package](https://github.com/vercel/repository-dispatch), and see the [how can I run end-to-end tests after my Vercel preview deployment?](https://vercel.com/guides/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment) guide for a practical example.

#### [Migrating from `deployment_status`](#migrating-from-deployment_status)

With `repository_dispatch`, the dispatch event `client_payload` contains details about your deployment allowing you to reduce GitHub Actions costs and complexity in your workflows.

For example, to migrate the GitHub Actions trigger for preview deployments for end-to-end tests:

Previously, we needed to check if the status of a deployment was successful. Now, with `repository_dispatch` we can trigger our workflow only on a successful deployment by specifying the `'vercel.deployment.success'` dispatch type.

Since we're no longer using the `deployment_status` event, we need to get the `url` from the `vercel.deployment.success` event's `client_payload`.

```
name: End to End Tests
 
on:
- deployment_status:
+ repository_dispatch:
+   types:
+    - 'vercel.deployment.success'
jobs:
  run-e2es:
-   if: github.event_name == 'deployment_status' && github.event.deployment_status.state == 'success'
+   if: github.event_name == 'repository_dispatch'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: npm ci && npx playwright install --with-deps
      - name: Run tests
        run: npx playwright test
        env:
-         BASE_URL: ${{ github.event.deployment_status.environment_url }}
+         BASE_URL: ${{ github.event.client_payload.url }}
```

--------------------------------------------------------------------------------
title: "Deploying GitLab Projects with Vercel"
description: "​Vercel for GitLab automatically deploys your GitLab projects with Vercel, providing Preview Deployment URLs, and automatic Custom Domain updates."
last_updated: "null"
source: "https://vercel.com/docs/git/vercel-for-gitlab"
--------------------------------------------------------------------------------

# Deploying GitLab Projects with Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel for GitLab automatically deploys your GitLab projects with [Vercel](/), providing [Preview Deployment URLs](/docs/deployments/environments#preview-environment-pre-production#preview-urls), and automatic [Custom Domain](/docs/domains/working-with-domains) updates.

## [Supported GitLab Products](#supported-gitlab-products)

*   [GitLab Free](https://about.gitlab.com/pricing/)
*   [GitLab Premium](https://about.gitlab.com/pricing/)
*   [GitLab Ultimate](https://about.gitlab.com/pricing/)
*   [GitLab Enterprise](https://about.gitlab.com/enterprise/)
*   [Self-Managed GitLab](#using-gitlab-pipelines)

## [Deploying a GitLab Repository](#deploying-a-gitlab-repository)

The [Deploying a Git repository](/docs/git#deploying-a-git-repository) guide outlines how to create a new Vercel Project from a GitLab repository, and enable automatic deployments on every branch push.

## [Changing the GitLab Repository of a Project](#changing-the-gitlab-repository-of-a-project)

If you'd like to connect your Vercel Project to a different GitLab repository or disconnect it, you can do so from the [Git section](/docs/projects/overview#git) in the Project Settings.

### [A Deployment for Each Push](#a-deployment-for-each-push)

Vercel for GitLab will deploy each push by default. This includes pushes and pull requests made to branches. This allows those working within the project to preview the changes made before they are pushed to production.

With each new push, if Vercel is already building a previous commit on the same branch, the current build will complete and any commit pushed during this time will be queued. Once the first build completes, the most recent commit will begin deployment and the other queued builds will be cancelled. This ensures that you always have the latest changes deployed as quickly as possible.

### [Updating the Production Domain](#updating-the-production-domain)

If [Custom Domains](/docs/projects/custom-domains) are set from a project domains dashboard, pushes and merges to the [Production Branch](/docs/git#production-branch) (commonly "main") will be made live to those domains with the latest deployment made with a push.

If you decide to revert a commit that has already been deployed to production, the previous [Production Deployment](/docs/deployments/environments#production-environment) from a commit will automatically be made available at the [Custom Domain](/docs/projects/custom-domains) instantly; providing you with instant rollbacks.

### [Preview URLs for Each Merge Request](#preview-urls-for-each-merge-request)

The latest push to any [merge request](https://docs.gitlab.com/ee/user/project/merge_requests/) will automatically be made available at a unique preview URL based on the project name, branch, and team or username. These URLs will be provided through a comment on each merge request.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fguides%2Fgetting-started-with-vercel-for-gitlab%2Fmerge-request-alias.png&w=1920&q=75)

A preview URL created from a merge request.

### [System environment variables](#system-environment-variables)

You may want to use different workflows and APIs based on Git information. To support this, the following [System Environment Variables](/docs/environment-variables/system-environment-variables) are exposed to your Deployments:

  

### [VERCEL\_GIT\_PROVIDER](#VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from. In the case of GitLab, the value is always `gitlab`.

### [VERCEL\_GIT\_REPO\_SLUG](#VERCEL_GIT_REPO_SLUG)

The GitLab name of the deployed project.

.env

```
VERCEL_GIT_REPO_SLUG=my-site
```

### [VERCEL\_GIT\_REPO\_OWNER](#VERCEL_GIT_REPO_OWNER)

The GitLab user, group, or sub-group that the project belongs to.

.env

```
VERCEL_GIT_REPO_OWNER=acme
```

### [VERCEL\_GIT\_REPO\_ID](#VERCEL_GIT_REPO_ID)

The GitLab ID of the deployed project.

.env

```
VERCEL_GIT_REPO_ID=13343236
```

### [VERCEL\_GIT\_COMMIT\_REF](#VERCEL_GIT_COMMIT_REF)

The GitLab branch that the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VERCEL\_GIT\_COMMIT\_SHA](#VERCEL_GIT_COMMIT_SHA)

The GitLab sha of the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VERCEL\_GIT\_COMMIT\_MESSAGE](#VERCEL_GIT_COMMIT_MESSAGE)

The message accompanying the GitLab commit that the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_MESSAGE=Add John Doe to about page
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username belonging to the author of the commit that was deployed on GitLab.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name belonging to the author of the commit that was deployed on GitLab.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VERCEL\_GIT\_PULL\_REQUEST\_ID](#VERCEL_GIT_PULL_REQUEST_ID)

The GitLab merge request id the deployment was triggered by. If a deployment is created on a branch before a merge request is made, this value will be an empty string.

.env

```
VERCEL_GIT_PULL_REQUEST_ID=23
```

We require some permissions through our Vercel for GitLab integration. Below are listed the permissions required and a description for what they are used for.

| Permission | Read | Write | Description |
| --- | --- | --- | --- |
| `API` | Y | Y | Allows us access to the API—including all groups and projects, the container registry, and the package registry—to clone repositories and add comments to pull requests and commits. |

We use the permissions above in order to provide you with the best possible deployment experience. If you have any questions or concerns about any of the permission scopes, please [contact Vercel Support](/help#issues).

To sign up on Vercel with a different GitLab account, sign out of your current GitLab account.

Then, restart the Vercel [signup process](/signup).

## [Missing Git repository](#missing-git-repository)

When importing or connecting a GitLab repository, we require that you have Maintainer access to the corresponding repository, so that we can configure a webhook and automatically deploy pushed commits. If your repository belongs to a [Gitlab group](https://docs.gitlab.com/ee/user/group/), you need to have Maintainer access to the group as well. You can use the [Group and project access requests API](https://docs.gitlab.com/ee/api/access_requests.html#valid-access-levels) to find the access levels for a group.

If a repository is missing when you try to import or connect it, make sure that you have [Maintainer access configured for the repository](https://docs.gitlab.com/ee/user/project/members/).

## [Silence comments](#silence-comments)

By default, comments from the Vercel bot will appear on your pull requests and commits. You can silence these comments in your project's settings:

1.  From the Vercel [dashboard](/dashboard), select your project
2.  From the Settings tab, select Git
3.  Under Connected Git Repository, toggle the switches to your preference

It is currently not possible to prevent comments for specific branches.

## [Using GitLab Pipelines](#using-gitlab-pipelines)

You can use GitLab Pipelines to build and deploy your Vercel Application.

`vercel build` allows you to build your project inside GitLab Pipelines, without exposing your source code to Vercel. Then, `vercel deploy --prebuilt` skips the build step on Vercel and uploads the previously generated `.vercel/output` folder to Vercel from the GitLab Pipeline.

[Learn more about how to configure GitLab Pipelines and Vercel](https://vercel.com/guides/how-can-i-use-gitlab-pipelines-with-vercel) for custom CI/CD workflows.

In some cases, your GitLab merge pipeline can fail while your branch pipeline succeeds, allowing your merge requests to [merge with failing tests](https://gitlab.com/gitlab-org/gitlab/-/issues/384927#top). This is a GitLab issue. To avoid it, we recommend using [Vercel CLI](/docs/cli/deploying-from-cli) to deploy your projects.

--------------------------------------------------------------------------------
title: "Glossary"
description: "Learn about the terms and concepts used in Vercel's products and documentation."
last_updated: "null"
source: "https://vercel.com/docs/glossary"
--------------------------------------------------------------------------------

# Glossary

Copy page

Ask AI about this page

Last updated October 30, 2025

A full glossary of terms used in Vercel's products and documentation.

## [A](#a)

### [Active CPU](#active-cpu)

A pricing model for [Fluid Compute](/docs/fluid-compute) where you only pay for the actual CPU time your functions use while executing, rather than provisioned capacity.

### [AI Gateway](#ai-gateway)

A proxy service from Vercel that routes model requests to various AI providers, offering a unified API, budget management, usage monitoring, load balancing, and fallback capabilities. Available in beta.

### [AI SDK](#ai-sdk)

A TypeScript toolkit designed to help developers build AI-powered applications with React, Next.js, Vue, Svelte, and Node.js by providing unified APIs for multiple LLM providers.

### [Analytics](#analytics)

See [Web Analytics](#web-analytics).

### [Anycast Network](#anycast-network)

A network topology that shares an IP address among multiple nodes, routing requests to the nearest available node based on network conditions to improve performance and fault tolerance.

## [B](#b)

### [Build](#build)

The process that Vercel performs every time you deploy your code, compiling, bundling, and optimizing your application so it's ready to serve to users.

### [Build Cache](#build-cache)

A cache that stores build artifacts and dependencies to speed up subsequent deployments. Each build cache can be up to 1 GB and is retained for one month.

### [Build Command](#build-command)

The command used to build your project during deployment. Vercel automatically configures this based on your framework, but it can be overridden.

### [Build Output API](#build-output-api)

A file-system-based specification for a directory structure that can produce a Vercel deployment, primarily targeted at framework authors.

### [Bot Protection](#bot-protection)

Security features that help identify and block malicious bots and crawlers from accessing your applications.

## [C](#c)

### [CDN (Content Delivery Network)](#cdn-content-delivery-network)

A distributed network of servers that stores static content in multiple locations around the globe to serve content from the closest server to users.

### [CI/CD (Continuous Integration/Continuous Deployment)](#ci/cd-continuous-integration/continuous-deployment)

Development practices where code changes are automatically built, tested, and deployed. Vercel provides built-in CI/CD through Git integrations.

### [CLI (Command Line Interface)](#cli-command-line-interface)

The Vercel CLI is a command-line tool that allows you to deploy projects, manage deployments, and configure Vercel from your terminal.

### [Compute](#compute)

The processing power and execution environment where your application code runs. Vercel offers serverless compute through Functions and Edge compute through Middleware.

### [Concurrency](#concurrency)

The ability to handle multiple requests simultaneously. Vercel Functions support concurrency scaling and [Fluid Compute](/docs/fluid-compute) offers enhanced concurrency.

### [Core Web Vitals](#core-web-vitals)

Key metrics defined by Google that assess your web application's loading speed, responsiveness, and visual stability, including LCP, FID, and CLS.

### [Cron Jobs](#cron-jobs)

Scheduled tasks that run at specified intervals. Vercel supports cron jobs for automating recurring processes.

### [Custom Domain](#custom-domain)

A domain that you own and configure to point to your Vercel deployment, replacing the default `.vercel.app` domain.

## [D](#d)

### [Data Cache](#data-cache)

A specialized cache that stores responses from data fetches in frameworks like Next.js, allowing for granular caching per fetch rather than per route.

### [DDoS (Distributed Denial of Service)](#ddos-distributed-denial-of-service)

A type of cyber attack where multiple systems flood a target with traffic. Vercel provides built-in DDoS protection and mitigation.

### [Deploy Hooks](#deploy-hooks)

URLs that accept HTTP POST requests to trigger deployments without requiring a new Git commit.

### [Deployment](#deployment)

The result of a successful build of your project on Vercel. Each deployment generates a unique URL and represents a specific version of your application.

### [Deployment Protection](#deployment-protection)

Security features that restrict access to your deployments using methods like Vercel Authentication, Password Protection, or Trusted IPs.

### [Directory](#directory)

A file system structure used to organize and store files, also known as a folder. Often abbreviated as "dir" in programming contexts.

## [E](#e)

### [Edge](#edge)

The edge refers to servers closest to users in a distributed network. Vercel's CDN runs code and serves content from edge locations globally.

### [Edge Config](#edge-config)

A global data store that enables ultra-fast data reads at the edge (typically under 1ms) for configuration data like feature flags.

### [CDN (Content Delivery Network)](#cdn-content-delivery-network)

Vercel's global infrastructure consisting of Points of Presence (PoPs) and compute-capable regions that serve content and run code close to users.

### [Edge Runtime](#edge-runtime)

A minimal JavaScript runtime that exposes Web Standard APIs, used for Vercel Functions and Routing Middleware.

### [Environment](#environment)

A context for running your application, such as Local Development, Preview, or Production. Each environment can have its own configuration and environment variables.

### [Environment Variables](#environment-variables)

Configuration values that can be accessed by your application at build time or runtime, used for API keys, database connections, and other sensitive information.

## [F](#f)

### [Fast Data Transfer](#fast-data-transfer)

Data transfer between the Vercel CDN and user devices, optimized for performance and charged based on usage.

### [Feature Flags](#feature-flags)

Configuration switches that allow you to enable or disable features in your application without deploying new code, often stored in Edge Config.

### [Firewall](#firewall)

See [Vercel Firewall](#vercel-firewall).

### [Fluid Compute](#fluid-compute)

An enhanced execution model for Vercel Functions that provides in-function concurrency, and a new pricing model where you only pay for the actual CPU time your functions use while executing, rather than provisioned capacity.

### [Framework](#framework)

A software library that provides a foundation for building applications. Vercel supports over 30 frameworks including Next.js, React, Vue, and Svelte.

### [Framework Preset](#framework-preset)

A configuration setting that tells Vercel which framework your project uses, enabling automatic optimization and build configuration.

### [Functions](#functions)

See [Vercel Functions](#vercel-functions).

## [G](#g)

### [Git Integration](#git-integration)

Automatic connection between your Git repository (GitHub, GitLab, Bitbucket, Azure DevOps) and Vercel for continuous deployment.

## [H](#h)

### [Headers](#headers)

HTTP headers that can be configured to modify request and response behavior, improving security, performance, and functionality.

### [HTTPS/SSL](#https/ssl)

Secure HTTP protocol that encrypts communication between clients and servers. All Vercel deployments automatically use HTTPS with SSL certificates.

## [I](#i)

### [I/O-bound](#i/o-bound)

Processes limited by input/output operations rather than CPU speed, such as database queries or API requests. Optimized through concurrency.

### [Image Optimization](#image-optimization)

Automatic optimization of images including format conversion, resizing, and compression to improve performance and reduce bandwidth.

### [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)

A feature that allows you to update static content without redeployment by rebuilding pages in the background on a specified interval.

### [Install Command](#install-command)

The command used to install dependencies before building your project, such as `npm install` or `pnpm install`.

### [Integration](#integration)

Third-party services and tools that connect with Vercel to extend functionality, available through the Vercel Marketplace.

## [J](#j)

### [JA3/JA4 Fingerprints](#ja3/ja4-fingerprints)

TLS fingerprinting techniques used by Vercel's security systems to identify and restrict malicious traffic patterns.

## [L](#l)

### [Drains](#drains)

A feature that allows you to send observability data (logs, traces, speed insights, and analytics) to external services for long-term retention and analysis.

## [M](#m)

### [Managed Infrastructure](#managed-infrastructure)

Vercel's fully managed platform that handles server provisioning, scaling, security, and maintenance automatically.

### [MCP (Model Context Protocol)](#mcp-model-context-protocol)

A protocol for AI applications that enables secure and standardized communication between AI models and external data sources.

### [Middleware](#middleware)

Code that executes before a request is processed, running at the edge to modify responses, implement authentication, or perform redirects.

### [Microfrontends](#microfrontends)

A development approach that allows you to split a single application into smaller, independently deployable units that render as one cohesive application for users. Different teams can use different technologies to develop, test, and deploy each microfrontend independently.

### [Monorepo](#monorepo)

A version control strategy where multiple packages or modules are stored in a single repository, facilitating code sharing and collaboration.

### [Multi-repo](#multi-repo)

A version control strategy where each package or module has its own separate repository, also known as "polyrepo."

### [Multi-tenant](#multi-tenant)

Applications that serve multiple customers (tenants) from a single codebase, with each tenant getting their own domain or subdomain.

## [N](#n)

### [Node.js](#node.js)

A JavaScript runtime environment that Vercel supports for Vercel Functions and applications.

## [O](#o)

### [Observability](#observability)

Tools and features that help you monitor, analyze, and understand your application's performance, traffic, and behavior in production.

### [OIDC (OpenID Connect)](#oidc-openid-connect)

A federation protocol that issues short-lived, non-persistent tokens for secure backend access without storing long-lived credentials.

### [Origin Server](#origin-server)

The server that stores and runs the original version of your application code, where requests are processed when not served from cache.

### [Output Directory](#output-directory)

The folder containing your final build output after the build process completes, such as `dist`, `build`, or `.next`.

## [P](#p)

### [Package](#package)

A collection of files and directories grouped together for a common purpose, such as libraries, applications, or development tools.

### [Password Protection](#password-protection)

A deployment protection method that restricts access to deployments using a password, available on Enterprise plans or as a Pro add-on.

### [Points of Presence (PoPs)](#points-of-presence-pops)

Distributed servers in Vercel's CDN that provide the first point of contact for requests, handling routing, DDoS protection, and SSL termination.

### [Preview Deployment](#preview-deployment)

A deployment created from non-production branches that allows you to test changes in a live environment before merging to production.

### [Production Deployment](#production-deployment)

The live version of your application that serves end users, typically deployed from your main branch.

### [Project](#project)

An application that you have deployed to Vercel, which can have multiple deployments and is connected to a Git repository.

## [R](#r)

### [Real Experience Score (RES)](#real-experience-score-res)

A performance metric in Speed Insights that uses real user data to measure your application's actual performance in production.

### [Redirects](#redirects)

HTTP responses that tell clients to make a new request to a different URL, useful for enforcing HTTPS or directing traffic.

### [Region](#region)

Geographic locations where Vercel can run your functions and store data. Vercel has 19 compute-capable regions globally.

### [Repository](#repository)

A location where files and source code are stored and managed in version control systems like Git, maintaining history of all changes.

### [Rewrites](#rewrites)

URL transformations that change what the server fetches internally without changing the URL visible to the client.

### [Runtime](#runtime)

The execution environment for your functions, such as Node.js, Edge Runtime, Python, or other supported runtimes.

### [Runtime Logs](#runtime-logs)

Logs generated by your functions during execution, useful for debugging and monitoring application behavior.

## [S](#s)

### [SAML SSO (Single Sign-On)](#saml-sso-single-sign-on)

An authentication protocol that allows teams to log into Vercel using their organization's identity provider.

### [Sandbox](#sandbox)

See [Vercel Sandbox](#vercel-sandbox).

### [Secure Compute](#secure-compute)

An Enterprise feature that creates private connections between Vercel Functions and backend infrastructure using dedicated IP addresses.

### [Serverless](#serverless)

A cloud computing model where code runs without managing servers, automatically scaling based on demand and charging only for actual usage.

### [Speed Insights](#speed-insights)

Performance monitoring that provides detailed insights into your website's Core Web Vitals and loading performance metrics.

### [Storage](#storage)

Vercel's suite of storage products including Blob storage for files and Edge Config for configuration data.

### [Streaming](#streaming)

A technique for sending data progressively from functions to improve perceived performance and responsiveness.

## [T](#t)

### [Trusted IPs](#trusted-ips)

A deployment protection method that restricts access to deployments based on IP address allowlists, available on Enterprise plans.

### [Turborepo](#turborepo)

A high-performance build system for monorepos that provides fast incremental builds and remote caching capabilities.

## [V](#v)

### 

An AI-powered tool that converts natural language descriptions into React code and UI components, integrated with Vercel for deployment.

### [Vercel Authentication](#vercel-authentication)

A deployment protection method that restricts access to team members and authorized users with Vercel accounts.

### [Vercel Blob](#vercel-blob)

Scalable object storage service for static assets like images, videos, and files, optimized for global content delivery.

### [Vercel Firewall](#vercel-firewall)

A multi-layered security system that protects applications from threats, including platform-wide DDoS protection and customizable WAF rules.

### [Vercel Functions](#vercel-functions)

Serverless compute that allows you to run server-side code without managing servers, automatically scaling based on demand.

### [Vercel Sandbox](#vercel-sandbox)

An ephemeral compute primitive for safely running untrusted or user-generated code in isolated Linux VMs.

### [Virtual Experience Score (VES)](#virtual-experience-score-ves)

A predictive performance metric that anticipates the impact of changes on application performance before deployment.

## [W](#w)

### [WAF (Web Application Firewall)](#waf-web-application-firewall)

A customizable security layer that allows you to define rules to protect against attacks, scrapers, and unwanted traffic.

### [Web Analytics](#web-analytics)

Privacy-friendly analytics that provide insights into website visitors, page views, and user behavior without using cookies.

### [Workspace](#workspace)

In JavaScript, an entity in a repository that can be either a single package or a collection of packages, often at the repository root.

--------------------------------------------------------------------------------
title: "Headers"
description: "This reference covers the list of request, response, cache-control, and custom response headers included with deployments with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/headers"
--------------------------------------------------------------------------------

# Headers

Copy page

Ask AI about this page

Last updated September 9, 2025

Headers are small pieces of information that are sent between the client (usually a web browser) and the server. They contain metadata about the request and response, such as the content type, cache-control directives, and authentication tokens. [HTTP headers](https://developer.mozilla.org/docs/Web/HTTP/Headers) can be found in both the HTTP Request and HTTP Response.

## [Using headers](#using-headers)

By using headers effectively, you can optimize the performance and security of your application on Vercel's edge network. Here are some tips for using headers on Vercel:

1.  [Use caching headers](#cache-control-header): Caching headers instruct the client and server to cache resources like images, CSS files, and JavaScript files, so they don't need to be reloaded every time a user visits your site. By using caching headers, you can significantly reduce the time it takes for your site to load.
2.  [Use compression headers](/docs/compression#compression-with-vercel-cdn): Use the `Accept-Encoding` header to tell the client and server to compress data before it's sent over the network. By using compression, you can reduce the amount of data that needs to be sent, resulting in faster load times.
3.  Use custom headers: You can also use custom headers in your `vercel.json` file to add metadata specific to your application. For example, you could add a header that indicates the user's preferred language or the version of your application. See [Project Configuration](/docs/project-configuration#headers) docs for more information.

## [Request headers](#request-headers)

To learn about the request headers sent to each Vercel deployment and how to use them to process requests before sending a response, see [Request headers](/docs/headers/request-headers).

## [Response headers](#response-headers)

To learn about the response headers included in Vercel deployment responses and how to use them to process responses before sending a response, see [Response headers](/docs/headers/response-headers).

## [Cache-Control header](#cache-control-header)

To learn about the cache-control headers sent to each Vercel deployment and how to use them to control the caching behavior of your application, see [Cache-Control headers](/docs/headers/cache-control-headers).

## [More resources](#more-resources)

*   [Set Caching Header](/guides/set-cache-control-headers)

--------------------------------------------------------------------------------
title: "Cache-Control headers"
description: "Learn about the cache-control headers sent to each Vercel deployment and how to use them to control the caching behavior of your application."
last_updated: "null"
source: "https://vercel.com/docs/headers/cache-control-headers"
--------------------------------------------------------------------------------

# Cache-Control headers

Copy page

Ask AI about this page

Last updated September 24, 2025

You can control how Vercel's CDN caches your Function responses by setting a [Cache-Control headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Cache-Control) header.

## [Default `cache-control` value](#default-cache-control-value)

The default value is `cache-control: public, max-age=0, must-revalidate` which instructs both the CDN and the browser not to cache.

## [Recommended settings](#recommended-settings)

We recommend that you set your cache to`max-age=0, s-maxage=86400`, adjusting 86400 to the number of seconds you want the response cached. This configuration tells browsers not to cache, allowing Vercel's CDN to cache responses and invalidate them when deployments update.

## [`s-maxage`](#s-maxage)

This directive sets the number of seconds a response is considered "fresh" by the CDN. After this period ends, Vercel's CDN will serve the "stale" response from the edge until the response is asynchronously revalidated with a "fresh" response to your Vercel Function.

`s-maxage` is consumed by Vercel's proxy and not included as part the final HTTP response to the client.

### [`s-maxage` example](#s-maxage-example)

The following example instructs the CDN to cache the response for 60 seconds. A response can be cached a minimum of `1` second and maximum of `31536000` seconds (1 year).

cache-response

```
Cache-Control: s-maxage=60
```

## [`stale-while-revalidate`](#stale-while-revalidate)

This `cache-control` directive allows you to serve content from the Vercel cache while simultaneously updating the cache in the background with the response from your function. It is useful when:

*   Your content changes frequently, but regeneration is slow, such as content that relies on an expensive database query or upstream API request
*   Your content changes infrequently but you want to have the flexibility to update it without waiting for the cache to expire

`stale-while-revalidate` is consumed by Vercel's proxy and not included as part the final HTTP response to the client. This allows you to deliver the latest content to your visitors right after creating a new deployment (as opposed to waiting for browser cache to expire). It also prevents content-flash.

### [SWR example](#swr-example)

The following example instructs the CDN to:

*   Serve content from the cache for 1 second
*   Return a stale request (if requested after 1 second)
*   Update the cache in the background asynchronously (if requested after 1 second)

swr-on-edge-network

```
Cache-Control: s-maxage=1, stale-while-revalidate=59
```

The first request is served synchronously. Subsequent requests are served from the cache and revalidated asynchronously if the cache is "stale".

If you need to do a _synchronous_ revalidation you can set the `pragma: no-cache` header along with the `cache-control` header. This can be used to understand how long the background revalidation took. It sets the `x-vercel-cache` header to `REVALIDATED`.

Many browser developer tools set `pragma: no-cache` by default, which reveals the true load time of the page with the synchronous update to the cache.

## [`stale-if-error`](#stale-if-error)

This directive is currently not supported. `stale-if-error` is consumed by Vercel's proxy, and will not be included in the HTTP response sent to the client.

## [`proxy-revalidate`](#proxy-revalidate)

This directive is currently not supported.

## [Using `private`](#using-private)

Using the `private` directive specifies that the response can only be cached by the client and not by Vercel's CDN. Use this directive when you want to cache content on the user's browser, but prevent caching on Vercel's CDN.

## [`Pragma: no-cache`](#pragma:-no-cache)

When Vercel's CDN receives a request with `Pragma: no-cache` (such as when the browser devtools are open), it will revalidate any stale resource synchronously, instead of in the background.

## [CDN-Cache-Control Header](#cdn-cache-control-header)

Sometimes the directives you set in a `Cache-Control` header can be interpreted differently by the different CDNs and proxies your content passes through between the origin server and a visitor's browser. To explicitly control caching you can use targeted cache control headers.

The `CDN-Cache-Control` and `Vercel-CDN-Cache-Control` headers are response headers that can be used to specify caching behavior on the CDN.

You can use the same directives as [`Cache-Control`](#default-cache-control-value), but `CDN-Cache-Control` is only used by the CDN.

## [Behavior](#behavior)

Origins can set the following headers:

*   `Vercel-CDN-Cache-Control`
*   `CDN-Cache-Control`
*   `Cache-Control`

When multiple of the above headers are set, Vercel's CDN will use the following priority to determine the caching behavior:

### [`Vercel-CDN-Cache-Control`](#vercel-cdn-cache-control)

`Vercel-CDN-Cache-Control` is exclusive to Vercel and has top priority, whether it's defined in a Vercel Function response or a `vercel.json` file. It controls caching behavior only within Vercel's Cache. It is removed from the response and not sent to the client or any CDNs.

### [`CDN-Cache-Control`](#cdn-cache-control)

`CDN-Cache-Control` is second in priority after `Vercel-CDN-Cache-Control`, and always overrides `Cache-Control` headers, whether defined in a Vercel Function response or a `vercel.json` file.

By default, `CDN-Cache-Control` configures Vercel's Cache and is used by other CDNs, allowing you to configure intermediary caches. If `Vercel-CDN-Cache-Control` is also set, `CDN-Cache-Control` only influences other CDN caches.

### [`Cache-Control`](#cache-control)

`Cache-Control` is a web standard header and last in priority. If neither `CDN-Cache-Control` nor `Vercel-CDN-Cache-Control` are set, this header will be used by Vercel's Cache before being forwarded to the client.

You can still set `Cache-Control` while using the other two, and it will be forwarded to the client as is.

If only `Cache-Control` is used, Vercel strips the `s-maxage` directive from the header before it's sent to the client.

## [Cache-Control comparison tables](#cache-control-comparison-tables)

The following tables demonstrate how Vercel's Cache behaves in different scenarios:

### [Functions have priority over config files](#functions-have-priority-over-config-files)

`Cache-Control` headers returned from Vercel Functions take priority over `Cache-Control` headers from `next.config.js` or `vercel.json` files.

| Parameter | Value |
| --- | --- |
| Vercel Function response headers | `Cache-Control: s-maxage=60` |
| `vercel.json` or `next.config.js` headers | `Cache-Control: s-maxage: 120` |
| Cache behavior | 60s TTL |
| Headers sent to the client | `Cache-Control: public, max-age: 0` |

### [`CDN-Cache-Control` priority](#cdn-cache-control-priority)

`CDN-Cache-Control` has priority over `Cache-Control`, even if defined in `vercel.json` or `next.config.js`.

| Parameter | Value |
| --- | --- |
| Vercel Function response headers | `Cache-Control: s-maxage=60` |
| `vercel.json` or `next.config.js` headers | `CDN-Cache-Control: max-age=120` |
| Cache behavior | 120s TTL |
| Headers sent to the client | `Cache-Control: s-maxage=60 CDN-Cache-Control: max-age=120` |

### [`Vercel-CDN-Cache-Control` priority](#vercel-cdn-cache-control-priority)

`Vercel-CDN-Cache-Control` has priority over both `CDN-Cache-Control` and `Cache-Control`. It only applies to Vercel, so it is not returned with the other headers, which will control cache behavior on the browser and other CDNs.

| Parameter | Value |
| --- | --- |
| Vercel Function response headers | `CDN-Cache-Control: max-age=120` |
| `vercel.json` or `next.config.js` headers | `Cache-Control: s-maxage=60 Vercel-CDN-Cache-Control: max-age=300` |
| Cache behavior | 300s TTL |
| Headers sent to the client | `Cache-Control: s-maxage=60 CDN-Cache-Control: max-age=120` |

## [Which Cache-Control headers to use with CDNs](#which-cache-control-headers-to-use-with-cdns)

*   If you want to control caching similarly on Vercel, CDNs, and the client, use `Cache-Control`
*   If you want to control caching on Vercel and also on other CDNs, use `CDN-Cache-Control`
*   If you want to control caching only on Vercel, use `Vercel-CDN-Cache-Control`
*   If you want to specify different caching behaviors for Vercel, other CDNs, and the client, you can set all three headers

## [Example usage](#example-usage)

The following example demonstrates `Cache-Control` headers that instruct:

*   Vercel's Cache to have a [TTL](https://en.wikipedia.org/wiki/Time_to_live) of `3600` seconds
*   Downstream CDNs to have a TTL of `60` seconds
*   Clients to have a TTL of `10` seconds

Next.js (/app)Next.js (/pages)Other frameworks

app/api/cache-control-headers/route.ts

TypeScript

TypeScriptJavaScript

```
export async function GET() {
  return new Response('Cache Control example', {
    status: 200,
    headers: {
      'Cache-Control': 'max-age=10',
      'CDN-Cache-Control': 'max-age=60',
      'Vercel-CDN-Cache-Control': 'max-age=3600',
    },
  });
}
```

## [Custom Response Headers](#custom-response-headers)

Using configuration, you can assign custom headers to each response.

Custom headers can be configured with the `headers` property in [`next.config.js`](https://nextjs.org/docs/api-reference/next.config.js/headers) for Next.js projects, or it can be configured in [`vercel.json`](/docs/project-configuration#headers) for all other projects.

Alternatively, a [Vercel Function](/docs/functions) can assign headers to the [Response](https://nodejs.org/api/http.html#http_response_setheader_name_value) object.

Response headers `x-matched-path`, `server`, and `content-length` are reserved and cannot be modified.

--------------------------------------------------------------------------------
title: "Request headers"
description: "Learn about the request headers sent to each Vercel deployment and how to use them to process requests before sending a response."
last_updated: "null"
source: "https://vercel.com/docs/headers/request-headers"
--------------------------------------------------------------------------------

# Request headers

Copy page

Ask AI about this page

Last updated September 9, 2025

The following headers are sent to each Vercel deployment and can be used to process the request before sending back a response. These headers can be read from the [Request](https://nodejs.org/api/http.html#http_message_headers) object in your [Vercel Function](/docs/functions).

## [`host`](#host)

This header represents the domain name as it was accessed by the client. If the deployment has been assigned to a preview URL or production domain and the client visits the domain URL, it contains the custom domain instead of the underlying deployment URL.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const host = request.headers.get('host');
  return new Response(`Host: ${host}`);
}
```

## [`x-vercel-id`](#x-vercel-id)

This header contains a list of [Vercel regions](/docs/regions) your request hit, as well as the region the function was executed in (for both Edge and Serverless).

It also allows Vercel to automatically prevent infinite loops.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const vercelId = request.headers.get('x-vercel-id');
  return new Response(`Vercel ID: ${vercelId}`);
}
```

## [`x-forwarded-host`](#x-forwarded-host)

This header is identical to the `host` header.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const host = request.headers.get('x-forwarded-host');
  return new Response(`Host: ${host}`);
}
```

## [`x-forwarded-proto`](#x-forwarded-proto)

This header represents the protocol of the forwarded server, typically `https` in production and `http`in development.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const protocol = request.headers.get('x-forwarded-proto');
  return new Response(`Protocol: ${protocol}`);
}
```

## [`x-forwarded-for`](#x-forwarded-for)

The public IP address of the client that made the request.

If you are trying to use Vercel behind a proxy, we currently overwrite the [`X-Forwarded-For`](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Forwarded-For) header and do not forward external IPs. This restriction is in place to prevent IP spoofing.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const ip = request.headers.get('x-forwarded-for');
  return new Response(`IP: ${ip}`);
}
```

### [Custom `X-Forwarded-For` IP](#custom-x-forwarded-for-ip)

Trusted Proxy is available on [Enterprise plans](/docs/plans/enterprise)

Enterprise customers can purchase and enable a trusted proxy to allow your custom `X-Forwarded-For` IP. [Contact us](/contact/sales) for more information.

## [`x-vercel-forwarded-for`](#x-vercel-forwarded-for)

This header is identical to the `x-forwarded-for` header. However, `x-forwarded-for` could be overwritten if you're using a proxy on top of Vercel.

## [`x-real-ip`](#x-real-ip)

This header is identical to the `x-forwarded-for` header.

## [`x-vercel-deployment-url`](#x-vercel-deployment-url)

This header represents the unique deployment, not the preview URL or production domain. For example, `*.vercel.app`.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const deploymentUrl = request.headers.get('x-vercel-deployment-url');
  return new Response(`Deployment URL: ${deploymentUrl}`);
}
```

## [`x-vercel-ip-continent`](#x-vercel-ip-continent)

A two-character [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) code representing the continent associated with the location of the requester's public IP address. Codes used to identify continents are as follows:

*   `AF` for Africa
*   `AN` for Antarctica
*   `AS` for Asia
*   `EU` for Europe
*   `NA` for North America
*   `OC` for Oceania
*   `SA` for South America

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const continent = request.headers.get('x-vercel-ip-continent');
  return new Response(`Continent: ${continent}`);
}
```

## [`x-vercel-ip-country`](#x-vercel-ip-country)

A two-character [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code for the country associated with the location of the requester's public IP address.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const country = request.headers.get('x-vercel-ip-country');
  return new Response(`Country: ${country}`);
}
```

## [`x-vercel-ip-country-region`](#x-vercel-ip-country-region)

A string of up to three characters containing the region-portion of the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) code for the first level region associated with the requester's public IP address. Some countries have two levels of subdivisions, in which case this is the least specific one. For example, in the United Kingdom this will be a country like "England", not a county like "Devon".

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const region = request.headers.get('x-vercel-ip-country-region');
  return new Response(`Region: ${region}`);
}
```

## [`x-vercel-ip-city`](#x-vercel-ip-city)

The city name for the location of the requester's public IP address. Non-ASCII characters are encoded according to [RFC3986](https://tools.ietf.org/html/rfc3986).

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const city = request.headers.get('x-vercel-ip-city');
  return new Response(`City: ${city}`);
}
```

## [`x-vercel-ip-latitude`](#x-vercel-ip-latitude)

The latitude for the location of the requester's public IP address. For example, `37.7749`.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const latitude = request.headers.get('x-vercel-ip-latitude');
  return new Response(`Latitude: ${latitude}`);
}
```

## [`x-vercel-ip-longitude`](#x-vercel-ip-longitude)

The longitude for the location of the requester's public IP address. For example, `-122.4194`.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const longitude = request.headers.get('x-vercel-ip-longitude');
  return new Response(`Longitude: ${longitude}`);
}
```

## [`x-vercel-ip-timezone`](#x-vercel-ip-timezone)

The name of the time zone for the location of the requester's public IP address in ICANN Time Zone Database name format such as `America/Chicago`.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const timezone = request.headers.get('x-vercel-ip-timezone');
  return new Response(`Timezone: ${timezone}`);
}
```

## [`x-vercel-ip-postal-code`](#x-vercel-ip-postal-code)

The postal code close to the user's location.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  const postalCode = request.headers.get('x-vercel-ip-postal-code');
  return new Response(`Postal Code: ${postalCode}`);
}
```

## [`x-vercel-signature`](#x-vercel-signature)

The signature of the request. This header is used to verify that the request was sent by Vercel, and contains a hash signature you can use to validate the request body.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/header/route.ts

TypeScript

TypeScriptJavaScript

```
export function POST(request: Request) {
  const signature = request.headers.get('x-vercel-signature');
  return new Response(`Signature: ${signature}`);
}
```

--------------------------------------------------------------------------------
title: "Response headers"
description: "Learn about the response headers sent to each Vercel deployment and how to use them to process responses before sending a response."
last_updated: "null"
source: "https://vercel.com/docs/headers/response-headers"
--------------------------------------------------------------------------------

# Response headers

Copy page

Ask AI about this page

Last updated September 15, 2025

The following headers are included in Vercel deployment responses and indicate certain factors of the environment. These headers can be viewed from the Browser's Dev Tools or using an HTTP client such as `curl -I <DEPLOYMENT_URL>`.

## [`cache-control`](#cache-control)

Used to specify directives for caching mechanisms in both the [Network layer cache](/docs/edge-cache) and the browser cache. See the [Cache Control Headers](/docs/headers#cache-control-header) section for more detail.

If you use this header to instruct the CDN to cache data, such as with the [`s-maxage`](/docs/headers/cache-control-headers#s-maxage) directive, Vercel returns the following `cache-control` header to the client:

\-`cache-control: public, max-age=0, must-revalidate`

## [`content-length`](#content-length)

An integer that indicates the number of bytes in the response.

## [`content-type`](#content-type)

The [media type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types) that describes the nature and format of the response.

## [`date`](#date)

A timestamp indicating when the response was generated.

## [`server: Vercel`](#server:-vercel)

Shows where the request came from. This header can be overridden by other proxies (e.g., Cloudflare).

## [`strict-transport-security`](#strict-transport-security)

A header often abbreviated as [HSTS](https://developer.mozilla.org/docs/Glossary/HSTS) that tells browsers that the resource should only be requested over HTTPS. The default value is `strict-transport-security: max-age=63072000` (2 years)

## [`x-robots-tag`](#x-robots-tag)

Present only on:

*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production)
*   Outdated [production deployments](/docs/deployments). When you [promote a new deployment to production](/docs/deployments/promoting-a-deployment), the `x-robots-tag` header will be sent to requests for outdated production deployments

We add this header automatically with a value of `noindex` to prevent search engines from crawling your Preview Deployments and outdated Production Deployments, which could cause them to penalize your site for duplicate content.

You can prevent this header from being added to your Preview Deployment by:

*   [Assigning a production domain](/docs/domains/working-with-domains/assign-domain-to-a-git-branch) to it
*   Disabling it manually [using vercel.json](/docs/project-configuration#headers)

## [`x-vercel-cache`](#x-vercel-cache)

The `x-vercel-cache` header is primarily used to indicate the cache status of static assets and responses from Vercel's CDN. For dynamic routes and fetch requests that utilize the [Vercel Data Cache](/docs/infrastructure/data-cache), this header will often show `MISS` even if the data is being served from the Data Cache. Use [custom headers](/docs/headers/cache-control-headers#custom-response-headers) or [runtime logs](/docs/runtime-logs) to determine if a fetch response was served from the Data Cache.

The following values are possible when the content being served [is static](/docs/edge-cache#static-files-caching) or uses [a Cache-Control header](/docs/headers#cache-control-header):

### [`MISS`](#miss)

The response was not found in the cache and was fetched from the origin server.

![MISS: The response was not found in the cache and was fetched from the origin server](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-miss2x.png%3Flightbox&w=1920&q=75)![MISS: The response was not found in the cache and was fetched from the origin server](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-miss2x.png%3Flightbox&w=1920&q=75)

MISS: The response was not found in the cache and was fetched from the origin server

Zoom Image

![MISS: The response was not found in the cache and was fetched from the origin server](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-miss2x.png%3Flightbox&w=1920&q=75)![MISS: The response was not found in the cache and was fetched from the origin server](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-miss2x.png%3Flightbox&w=1920&q=75)

MISS: The response was not found in the cache and was fetched from the origin server

### [`HIT`](#hit)

The response was served from the cache.

![HIT: The response was served from the cache](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-hit2x.png%3Flightbox&w=1920&q=75)![HIT: The response was served from the cache](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-hit2x.png%3Flightbox&w=1920&q=75)

HIT: The response was served from the cache

Zoom Image

![HIT: The response was served from the cache](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-hit2x.png%3Flightbox&w=1920&q=75)![HIT: The response was served from the cache](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-hit2x.png%3Flightbox&w=1920&q=75)

HIT: The response was served from the cache

### [`STALE`](#stale)

The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.

Cached content can go stale for several different reasons such as:

*   Response included `stale-while-revalidate` Cache-Control response header.
*   Response was served from [ISR](/docs/incremental-static-regeneration) with a revalidation time in frameworks like Next.js.
*   On-demand using `@vercel/functions` like [`invalidateByTag()`](/docs/functions/functions-api-reference/vercel-functions-package#invalidatebytag).
*   On-demand using framework-specific functions like [`revalidatePath()`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) with lifetimes in Next.js.
*   On-demand using the Vercel dashboard [project purge settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fcaches&title=Cache+Purge+Settings) to invalidate by tag.

See [purging the cache](/docs/edge-cache/purge) for more information.

![STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-stale2x.png%3Flightbox&w=1920&q=75)![STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-stale2x.png%3Flightbox&w=1920&q=75)

STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.

Zoom Image

![STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-stale2x.png%3Flightbox&w=1920&q=75)![STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-stale2x.png%3Flightbox&w=1920&q=75)

STALE: The response was served from the cache but the content is no longer fresh, so a background request to the origin server was made to update the content.

### [`PRERENDER`](#prerender)

The response was served from static storage. An example of prerender is in `Next.js`, when setting `fallback:true` in `getStaticPaths`. However, `fallback:blocking` will not return prerender.

![PRERENDER: The response was served from static storage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-prerender2x.png%3Flightbox&w=1920&q=75)![PRERENDER: The response was served from static storage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-prerender2x.png%3Flightbox&w=1920&q=75)

PRERENDER: The response was served from static storage.

Zoom Image

![PRERENDER: The response was served from static storage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-prerender2x.png%3Flightbox&w=1920&q=75)![PRERENDER: The response was served from static storage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-prerender2x.png%3Flightbox&w=1920&q=75)

PRERENDER: The response was served from static storage.

### [`REVALIDATED`](#revalidated)

The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.

The cached content can be deleted in several ways such as:

*   On-demand using `@vercel/functions` like [`dangerouslyDeleteByTag()`](/docs/functions/functions-api-reference/vercel-functions-package#dangerouslydeletebytag).
*   On-demand using framework-specific functions like [`revalidatePath()`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) without a lifetime in Next.js.
*   On-demand using the Vercel dashboard [project purge settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fcaches&title=Cache+Purge+Settings) to delete by tag.

See [purging the cache](/docs/edge-cache/purge) for more information.

![REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-revalidated2x.png%3Flightbox&w=1920&q=75)![REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-revalidated2x.png%3Flightbox&w=1920&q=75)

REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.

Zoom Image

![REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-revalidated2x.png%3Flightbox&w=1920&q=75)![REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fx-vercel-cache-revalidated2x.png%3Flightbox&w=1920&q=75)

REVALIDATED: The response was served from the origin server after the cache was deleted so it must be revalidated in the foreground.

## [`x-vercel-id`](#x-vercel-id)

This header contains a list of [Vercel regions](/docs/regions) your request hit, as well as the region the function was executed in (for both Edge and Serverless).

It also allows Vercel to automatically prevent infinite loops.

--------------------------------------------------------------------------------
title: "Content Security Policy"
description: "Learn how the Content Security Policy (CSP) offers defense against web vulnerabilities, its key features, and best practices."
last_updated: "null"
source: "https://vercel.com/docs/headers/security-headers"
--------------------------------------------------------------------------------

# Content Security Policy

Copy page

Ask AI about this page

Last updated July 18, 2025

Content Security Policy is a browser feature designed to prevent cross-site scripting (XSS) and related code-injection attacks. CSP provides developers with the ability to define an allowlist of sources of trusted content, effectively restricting the browser from loading any resources from non-allowlisted sources.

When a browser receives the `Content-Security-Policy` HTTP header from a web server it adheres to the defined policy, blocking or allowing content loads based on the provided rules.

[XSS](/guides/understanding-xss-attacks) remains one of the most prevalent web application vulnerabilities. In an XSS attack, malicious scripts are injected into websites, which run on the end user's browser, potentially leading to stolen data, session hijacking, and other malicious actions.

CSP can reduce the likelihood of XSS by:

*   Allowlisting content sources – CSP works by specifying which sources of content are legitimate for a web application. You can define a list of valid sources for scripts, images, stylesheets, and other web resources. Any content not loaded from these approved sources will be blocked. Thus, if an attacker tries to inject a script from an unauthorized source, CSP will prevent it from loading and executing.
*   Inline script blocking – A common vector for XSS is through inline scripts, which are scripts written directly within the HTML content. CSP can be configured to block all inline scripts, rendering script tags injected by attackers (like `<script>alert('XSS Attack!')</script>`) ineffective.
*   Disallowing `eval()` – The `eval()` function in JavaScript can be misused to execute arbitrary code, which can be a potential XSS vector. CSP can be set up to disallow the use of `eval()` and its related functions.
*   Nonce and hashes – If there's a need to allow certain inline scripts (while still blocking others), CSP supports a nonce (number used once) that can be added to a script tag. Only scripts with the correct nonce value will be executed. Similarly, CSP can use hashes to allow the execution of specific inline scripts by matching their hash value.
*   Reporting violations – CSP can be set in `report-only` mode where policy violations don't result in content being blocked but instead send a report to a specified URI. This helps website administrators detect and respond to potential XSS attempts, allowing them to patch vulnerabilities and refine their CSP rules.
*   Plugin restrictions – Some XSS attacks might exploit browser plugins. With CSP, you can limit the types of plugins that can be invoked, further reducing potential attack vectors.

While input sanitization and secure coding practices are essential, CSP acts as a second line of defense, reducing the risk of [XSS exploits](/guides/understanding-xss-attacks).

Beyond XSS, CSP can prevent the unauthorized loading of content, protecting users from other threats like clickjacking and data injection.

## [Content Security Policy headers](#content-security-policy-headers)

```
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com; img-src 'self' img.example.com; style-src 'self';
```

This policy permits:

*   All content to be loaded only from the site's own origin.
*   Scripts to be loaded from the site's own origin and cdn.example.com.
*   Images from the site's own origin and img.example.com
*   Styles only from the site's origin.

## [Best Practices](#best-practices)

*   Before enforcing a CSP, start with the `Content-Security-Policy-Report-Only` header. You can do this to keep an eye on possible violations without actually blocking any content. Change to enforcing mode once you know your policy won't break any features.
*   Avoid using `unsafe-inline` and `unsafe-eval` . The use of `eval()` and inline scripts/styles can pose security risks. Avoid enabling these unless absolutely necessary as a best practice. Use nonces or hashes to allowlist particular scripts or styles if you need to allow inline scripts or styles.
*   Use nonces for inline scripts and styles. To allow that particular inline content, a nonce (number used once) can be added to a script or style tag, the CSP header, or both. This ensures that only the inline scripts and styles you have explicitly permitted will be used.
*   Be as detailed as you can, and avoid using too general sources like `.` . List the specific subdomains you want to allow rather than allowing all subdomains (`.domain.com`).
*   Keep directives updated. As your project evolves, the sources from which you load content might change. Ensure you update your CSP directives accordingly.

Keep in mind that while CSP is a robust security measure, it's part of a multi-layered security strategy. Input validation, output encoding, and other security practices remain crucial.

Additionally, while CSP is supported by modern browsers, nuances exist in their implementations. Ensure you test your policy across diverse browsers, accounting for variations and ensuring the same security postures.

--------------------------------------------------------------------------------
title: "Image Optimization with Vercel"
description: "Transform and optimize images to improve page load performance."
last_updated: "null"
source: "https://vercel.com/docs/image-optimization"
--------------------------------------------------------------------------------

# Image Optimization with Vercel

Copy page

Ask AI about this page

Last updated October 14, 2025

Image Optimization is available on [all plans](/docs/plans)

Vercel supports dynamically transforming unoptimized images to reduce the file size while maintaining high quality. These optimized images are cached on the [Vercel CDN](/docs/cdn), meaning they're available close to users whenever they're requested.

## [Get started](#get-started)

Image Optimization works with many frameworks, including Next.js, Astro, and Nuxt, enabling you to optimize images using built-in components.

*   Get started by following the [Image Optimization Quickstart](/docs/image-optimization/quickstart) and selecting your framework (Next.js, Nuxt, or Astro) from the dropdown.
*   For a live example which demonstrates usage with the [`next/image`](https://nextjs.org/docs/pages/api-reference/components/image) component, see the [Image Optimization demo](https://image-component.nextjs.gallery/).

## [Why should I optimize my images on Vercel?](#why-should-i-optimize-my-images-on-vercel)

Optimizing images on Vercel provides several advantages for your application:

*   Reduces the size of images and data transferred, enhancing website performance, user experience, and [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) usage.
*   Improving [Core Web Vitals](https://web.dev/vitals/), reduced bounce rates, and speeding up page loads.
*   Sizing images to support different devices and use modern formats like [WebP](https://developer.mozilla.org/docs/Web/Media/Formats/Image_types#webp_image) and [AVIF](https://developer.mozilla.org/docs/Web/Media/Formats/Image_types#avif_image).
*   Optimized images are cached after transformation, which allows them to be reused in subsequent requests.

## [How Image Optimization works](#how-image-optimization-works)

The flow of image optimization on Vercel involves several steps, starting from the image request to serving the optimized image.

1.  The optimization process starts with your component choice in your codebase:
    
    *   If you use a standard HTML `img` element, the browser will be instructed to bypass optimization and serve the image directly from its source.
    *   If you use a framework's `Image` component (like [`next/image`](https://nextjs.org/docs/app/api-reference/components/image)) it will use Vercel's image optimization pipeline, allowing your images to be automatically optimized and cached.
2.  When Next.js receives an image request, it checks the [`unoptimized`](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) prop on the `Image` component or the configuration in the [`next.config.ts`](https://nextjs.org/docs/app/api-reference/next-config-js) file to determine if optimization is disabled.
    
    *   If you set the `unoptimized` prop on the `Image` component to `true`, Next.js bypasses optimization and serves the image directly from its source.
    *   If you don't set the `unoptimized` prop or set it to `false`, Next.js checks the `next.config.ts` file to see if optimization is disabled. This configuration applies to all images and overrides the individual component prop.
    *   If neither the `unoptimized` prop is set nor optimization is disabled in the `next.config.ts` file, Next.js continues with the optimization process.
3.  If optimization is enabled, Vercel validates the [loader configuration](https://nextjs.org/docs/app/api-reference/components/image#loader) (whether using the default or a custom loader) and verifies that the image [source URL](https://nextjs.org/docs/app/api-reference/components/image#src) matches the allowed patterns defined in your configuration ([`remotePatterns`](/docs/image-optimization#setting-up-remote-patterns) or [`localPatterns`](/docs/image-optimization#setting-up-local-patterns)).
    
4.  Vercel then checks the status of the cache to see if an image has been previously cached:
    

*   `HIT`: The image is fetched and served from the cache, either in region or from the shared global cache.
    *   If fetched from the global cache, it's billed as an [image cache read](/docs/image-optimization/limits-and-pricing#image-cache-reads) which is reflected in your [usage metrics](https://vercel.com/docs/pricing/manage-and-optimize-usage#viewing-usage).
*   `MISS`: The image is fetched, transformed, cached, and then served to the user.
    *   Billed as an [image transformation](/docs/image-optimization/limits-and-pricing#image-transformations) and [image cache write](/docs/image-optimization/limits-and-pricing#image-cache-writes) which is reflected in your [usage metrics](https://vercel.com/docs/pricing/manage-and-optimize-usage#viewing-usage).
*   `STALE`: The image is fetched and served from the cache while revalidating in the background.
    *   Billed as an [image transformation](/docs/image-optimization/limits-and-pricing#image-transformations) and [image cache write](/docs/image-optimization/limits-and-pricing#image-cache-writes) which is reflected in your [usage metrics](https://vercel.com/docs/pricing/manage-and-optimize-usage#viewing-usage).

## [When to use Image Optimization](#when-to-use-image-optimization)

Image Optimization is ideal for:

*   Responsive layouts where images need to be optimized for different device sizes (e.g. mobile vs desktop)
*   Large, high-quality images (e.g. product photos, hero images)
*   User uploaded images
*   Content where images play a central role (e.g. photography portfolios)

In some cases, Image Optimization may not be necessary or beneficial, such as:

*   Small icons or thumbnails (under 10 KB)
*   Animated image formats such as GIFs
*   Vector image formats such as SVG
*   Frequently changing images where caching could lead to outdated content

If your images meet any of the above criteria where Image Optimization is not beneficial, we recommend using the [`unoptimized`](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) prop on the Next.js `Image` component. For guidance on [SvelteKit](https://svelte.dev/docs/kit/adapter-vercel#Image-Optimization), [Astro](https://docs.astro.build/en/guides/images/#authorizing-remote-images), or [Nuxt](https://image.nuxt.com/providers/vercel), see their documentation.

It's important that you are only optimizing images that need to be optimized otherwise you could end up using your [image usage](/docs/image-optimization/limits-and-pricing) quota unnecessarily. For example, if you have a small icon or thumbnail that is under 10 KB, you should not use Image Optimization as these images are already very small and optimizing them further would not provide any benefits.

## [Setting up remote or local patterns](#setting-up-remote-or-local-patterns)

An important aspect of using the `Image` component is properly setting up remote/local patterns in your `next.config.ts` file. This configuration determines which images are allowed to be optimized.

You can set up patterns for both [local images](#local-images) (stored as static assets in your `public` folder) and [remote images](#remote-images) (stored externally). In both cases you specify the pathname the images are located at.

### [Local images](#local-images)

A local image is imported from your file system and analyzed at build time. The import is added to the `src` prop: `src={myImage}`

#### [Setting up local patterns](#setting-up-local-patterns)

To set up local patterns, you need to specify the pathname of the images you want to optimize. This is done in the `next.config.ts` file:

next.config.ts

```
module.exports = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/images/**',
        search: '',
      },
    ],
  },
};
```

See the [Next.js documentation for local patterns](https://nextjs.org/docs/app/api-reference/components/image#localpatterns) for more information.

#### [Local images cache key](#local-images-cache-key)

The cache key for local images is based on the query string parameters, the `Accept` HTTP header, and the content hash of the image URL.

*   Cache Key:
    *   Project ID
    *   Query string parameters:
        *   `q`: The quality of the optimized image, between 1 (lowest quality) and 100 (highest quality).
        *   `w`: The width (in pixels) of the optimized image.
        *   `url`: The URL of the optimized image is keyed by content hash e.g. `/assets/me.png` is converted to `3399d02f49253deb9f5b5d1159292099`.
    *   `Accept` HTTP header (normalized).
*   Local image cache invalidation:
    *   Redeploying your app doesn't invalidate the image cache.
    *   To invalidate, replace the image of the same name with different content, then [redeploy](/docs/deployments/managing-deployments#redeploy-a-project).
*   Local image cache expiration:
    *   [Cached](/docs/edge-cache#static-files-caching) for up to 31 days on the Vercel CDN.

### [Remote images](#remote-images)

A remote image requires the `src` property to be a URL string, which can be relative or absolute.

#### [Setting up remote patterns](#setting-up-remote-patterns)

To set up remote patterns, you need to specify the `hostname` of the images you want to optimize. This is done in the `next.config.ts` file:

next.config.ts

```
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '/account123/**',
        search: '',
      },
    ],
  },
};
```

In the case of external images, you should consider adding your account id to the `pathname` if you don't own the `hostname`. For example `pathname: '/account123/v12h2bv/**'`. This helps protect your source images from potential abuse.

See the [Next.js documentation for remote patterns](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns) for more information.

#### [Remote images cache key](#remote-images-cache-key)

The cache key for remote images is based on the query string parameters, the `Accept` HTTP header, and the content hash of the image URL.

*   Cache Key:
    *   Project ID
    *   Query string parameters:
        *   `q`: The quality of the optimized image, between 1 (lowest quality) and 100 (highest quality).
        *   `w`: The width (in pixels) of the optimized image.
        *   `url`: The URL of the optimized image e.g. [https://example.com/assets/me.png](https://example.com/assets/me.png).
    *   `Accept` HTTP header (normalized).
*   Remote image cache invalidation:
    *   Redeploying your app doesn't invalidate the image cache
    *   To invalidate, add a query string to the `src` property (e.g., `?v=2`), then [redeploy](/docs/deployments/managing-deployments#redeploy-a-project).
    *   Alternatively, you can configure the cache to expire more frequently.
*   Remote image cache expiration:
    *   TTL is determined by the [`Cache-Control`](/docs/headers#cache-control-header) `max-age` header from the upstream image or [`minimumCacheTTL`](https://nextjs.org/docs/api-reference/next/image#minimum-cache-ttl) config (default: `3600` seconds), whichever is larger.
    *   If your image content changes frequently, it's best to keep this TTL short.

Once an image is cached, it remains so even if you update the source image. For remote images, users accessing a URL with a previously cached image will see the old version until the cache expires or the image is invalidated. Each time an image is requested, it counts towards your [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) and [Edge Request](/docs/manage-cdn-usage#edge-requests) usage for your billing cycle.

See [Pricing](/docs/image-optimization/limits-and-pricing) for more information, and read more about [caching behavior](https://nextjs.org/docs/app/api-reference/components/image#caching-behavior) in the Next.js documentation.

## [Image Transformation URL format](#image-transformation-url-format)

When you use the `Image` component in common frameworks and deploy your project on Vercel, Image Optimization automatically adjusts your images for different device screen sizes. The `src` prop you provided in your code is dynamically replaced with an optimized image URL. For example:

*   Next.js: `/_next/image?url={link/to/src/image}&w=3840&q=75`
*   Nuxt, Astro, etc: `/_vercel/image?url={link/to/src/image}&w=3840&q=75`

The Image Optimization API has the following query parameters:

*   `url`: The URL of the source image to be transformed. This can be a local image (relative url) or remote image (absolute url).
*   `w`: The width of the transformed image in pixels. No height is needed since the source image aspect ratio is preserved.
*   `q`: The quality of the transformed image, between 1 (lowest quality) and 100 (highest quality).

The allowed values of those query parameters are determined by the framework you are using, such as `next.config.js` for Next.js.

If you are not using a framework that comes with an `Image` component or you are building your own framework, refer to the [Build Output API](/docs/build-output-api/configuration#images) to see how the build output from a framework can configure the Image Optimization API.

## [Opt-in](#opt-in)

To switch to the transformation images-based pricing plan:

1.  Choose your team scope on the dashboard, and go to Settings, then Billing
2.  Scroll down to the Image Optimization section
3.  Select Review Cost Estimate. Proceed to enable this option in the dialog that shows the cost estimate.

[View your estimate](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fsettings%2Fbilling%23image-optimization-new-price&title=Go+to+Billing+Settings)

## [Related](#related)

For more information on what to do next, we recommend the following articles:

*   [Image Optimization quickstart](/docs/image-optimization/quickstart)
*   [Managing costs](/docs/image-optimization/managing-image-optimization-costs)
*   [Pricing](/docs/image-optimization/limits-and-pricing)
*   If you are building a custom web framework, you can also use the [Build Output API](/docs/build-output-api/v3/configuration#images) to implement Image Optimization. To learn how to do this, see the [Build your own web framework](/blog/build-your-own-web-framework#automatic-image-optimization) blog post.

--------------------------------------------------------------------------------
title: "Legacy Pricing for Image Optimization"
description: "This page outlines information on the pricing and limits for the source images-based legacy option."
last_updated: "null"
source: "https://vercel.com/docs/image-optimization/legacy-pricing"
--------------------------------------------------------------------------------

# Legacy Pricing for Image Optimization

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Pricing](#pricing)

This legacy pricing option is only available to Pro and Enterprise teams created before February 18th, 2025, who are given the choice to [opt-in](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fsettings%2Fbilling%23image-optimization-new-price&title=Go+to+Billing+Settings) to the [transformation images-based pricing plan](/docs/image-optimization/limits-and-pricing) or stay on this legacy source images-based pricing plan. Upgrading or downgrading your plan will automatically opt-in your team.

Image Optimization pricing is dependent on your plan and how many unique [source images](#source-images) you have across your projects during your billing period.

| Resource | Hobby Included | Pro Included | Pro Additional |
| --- | --- | --- | --- |
| [Image Optimization Source Images](#source-images) | First 1,000 | First 5,000 | $5.00 per 1,000 Images |

## [Usage](#usage)

The table below shows the metrics for the Image Optimization section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Source images](/docs/image-optimization/managing-image-optimization-costs#source-image-optimizations) | The number of images that have been optimized using the Image Optimization feature | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/image-optimization/managing-image-optimization-costs#how-to-optimize-your-costs) |

Usage is not incurred until an image is requested.

### [Source Images](#source-images)

A source image is the value that is passed to the `src` prop. A single source image can produce multiple optimized images. For example:

*   Usage: `<Image src="/hero.png" width="700" height="745" />`
*   Source image: `/hero.png`
*   Optimized image: `/_next/image?url=%2Fhero.png&w=750&q=75`
*   Optimized image: `/_next/image?url=%2Fhero.png&w=828&q=75`
*   Optimized image: `/_next/image?url=%2Fhero.png&w=1080&q=75`

For example, if you are on a Pro plan and have passed 6000 source images to the `src` prop within the last billing cycle, your bill will be $5 for image optimization.

## [Billing](#billing)

You are billed for the number of unique [source images](#source-images) requested during the billing period.

Additionally, charges apply for [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) when optimized images are delivered from Vercel's [CDN](/docs/cdn) to clients.

### [Hobby](#hobby)

Image Optimization is free for Hobby users within the [usage limits](/docs/limits/fair-use-guidelines#typical-monthly-usage-guidelines). As stated in the [Fair Usage Policy](/docs/limits/fair-use-guidelines#commercial-usage), Hobby teams are restricted to non-commercial personal use only.

Vercel will send you emails as you are nearing your [usage](#pricing) limits, but you will also be advised of any alerts within the [dashboard](/dashboard).

Once you exceed the limits:

*   New [source images](#source-images) will fail to optimize and instead return a runtime error response with [402 status code](/docs/errors/platform-error-codes#402:-deployment_disabled). This will trigger the [`onError`](https://nextjs.org/docs/app/api-reference/components/image#onerror) callback and show the [`alt`](https://nextjs.org/docs/app/api-reference/components/image#alt) text instead of the image
*   Previously optimized images have already been cached and will continue to work as expected, without error

You will not be charged for exceeding the usage limits, but this usually means your application is ready to upgrade to a [Pro plan](/docs/plans/pro).

### Experience Vercel Pro for free

Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.

[Start your free Pro trial](/upgrade/docs-trial-button)

If you want to continue using Hobby, read more about [Managing Usage & Costs](/docs/image-optimization/managing-image-optimization-costs) to see how you can disable Image Optimization per image or per project.

### [Pro and Enterprise](#pro-and-enterprise)

For Teams on Pro trials, the [trial will end](/docs/plans/pro-plan/trials#post-trial-decision) if your Team uses over 2500 source images. For more information, see the [trial limits](/docs/plans/pro-plan/trials#trial-limitations).

Vercel will send you emails as you are nearing your [usage](#pricing) limits, but you will also be advised of any alerts within the [dashboard](/dashboard). Once your team exceeds the 5000 source images limit, you will continue to be charged $5 per 1000 source images for on-demand usage.

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

## [Limits](#limits)

For all the images that are optimized by Vercel, the following limits apply:

*   The maximum size for an optimized image is 10 MB, as set out in the [Cacheable Responses limits](/docs/edge-cache#how-to-cache-responses)
*   Each [source image](#source-images) has a maximum width and height of 8192 pixels
*   A [source image](#source-images) must be one of the following formats to be optimized: `image/jpeg`, `image/png`, `image/webp`, `image/avif`. Other formats will be served as-is

See the [Fair Usage Policy](/docs/limits/fair-use-guidelines#typical-monthly-usage-guidelines) for typical monthly usage guidelines.

--------------------------------------------------------------------------------
title: "Limits and Pricing for Image Optimization"
description: "This page outlines information on the limits that are applicable when using Image Optimization, and the costs they can incur."
last_updated: "null"
source: "https://vercel.com/docs/image-optimization/limits-and-pricing"
--------------------------------------------------------------------------------

# Limits and Pricing for Image Optimization

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Pricing](#pricing)

This is the default pricing option. For Pro and Enterprise teams created before February 18th, 2025, you will be given the choice to [opt-in](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fsettings%2Fbilling%23image-optimization-new-price&title=Go+to+Billing+Settings) to this pricing plan or stay on the [legacy source images-based](/docs/image-optimization/legacy-pricing) pricing plan. Upgrading or downgrading your plan will automatically opt-in your team.

Image optimization pricing is dependent on your plan and on specific parameters outlined in the table below. For detailed pricing information for each region, review [Regional Pricing](/docs/pricing/regional-pricing#specific-region-pricing).

| Image Usage | Hobby Included | On-demand Rates |
| --- | --- | --- |
| [Image transformations](#image-transformations) | 5K/month | [$0.05 - $0.0812 per 1K](/docs/pricing/regional-pricing#specific-region-pricing) |
| [Image cache reads](#image-cache-reads) | 300K/month | [$0.40 - $0.64 per 1M](/docs/pricing/regional-pricing#specific-region-pricing) |
| [Image cache writes](#image-cache-writes) | 100K/month | [$4.00 - $6.40 per 1M](/docs/pricing/regional-pricing#specific-region-pricing) |

This ensures that you only pay for the optimizations when the images are used instead of the number of images in your project.

## [Image transformations](#image-transformations)

Image transformations are billed for every cache MISS and STALE. The cache key is based on several inputs and differs for [local images cache key](/docs/image-optimization#local-images-cache-key) vs the [remote images cache key](/docs/image-optimization#remote-images-cache-key).

## [Image cache reads](#image-cache-reads)

The total amount of Read Units used to access the cached image from the global cache, measured in 8KB units.

It is _not_ billed for every cache HIT, only when the image needs to be retrieved from the shared global cache.

An image that has been accessed recently (several hours ago) in the same region will be cached in region and does _not_ incur this cost.

## [Image cache writes](#image-cache-writes)

The total amount of Write Units used to store the cached image in the global cache, measured in 8KB units. It is billed for every cache MISS and STALE.

## [Billing](#billing)

You are billed for the number of [Image Transformations](#image-transformations), [Image Cache Reads](#image-cache-reads), and [Image Cache Writes](#image-cache-writes) during the billing period.

Additionally, charges apply for [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) and [Edge Requests](/docs/manage-cdn-usage#edge-requests) when transformed images are delivered from Vercel's [CDN](/docs/cdn) to clients.

### [Hobby](#hobby)

Image Optimization is free for Hobby users within the [usage limits](/docs/limits/fair-use-guidelines#typical-monthly-usage-guidelines). As stated in the [Fair Usage Policy](/docs/limits/fair-use-guidelines#commercial-usage), Hobby teams are restricted to non-commercial personal use only.

Vercel will send you emails as you are nearing your [usage](#pricing) limits, but you will also be advised of any alerts within the [dashboard](/dashboard).

Once you exceed the limits:

*   New images will fail to optimize and instead return a runtime error response with [402 status code](/docs/errors/platform-error-codes#402:-deployment_disabled). This will trigger the [`onError`](https://nextjs.org/docs/app/api-reference/components/image#onerror) callback and show the [`alt`](https://nextjs.org/docs/app/api-reference/components/image#alt) text instead of the image
*   Previously optimized images have already been cached and will continue to work as expected, without error

You will not be charged for exceeding the usage limits, but this usually means your application is ready to upgrade to a [Pro plan](/docs/plans/pro).

If you want to continue using Hobby, read more about [Managing Usage & Costs](/docs/image-optimization/managing-image-optimization-costs) to see how you can disable Image Optimization per image or per project.

### [Pro and Enterprise](#pro-and-enterprise)

Vercel will send you emails as you are nearing your [usage](#pricing) limits, but you will also be advised of any alerts within the [dashboard](/dashboard).

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

## [Limits](#limits)

For all the images that are [optimized by Vercel](/docs/image-optimization/managing-image-optimization-costs#measuring-usage), the following limits apply:

*   The maximum size for an transformed image is 10 MB, as set out in the [Cacheable Responses limits](/docs/edge-cache#how-to-cache-responses)
*   Each source image has a maximum width and height of 8192 pixels
*   A source image must be one of the following formats to be optimized: `image/jpeg`, `image/png`, `image/webp`, `image/avif`. Other formats will be served as-is

See the [Fair Usage Policy](/docs/limits/fair-use-guidelines#typical-monthly-usage-guidelines) for typical monthly usage guidelines.

--------------------------------------------------------------------------------
title: "Managing Usage & Costs"
description: "Learn how to measure and manage Image Optimization usage with this guide to avoid any unexpected costs."
last_updated: "null"
source: "https://vercel.com/docs/image-optimization/managing-image-optimization-costs"
--------------------------------------------------------------------------------

# Managing Usage & Costs

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Measuring usage](#measuring-usage)

This document describes usage for the default pricing option. For Pro and Enterprise teams created before February 18th, 2025 you will be given the choice to [opt-in](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fsettings%2Fbilling%23image-optimization-new-price&title=Go+to+Billing+Settings) to this pricing plan or stay on the [legacy source images-based](/docs/image-optimization/legacy-pricing) pricing plan.

Your Image Optimization usage over time is displayed under the Image Optimization section of the [Usage](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fusage%23image-optimization-image-transformations&title=Go%20to%20Usage) tab on your dashboard.

You can also view detailed information in the Image Optimization section of the [Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fobservability%2Fimage-optimization&title=Go%20to%20Observability) tab on your dashboard.

## [Reducing usage](#reducing-usage)

To help you minimize Image Optimization usage costs, consider implementing the following suggestions:

*   Cache Max Age: If your images do not change in less than a month, set `max-age=2678400` (31 days) in the `Cache-Control` header or set [`images.minimumCacheTTL`](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl) to `minimumCacheTTL:2678400` to reduce the number of transformations and cache writes. Using static imports can also help as they set the `Cache-Control` header to 1 year.
    
*   Formats: Check if your Next.js configuration is using [`images.formats`](https://nextjs.org/docs/app/api-reference/components/image#formats) with multiple values and consider removing one. For example, change `['image/avif', 'image/web']` to `['image/webp']` to reduce the number of transformations.
    
*   Remote and local patterns: Configure [`images.remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns) and [`images.localPatterns`](https://nextjs.org/docs/app/api-reference/components/image#localpatterns) allowlist which images should be optimized so that you can limit unnecessary transformations and cache writes.
    
*   Qualities: Configure the [`images.qualities`](https://nextjs.org/docs/app/api-reference/components/image#qualities) allowlist to reduce possible transformations. Lowering the quality will make the transformed image smaller resulting in fewer cache reads, cache writes, and fast data transfer.
    
*   Image sizes: Configure the [`images.imageSizes`](https://nextjs.org/docs/app/api-reference/components/image#imagesizes) and [`images.deviceSizes`](https://nextjs.org/docs/app/api-reference/components/image#devicesizes) allowlists to match your audience and reduce the number of transformations and cache writes.
    
*   Unoptimized: For source images that do not benefit from optimization such as small images (under 10 KB), vector images (SVG) and animated images (GIF), use the [`unoptimized` property](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) on the Image component to avoid transformations, cache reads, and cache writes. Use sparingly since `unoptimized` on every image could increase fast data transfer cost.

--------------------------------------------------------------------------------
title: "Getting started with Image Optimization"
description: "Learn how you can leverage Vercel Image Optimization in your projects."
last_updated: "null"
source: "https://vercel.com/docs/image-optimization/quickstart"
--------------------------------------------------------------------------------

# Getting started with Image Optimization

Copy page

Ask AI about this page

Last updated October 14, 2025

This guide will help you get started with using Vercel Image Optimization in your project, showing you how to import images, add the required props, and deploy your app to Vercel. Vercel Image Optimization works out of the box with Next.js, Nuxt, SvelteKit, and Astro.

## [Prerequisites](#prerequisites)

*   A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
*   A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
*   The Vercel CLI installed. If you don't have it, you can install it using the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel
    ```
    

1.  ### [Import images](#import-images)
    
    Next.js provides a built-in [`next/image`](https://nextjs.org/docs/app/api-reference/components/image) component.
    
    app/example/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import Image from 'next/image';
    ```
    
2.  ### [Add the required props](#add-the-required-props)
    
    This component takes the following [required props](https://nextjs.org/docs/app/api-reference/components/image#required-props):
    
    *   `src`: The URL of the image
    *   `alt`: A short description of the image
    *   `width`: The width of the image
    *   `height`: The height of the image
    
    When using [local images](https://nextjs.org/docs/app/building-your-application/optimizing/images#local-images) you do not need to provide the `width` and `height` props. These values will be automatically determined based on the imported image.
    
    The example below uses a [remote image](https://nextjs.org/docs/app/building-your-application/optimizing/images#remote-images) with the `width` and `height` props applied:
    
    app/example/page.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    <Image
      src="https://images.unsplash.com/photo-1627843240167-b1f9d28f732e"
      alt="Triangular frames arranged concentrically, creating a tunnel against a dark background."
      width={1920}
      height={1080}
    />
    ```
    
    If there are some images that you wish to not optimize (for example, if the URL contains a token), you can use the [unoptimized](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) prop to disable image optimization on some or all of your images.
    
    For more information on all props, caching behavior, and responsive images, visit the [`next/image`](https://nextjs.org/docs/app/api-reference/components/image) documentation.
    
3.  ### [Deploy your app to Vercel](#deploy-your-app-to-vercel)
    
    Push your changes and deploy your Next.js application to Vercel.
    
    When deployed to Vercel, this component automatically optimizes your images on-demand and serves them from the [Vercel CDN](/docs/cdn).
    

## [Next steps](#next-steps)

Now that you've set up Vercel Image Optimization, you can explore the following:

*   [Explore limits and pricing](/docs/image-optimization/limits-and-pricing)
*   [Managing costs](/docs/image-optimization/managing-image-optimization-costs)

--------------------------------------------------------------------------------
title: "Incremental Migration to Vercel"
description: "Learn how to migrate your app or website to Vercel with minimal risk and high impact."
last_updated: "null"
source: "https://vercel.com/docs/incremental-migration"
--------------------------------------------------------------------------------

# Incremental Migration to Vercel

Copy page

Ask AI about this page

Last updated September 15, 2025

When migrating to Vercel you should use an incremental migration strategy. This allows your current site and your new site to operate simultaneously, enabling you to move different sections of your site at a pace that suits you.

In this guide, we'll explore incremental migration benefits, strategies, and implementation approaches for a zero-downtime migration to Vercel.

## [Why opt for incremental migration?](#why-opt-for-incremental-migration)

Incremental migrations offer several advantages:

*   Reduced risk due to smaller migration steps
*   A smoother rollback path in case of unexpected issues
*   Earlier technical implementation and business value validation
*   Downtime-free migration without maintenance windows

### [Disadvantages of one-time migrations](#disadvantages-of-one-time-migrations)

One-time migration involves developing the new site separately before switching traffic over. This approach has certain drawbacks:

*   Late discovery of expensive product issues
*   Difficulty in assessing migration success upfront
*   Potential for reaching a point of no-return, even with major problem detection
*   Possible business loss due to legacy system downtime during migration

### [When to use incremental migration?](#when-to-use-incremental-migration)

Despite requiring more effort to make the new and legacy sites work concurrently, incremental migration is beneficial if:

*   Risk reduction and time-saving benefits outweigh the effort
*   The extra effort needed for specific increments to interact with legacy data doesn't exceed the time saved

## [Incremental migration strategies](#incremental-migration-strategies)

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fincremental-migration-steps-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fincremental-migration-steps-dark.png&w=3840&q=75)

Incremental migration process

With incremental migration, legacy and new systems operate simultaneously. Depending on your strategy, you'll select a system aspect, like a feature or user group, to migrate incrementally.

### [Vertical migration](#vertical-migration)

This strategy targets system features with the following process:

1.  Identify all legacy system features
2.  Choose key features for the initial migration
3.  Repeat until all features have been migrated

Throughout, both systems operate in parallel with migrated features routed to the new system.

### [Horizontal migration](#horizontal-migration)

This strategy focuses on system users with the following process:

1.  Identify all user groups
2.  Select a user group for initial migration to the new system
3.  Repeat until all users have been migrated

During migration, a subset of users accesses the new system while others continue using the legacy system.

### [Hybrid migration](#hybrid-migration)

A blend of vertical and horizontal strategies. For each feature subset, migrate by user group before moving to the next feature subset.

## [Implementation approaches](#implementation-approaches)

Follow these steps to incrementally migrate your website to Vercel. Two possible strategies can be applied:

1.  [Point your domain to Vercel from the beginning](#point-your-domain-to-vercel)
2.  [Keep your domain on the legacy server](#keep-your-domain-on-the-legacy-server)

## [Point your domain to Vercel](#point-your-domain-to-vercel)

In this approach, you make Vercel [the entry point for all your production traffic](/docs/domains/add-a-domain). When you begin, all traffic will be sent to the legacy server with [rewrites](/docs/rewrites) and/or fallbacks. As you migrate different aspects of your site to Vercel, you can remove the rewrites/fallbacks to the migrated paths so that they are now served by Vercel.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fapproach-1-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fapproach-1-dark.png&w=3840&q=75)

Point your domain to Vercel approach

### [1\. Deploy your application](#1.-deploy-your-application)

Use the [framework](/docs/frameworks) of your choice to deploy your application to Vercel

### [2\. Re-route the traffic](#2.-re-route-the-traffic)

Send all traffic to the legacy server using one of the following 3 methods:

#### [Framework-specific rewrites](#framework-specific-rewrites)

Use rewrites [built-in to the framework](/docs/rewrites#framework-considerations) such as configuring `next.config.ts` with [fallbacks and rewrites in Next.js](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites)

The code example below shows how to configure rewrites with fallback using `next.config.js` to send all traffic to the legacy server:

next.config.ts

```
import type { NextConfig } from 'next';
 
const nextConfig: NextConfig = {
  async rewrites() {
    return {
      fallback: [
        {
          source: '/:path*',
          destination: 'https://my-legacy-site.com/:path*',
        },
      ],
    };
  },
};
 
export default nextConfig;
```

#### [Vercel configuration rewrites](#vercel-configuration-rewrites)

Use `vercel.json` for frameworks that do not have rewrite support. See the [how do rewrites work](/docs/rewrites) documentation to learn how to rewrite to an external destination, from a specific path.

#### [Edge Config](#edge-config)

Use [Edge Config](/docs/edge-config) with [Routing Middleware](/docs/routing-middleware) to rewrite requests at the edge with the following benefits:

*   No need to re-deploy your application when rewrite changes are required
*   Immediately switch back to the legacy server if the new feature implementation is broken

Review this [maintenance page example](https://vercel.com/templates/next.js/maintenance-page) to understand the mechanics of this approach

This is an example middleware code for executing the rewrites at the edge:

middleware.ts

```
import { get } from '@vercel/edge-config';
import { NextRequest, NextResponse } from 'next/server';
 
export const config = {
  matcher: '/((?!api|_next/static|favicon.ico).*)',
};
 
export default async function middleware(request: NextRequest) {
  const url = request.nextUrl;
  const rewrites = await get('rewrites'); // Get rewrites stored in Edge Config
 
  for (const rewrite of rewrites) {
    if (rewrite.source === url.pathname) {
      url.pathname = rewrite.destination;
      return NextResponse.rewrite(url);
    }
  }
 
  return NextResponse.next();
}
```

In the above example, you use Edge Config to store one key-value pair for each rewrite. In this case, you should consider [Edge Config Limits](/docs/edge-config/edge-config-limits) (For example, 5000 routes would require around 512KB of storage). You can also rewrite based on [URLPatterns](https://developer.mozilla.org/docs/Web/API/URLPattern) where you would store each URLPattern as a key-value pair in Edge Config and not require one pair for each route.

### [3\. Deploy to production](#3.-deploy-to-production)

Connect your [production domain](/docs/getting-started-with-vercel/domains) to your Vercel Project. All your traffic will now be sent to the legacy server.

### [4\. Deploy your first iteration](#4.-deploy-your-first-iteration)

Develop and test the first iteration of your application on Vercel on specific paths.

With the fallback approach such as with the `next.config.js` example above, Next.js will automatically serve content from your Vercel project as you add new paths to your application. You will therefore not need to make any rewrite configuration changes as you iterate. For specific rewrite rules, you will need to remove/update them as you iterate.

Repeat this process until all the paths are migrated to Vercel and all rewrites are removed.

## [Keep your domain on the legacy server](#keep-your-domain-on-the-legacy-server)

In this approach, once you have tested a specific feature on your new Vercel application, you configure your legacy server or proxy to send the traffic on that path to the path on the Vercel deployment where the feature is deployed.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fapproach-2-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fapproach-2-dark.png&w=3840&q=75)

Keep your domain on the legacy server approach

### [1\. Deploy your first feature](#1.-deploy-your-first-feature)

Use the [framework](/docs/frameworks) of your choice to deploy your application on Vercel and build the first feature that you would like to migrate.

### [2\. Add a rewrite or reverse proxy](#2.-add-a-rewrite-or-reverse-proxy)

Once you have tested the first feature fully on Vercel, add a rewrite or reverse proxy to your existing server to send the traffic on the path for that feature to the Vercel deployment.

For example, if you are using [nginx](https://nginx.org/), you can use the [`proxy_pass`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass) directive to send the traffic to the Vercel deployment.

Let's say you deployed the new feature at the folder `new-feature` of the new Next.js application and set its [`basePath`](https://nextjs.org/docs/app/api-reference/next-config-js/basePath) to `/new-feature`, as shown below:

next.config.ts

```
import type { NextConfig } from 'next';
 
const nextConfig: NextConfig = {
  basePath: '/new-feature',
};
 
export default nextConfig;
```

When deployed, your new feature will be available at `https://my-new-app.vercel.app/`.

You can then use the following nginx configuration to send the traffic for that feature from the legacy server to the new implementation:

nginx.conf

```
server {
    listen 80;
    server_name legacy-server.com www.legacy-server.com;
 
    location /feature-path-on-legacy-server {
        proxy_pass https://my-new-app.vercel.app/;
    }
}
```

Repeat steps 1 and 2 until all the features have been migrated to Vercel. You can then point your domain to Vercel and remove the legacy server.

## [Troubleshooting](#troubleshooting)

### [Maximum number of routes](#maximum-number-of-routes)

Vercel has a limit of 1024 routes per deployment for rewrites. If you have more than 1024 routes, you may want to consider creating a custom solution using Middleware. For more information on how to do this in Next.js, see [Managing redirects at scale](https://nextjs.org/docs/app/building-your-application/routing/redirecting#managing-redirects-at-scale-advanced).

### [Handling emergencies](#handling-emergencies)

If you're facing unexpected outcomes or cannot find an immediate solution for an unexpected behavior with a new feature, you can set up a variable in [Edge Config](/docs/edge-config) that you can turn on and off at any time without having to make any code changes on your deployment. The value of this variable will determine whether you rewrite to the new version or the legacy server.

For example, with Next.js, you can use the follow [middleware](/docs/edge-middleware) code example:

middleware.ts

```
import { NextRequest, NextResponse } from 'next/server';
import { get } from '@vercel/edge-config';
 
export const config = {
  matcher: ['/'], // URL to match
};
 
export async function middleware(request: NextRequest) {
  try {
    // Check whether the new version should be shown - isNewVersionActive is a boolean value stored in Edge Config that you can update from your Project dashboard without any code changes
    const isNewVersionActive = await get<boolean>('isNewVersionActive');
 
    // If `isNewVersionActive` is false, rewrite to the legacy server URL
    if (!isNewVersionActive) {
      req.nextUrl.pathname = `/legacy-path`;
      return NextResponse.rewrite(req.nextUrl);
    }
  } catch (error) {
    console.error(error);
  }
}
```

[Create an Edge Config](/docs/edge-config/edge-config-dashboard#creating-an-edge-config) and set it to `{ "isNewVersionActive": true }`. By default, the new feature is active since `isNewVersionActive` is `true`. If you experience any issues, you can fallback to the legacy server by setting `isNewVersionActive` to `false` in the Edge Config from your Vercel dashboard.

## [Session management](#session-management)

When your application is hosted across multiple servers, maintaining [session](https://developer.mozilla.org/docs/Web/HTTP/Session) information consistency can be challenging.

For example, if your legacy application is served on a different domain than your new application, the HTTP session cookies will not be shared between the two. If the data that you need to share is not easily calculable and derivable, you will need a central session store as in the use cases below:

*   Using cookies for storing user specific data such as last login time and recent viewed items
*   Using cookies for tracking the number of items added to the cart

If you are not currently using a central session store for persisting sessions or are considering moving to one, you can use [Vercel KV](/docs/storage/vercel-kv).

Learn more about creating a session store and managing session data in our [quickstart guide](/docs/storage/vercel-kv/quickstart).

## [User group strategies](#user-group-strategies)

Minimize risk and perform A/B testing by combining your migration by feature with a user group strategy. You can use [Edge Config](/docs/edge-config) to store user group information and [Routing Middleware](/docs/routing-middleware) to direct traffic appropriately.

*   Review our [Edge Config feature flag template](https://vercel.com/templates/next.js/feature-flag-apple-store) for a deeper understanding of this approach
*   You can also consult our [guide on A/B Testing on Vercel](https://vercel.com/guides/ab-testing-on-vercel) for implementing this strategy

## [Using functions](#using-functions)

Consider using [Vercel Functions](/docs/functions) as you migrate your application.

This allows for the implementation of small, specific, and independent functionality units triggered by events, potentially enhancing future performance and reducing the risk of breaking changes. However, it may require refactoring your existing code to be more modular and reusable.

## [SEO considerations](#seo-considerations)

Prevent the loss of indexed pages, links, and duplicate content when creating rewrites to direct part of your traffic to the new Vercel deployment. Consider the following:

*   Write E2E tests to ensure correct setting of canonical tags and robot indexing at each migration step
*   Account for existing redirects and rewrites on your legacy server, ensuring they are thoroughly tested during migration
*   Maintain the same routes for migrated feature(s) on Vercel

--------------------------------------------------------------------------------
title: "Incremental Static Regeneration (ISR)"
description: "Learn how Vercel's Incremental Static Regeneration (ISR) provides better performance and faster builds."
last_updated: "null"
source: "https://vercel.com/docs/incremental-static-regeneration"
--------------------------------------------------------------------------------

# Incremental Static Regeneration (ISR)

Copy page

Ask AI about this page

Last updated September 9, 2025

Incremental Static Regeneration is available on [all plans](/docs/plans)

Incremental Static Regeneration (ISR) allows you to create or update content on your site without redeploying. ISR's main benefits for developers include:

1.  Better Performance: Static pages can be consistently fast because ISR allows Vercel to cache generated pages in every region on [our global CDN](/docs/cdn) and persist files into durable storage
2.  Reduced Backend Load: ISR helps reduce backend load by using cached content to make fewer requests to your data sources
3.  Faster Builds: Pages can be generated when requested by a visitor or through an API instead of during the build, speeding up build times as your application grows

ISR is available to applications built with:

*   [Next.js](#using-isr-with-next.js)
*   [SvelteKit](/docs/frameworks/sveltekit#incremental-static-regeneration-isr)
*   [Nuxt](/docs/frameworks/nuxt#incremental-static-regeneration-isr)
*   [Astro](/docs/frameworks/astro#incremental-static-regeneration)
*   [Gatsby](/docs/frameworks/gatsby#incremental-static-regeneration)
*   Or any custom framework solution that implements the [Build Output API](/docs/build-output-api/v3)

### Interested in the Enterprise plan?

Contact our sales team to learn more about the Enterprise plan and how it can benefit your team.

[Contact Sales](/contact/sales)

## [Using ISR with Next.js](#using-isr-with-next.js)

Next.js will automatically create a Serverless Vercel Function that can revalidate when you add `next: { revalidate: 10 }` to the options object passed to a `fetch` request.

The following example demonstrates a Next.js page that uses ISR to render a list of blog posts:

Next.js (/app)Next.js (/pages)

app/blog-posts/page.tsx

TypeScript

TypeScriptJavaScript

```
export const revalidate = 10; // seconds
 
interface Post {
  title: string;
  id: number;
}
 
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog');
  const posts = (await res.json()) as Post[];
  return (
    <ul>
      {posts.map((post: Post) => {
        return <li key={post.id}>{post.title}</li>;
      })}
    </ul>
  );
}
```

To learn more about using ISR with Next.js in the App router, such as enabling on-demand revalidation, see [the official Next.js documentation](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration).

## [Using ISR with SvelteKit or Nuxt](#using-isr-with-sveltekit-or-nuxt)

*   See [our dedicated SvelteKit docs](/docs/frameworks/sveltekit#incremental-static-regeneration-isr) to learn how to use ISR with your SvelteKit projects on Vercel
*   See [our dedicated Nuxt docs](/docs/frameworks/nuxt#incremental-static-regeneration-isr) to use ISR with Nuxt

## [Using ISR with the Build Output API](#using-isr-with-the-build-output-api)

When using the Build Output API, the Serverless Vercel Functions generated for your ISR routes are called [Prerender Functions](/docs/build-output-api/v3#vercel-primitives/prerender-functions).

Build Output API Prerender Functions are [Vercel functions](/docs/functions) with accompanying JSON files that describe the Function's cache invalidation rules. See [our Prerender configuration file docs](/docs/build-output-api/v3/primitives#prerender-configuration-file) to learn more.

## [Differences between ISR and `Cache-Control` headers](#differences-between-isr-and-cache-control-headers)

Both ISR and `Cache-Control` headers help reduce backend load by using cached content to make fewer requests to your data source. However, there are key architectural differences between the two.

*   Shared Global Cache: ISR has cache shielding built-in automatically, which helps improve the cache `HIT` ratio. The cache for your ISR route's Vercel Function output is distributed globally. In the case of a cache `MISS`, it looks up the value in a single, global bucket. With only [`cache-control` headers](/docs/edge-cache), caches expire (by design) and are not shared across [regions](/docs/regions)
*   300ms Global Purges: When revalidating (either on-demand or in the background), your ISR route's Vercel Function is re-run, and the cache is brought up to date with the newest content within 300ms in all regions globally
*   Instant Rollbacks: ISR allows you to roll back instantly and not lose your previously generated pages by persisting them between deployments
*   Simplified Caching Experience: ISR abstracts common issues with HTTP-based caching implementations, adds additional features for availability and global performance, and provides a better developer experience for implementation

See [our Cache control options docs](/docs/edge-cache#cache-control-options) to learn more about `Cache-Control` headers.

### [ISR vs `Cache-Control` comparison table](#isr-vs-cache-control-comparison-table)

ISR vs Cache-Control comparison table
| 
Feature

 | 

ISR

 | 

Caching Headers

 |
| --- | --- | --- |
| On-demand purging & regeneration | 

 | 

Limited

 |
| Synchronized global purging | 

 | 

Limited

 |
| 

Support for fallbacks upon `MISS`

 | 

 | 

N/A

 |
| Durable storage | 

 | 

N/A

 |
| Atomic updates | 

 | 

N/A

 |
| Cache shielding | 

 | 

N/A

 |
| Slow origin protection | 

 | 

Limited

 |
| 

Automatic support for `stale-if-error`

 | 

 | 

Limited

 |
| 

Automatic support for `stale-while-revalidate`

 | 

 | 

 |
| Usage within popular frontend frameworks | 

 | 

 |
| Caching static page responses | 

 | 

 |

## [On-demand revalidation limits](#on-demand-revalidation-limits)

On-demand revalidation is scoped to the domain and deployment where it occurs, and doesn't affect sub domains or other deployments.

For example, if you trigger on-demand revalidation for `example-domain.com/example-page`, it won't revalidate the same page served by sub domains on the same deployment, such as `sub.example-domain.com/example-page`.

See [Revalidating across domains](/docs/edge-cache#revalidating-across-domains) to learn how to get around this limitation.

## [ISR pricing](#isr-pricing)

When using ISR with a framework on Vercel, a function is created based on your framework code. This means that you incur usage when the ISR [function](/docs/pricing/serverless-functions) is invoked, when [ISR reads and writes](/docs/pricing/incremental-static-regeneration) occur, and on the [Fast Origin Transfer](/docs/manage-cdn-usage#fast-origin-transfer):

*   You incur usage when the function is invoked – ISR functions are invoked whenever they revalidate in the background or through [on-demand revalidation](/docs/incremental-static-regeneration/quickstart#on-demand-revalidation)
*   You incur ISR writes when new content is stored in the ISR cache – Fresh content returned by ISR functions is persisted to durable storage for the duration you specify, until it goes unaccessed for 31 days
*   You incur Incur ISR reads when content is accessed from the ISR cache – The content served from the ISR cache when there is an edge-cache miss
*   You add to your [Fast Origin Transfer](/docs/manage-cdn-usage#fast-origin-transfer) usage

Explore your [usage top paths](/docs/limits/usage#top-paths) to better understand ISR usage and pricing.

## [More resources](#more-resources)

*   [Quickstart](/docs/incremental-static-regeneration/quickstart)
*   [Monitor ISR on Vercel](/docs/observability/monitoring)
*   [Next.js Caching](https://nextjs.org/docs/app/building-your-application/data-fetching/caching)

--------------------------------------------------------------------------------
title: "Incremental Static Regeneration usage and pricing"
description: "This page outlines information on the limits that are applicable to using Incremental Static Regeneration (ISR), and the costs they can incur."
last_updated: "null"
source: "https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing"
--------------------------------------------------------------------------------

# Incremental Static Regeneration usage and pricing

Copy page

Ask AI about this page

Last updated June 2, 2025

## [Pricing](#pricing)

Vercel offers several methods for caching data within Vercel’s managed infrastructure. [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) caches your data at the edge and persists it to durable storage – data reads and writes from durable storage will incur costs.

ISR Reads and Writes are priced regionally based on the [Vercel function region(s)](/docs/functions/configuring-functions/region) set at your project level. See the regional [pricing documentation](/docs/pricing/regional-pricing) and [ISR cache region](#isr-cache-region) for more information.

## [Usage](#usage)

The table below shows the metrics for the [ISR](/docs/pricing/incremental-static-regeneration) section of the [Usage dashboard](/docs/pricing/manage-and-optimize-usage#viewing-usage).

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column. The cost for each metric is based on the request location, see the [pricing section](/docs/incremental-static-regeneration/limits-and-pricing#pricing) and choose the region from the dropdown for specific information.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Reads](/docs/incremental-static-regeneration/limits-and-pricing#isr-reads-chart) | The total amount of Read Units used to access ISR data | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes) |
| [Writes](/docs/incremental-static-regeneration/limits-and-pricing#isr-writes-chart) | The total amount of Write Units used to store new ISR data | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes) |

### [Storage](#storage)

There is no limit on storage for ISR, all the data you write remains cached for the duration you specify. Only you or your team can invalidate this cache—unless it goes unaccessed for 31 days.

### [Written data](#written-data)

The total amount of Write Units used to durably store new ISR data, measured in 8KB units.

### [Read data](#read-data)

The total amount of Read Units used to access the ISR data, measured in 8KB units.

ISR reads and writes are measured in 8 KB units:

*   Read unit: One read unit equals 8 KB of data read from the ISR cache
*   Write unit: One write unit equals 8 KB of data written to the ISR cache

## [ISR reads and writes price](#isr-reads-and-writes-price)

ISR Reads and Writes are priced regionally based on the [Vercel function region(s)](/docs/functions/configuring-functions/region) set at your project level. See the regional [pricing documentation](/docs/pricing/regional-pricing) and [ISR cache region](#isr-cache-region) for more information.

### [ISR cache region](#isr-cache-region)

The ISR cache region for your deployment is set at build time and is based on the [default Function region](/docs/functions/configuring-functions/region#setting-your-default-region) set at your project level. If you have multiple regions set, the region that will give you the best [cost](/docs/pricing/regional-pricing) optimization is selected. For example, if `iad1` (Washington, D.C., USA) is one of your regions, it is always selected.

For best performance, set your default Function region (and hence your ISR cache region) to be close to where your users are. Although this may affect your ISR costs, automatic compression of ISR writes will keep your costs down.

## [Optimizing ISR reads and writes](#optimizing-isr-reads-and-writes)

You are charged based on the volume of data read from and written to the ISR cache, and the regions where reads and writes occur. To optimize ISR usage, consider the following strategies.

*   For content that rarely changes, set a longer [time-based revalidation](/docs/incremental-static-regeneration/quickstart#background-revalidation) interval
*   If you have events that trigger data updates, use [on-demand revalidation](/docs/incremental-static-regeneration/quickstart#on-demand-revalidation)

When attempting to perform a revalidation, if the content has no changes from the previous version, no ISR write units will be incurred. This applies to be time-based ISR as well as on-demand revalidation.

If you are seeing writes, this is because the content has changed. Here's how you can debug unexpected writes:

*   Ensure you're not using `new Date()` in the ISR output
*   Ensure you're not using `Math.random()` in the ISR output
*   Ensure any other code which produces a non-deterministic output is not included in the ISR output

## [ISR reads chart](#isr-reads-chart)

You get charged based on the amount of data read from your ISR cache and the region(s) in which the reads happen.

When viewing your ISR read units chart, you can group by:

*   Projects: To see the number of read units for each project
*   Region: To see the number of read units for each region

## [ISR writes chart](#isr-writes-chart)

You get charged based on the amount of ISR write units written to your ISR cache and the region(s) in which the writes happen.

When viewing your ISR writes chart, you can group by sum of units to see a total of all writes across your team's projects.

*   Projects: To see the number of write units for each project
*   Region: To see the number of write units for each region

--------------------------------------------------------------------------------
title: "Getting started with ISR"
description: "Learn how to use Incremental Static Regeneration (ISR) to regenerate your pages without rebuilding and redeploying your site."
last_updated: "null"
source: "https://vercel.com/docs/incremental-static-regeneration/quickstart"
--------------------------------------------------------------------------------

# Getting started with ISR

Copy page

Ask AI about this page

Last updated April 9, 2025

This guide will help you get started with using Incremental Static Regeneration (ISR) on your project, showing you how to regenerate your pages without rebuilding and redeploying your site. When a page with ISR enabled is regenerated, the most recent data for that page is fetched, and its cache is updated. There are two ways to trigger regeneration:

*   Background revalidation – Regeneration that recurs on an interval
*   On-demand revalidation – Regeneration that occurs when you send certain API requests to your app

## [Background Revalidation](#background-revalidation)

Background revalidation allows you to purge the cache for an ISR route automatically on an interval.

When using Next.js with the App Router, you can enable ISR by using the `revalidate` route segment config for a layout or page.

Next.js (/app)Next.js (/pages)SvelteKitNuxt

apps/example/page.tsx

TypeScript

TypeScriptJavaScript

```
export const revalidate = 10; // seconds
```

### [Example](#example)

The following example renders a list of blog posts from a demo site called `jsonplaceholder`, revalidating every 10 seconds or whenever a person visits the page:

Next.js (/app)Next.js (/pages)SvelteKitNuxt

app/blog-posts/page.tsx

TypeScript

TypeScriptJavaScript

```
export const revalidate = 10; // seconds
 
interface Post {
  title: string;
  id: number;
}
 
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog');
  const posts = (await res.json()) as Post[];
  return (
    <ul>
      {posts.map((post: Post) => {
        return <li key={post.id}>{post.title}</li>;
      })}
    </ul>
  );
}
```

To test this code, run the appropriate `dev` command for your framework, and navigate to the `/blog-posts/` route.

You should see a bulleted list of blog posts.

## [On-Demand Revalidation](#on-demand-revalidation)

On-demand revalidation allows you to purge the cache for an ISR route whenever you want, foregoing the time interval required with background revalidation.

To revalidate a page on demand with Next.js:

1.  Create an Environment Variable which will store a revalidation secret
2.  Create an API Route that checks for the secret, then triggers revalidation

The following example demonstrates an API route that triggers revalidation if the query paramater `?secret` matches a secret Environment Variable:

Next.js (/app)Next.js (/pages)SvelteKitNuxt

app/api/revalidate/route.ts

TypeScript

TypeScriptJavaScript

```
import { revalidatePath } from 'next/cache';
 
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  if (searchParams.get('secret') !== process.env.MY_SECRET_TOKEN) {
    return new Response('Invalid credentials', {
      status: 401,
    });
  }
 
  revalidatePath('/blog-posts');
 
  return Response.json({
    revalidated: true,
    now: Date.now(),
  });
}
```

See the [background revalidation section above](#background-revalidation) for a full ISR example.

## [Templates](#templates)

## [Next steps](#next-steps)

Now that you have set up ISR, you can explore the following:

*   [Explore usage and pricing](/docs/incremental-static-regeneration/limits-and-pricing)
*   [Monitor ISR on Vercel through Observability](/docs/observability/monitoring)

--------------------------------------------------------------------------------
title: "Performing an Instant Rollback on a Deployment"
description: "Learn how to perform an Instant Rollback on your production deployments and quickly roll back to a previously deployed production deployment."
last_updated: "null"
source: "https://vercel.com/docs/instant-rollback"
--------------------------------------------------------------------------------

# Performing an Instant Rollback on a Deployment

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel provides Instant Rollback as a way to quickly revert to a previous production deployment. This can be useful in situations that require a swift recovery from production incidents, like breaking changes or bugs. It's important to keep in mind that during a rollback:

*   The rolled back deployment is treated as a restored version of a previous deployment
*   The configuration used for the rolled back deployment will potentially become stale
*   The environment variables will not be updated if you change them in the project settings and will roll back to a previous build
*   If the project uses [cron jobs](/docs/cron-jobs), they will be reverted to the state of the rolled back deployment

For teams on a Pro or Enterprise plan, all deployments previously aliased to a production domain are [eligible to roll back](#eligible-deployments). Hobby users can roll back to the immediately previous deployment.

## [How to roll back deployments](#how-to-roll-back-deployments)

To initiate an Instant Rollback from the Vercel dashboard:

1.  ### [Select your project](#select-your-project)
    
    On the project's overview page, you will see the Production Deployment tile. From there, click Instant Rollback.
    
    ![Access Instant Rollback from the production deployment tile.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Finstant-rollback.png&w=3840&q=75)![Access Instant Rollback from the production deployment tile.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Finstant-rollback-dark.png&w=3840&q=75)
    
    Access Instant Rollback from the production deployment tile.
    
2.  ### [Select the deployment to roll back to](#select-the-deployment-to-roll-back-to)
    
    After selecting Instant Rollback, you'll see an dialog that displays your current production deployment and the eligible deployments that you can roll back to.
    
    If you're on the Pro or Enterprise plans, you can also click the Choose another deployment button to display a list of all [eligible](#eligible-deployments) deployments.
    
    Select the deployment that you'd like to roll back to and click Continue.
    
    ![Dialog showing the current and previous deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-process.png&w=1080&q=75)![Dialog showing the current and previous deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-process-dark.png&w=1080&q=75)
    
    Dialog showing the current and previous deployments.
    
3.  ### [Verify the information](#verify-the-information)
    
    Once you've selected the deployment to roll back to, verify the roll back information:
    
    *   The names of the domains and sub-domains that will be rolled back
    *   There are no change in Environment Variables, and they will remain in their original state
    *   A reminder about the changing behavior of external APIs, databases, and CMSes used in the current or previous deployments
4.  ### [Confirm the rollback](#confirm-the-rollback)
    
    Once you have verified the details, click the Confirm Rollback button. At this point, you'll get confirmation details about the successful rollback.
    
    ![Message for a successful roll back session.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-success.png&w=828&q=75)![Message for a successful roll back session.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-success-dark.png&w=828&q=75)
    
    Message for a successful roll back session.
    
    If you have custom aliases, ensure the domains listed above are correct. The rolled-back deployment does not include custom aliases since these are not a part of your project’s domain settings. Custom aliases will only be included if they were present on the previous production deployment.
    
5.  ### [Successful rollback](#successful-rollback)
    
    The rollback happens instantaneously and Vercel will point your domain and sub-domain back to the selected deployment. The production deployment tile for your project will highlight the canceled and rolled back commits.
    
    When using Instant Rollback, Vercel will turn off [auto-assignment of production domains](/docs/deployments/promoting-a-deployment#staging-and-promoting-a-production-deployment). This means that when you or your team push changes to production, the roll backed deployment won't be replaced.
    
    To replace the rolled back deployment, either turn on the Auto-assign Custom Production Domains toggle from the [Production Environment settings of your project settings](/docs/deployments/promoting-a-deployment#staging-and-promoting-a-production-deployment) and push a new change, or perform a [manual promote](/docs/deployments/promoting-a-deployment#promote-a-deployment-from-preview-to-production) to a newer deployment which will automatically turn the setting on.
    
    ![Production tile showing details about the rolled-back deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-on-production-tile.png&w=3840&q=75)![Production tile showing details about the rolled-back deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-on-production-tile-dark.png&w=3840&q=75)
    
    Production tile showing details about the rolled-back deployment.
    

*   You cannot run parallel roll backs on the same project
*   Only one deployment can be rolled back at a time for every project. However, a rolled back deployment stays disabled in your deployment list and can be accessed and re-reverted whenever you want
    

### [Accessing Instant Rollback from Deployments tab](#accessing-instant-rollback-from-deployments-tab)

You can also roll back from the main Deployments tab in your dashboard. Filtering the deployments list by `main` is recommended to view a list of [eligible roll back deployments](#eligible-deployments) as this list all your current and previous deployments promoted to production.

Click the vertical ellipses (⋮) next to the deployment row and select the Instant Rollback option from the context menu.

![Perform instant roll back on any of your main branch's deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-from-deploys-list.png&w=3840&q=75)![Perform instant roll back on any of your main branch's deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Frollback-from-deploys-list-dark.png&w=3840&q=75)

Perform instant roll back on any of your main branch's deployments.

## [Who can roll back deployments?](#who-can-roll-back-deployments)

*   Hobby plan: On the hobby plan you can roll back to the previous deployment
*   Pro and Enterprise plan: Owners and Members on these plans can roll back to any [eligible deployment](#eligible-deployments).

## [Eligible deployments](#eligible-deployments)

Deployments previously aliased to a production domain are eligible for Instant Rollback. Deployments that have never been aliased to production a domain, e.g., most [preview deployments](/docs/deployments/environments#preview-environment-pre-production), are not eligible.

## [Comparing Instant Rollback and manual promote options](#comparing-instant-rollback-and-manual-promote-options)

To compare the manual promotion options, see [Manually promoting to Production](/docs/deployments/promoting-a-deployment).

--------------------------------------------------------------------------------
title: "Vercel Integrations"
description: "Learn how to extend Vercel's capabilities by integrating with your preferred providers for AI, databases, headless content, commerce, and more."
last_updated: "null"
source: "https://vercel.com/docs/integrations"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./11-supported-frameworks-on-vercel.md) | [Index](./index.md) | [Next →](./13-vercel-integrations.md)
