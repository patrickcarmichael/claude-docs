---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Together Cookbooks & Example Apps

Source: https://docs.together.ai/examples

Explore our vast library of open-source cookbooks & example apps

export const FeaturedExampleAppCard = ({title, description, tags, imageUrl, openUrl}) => {
  return <a href={openUrl} target="_blank" rel="noopener noreferrer" className="relative w-full flex flex-col bg-white border border-neutral-300 dark:border-gray-700 rounded-2xl overflow-hidden transition-all">
      <div className="overflow-hidden rounded-2xl">
        <img noZoom src={imageUrl} className="w-full h-[355px] object-cover" alt={title} />
      </div>
      <div className="flex-1 bg-white/90 dark:bg-[#12161A] p-4 flex flex-col justify-start backdrop-blur-md absolute bottom-0 w-full">
        <div className="flex items-center gap-3 mb-2 w-full">
          <h3 className="text-2xl font-medium text-black dark:text-white flex-1">
            {title}
          </h3>
          <div className="flex gap-2">
            {tags.map((tag, index) => <FeatureBadge key={index} {...tag} />)}
          </div>
        </div>
        <p className="text-sm text-neutral-700 dark:text-gray-400" dangerouslySetInnerHTML={{
    __html: description.replace(/\n/g, "<br/>")
  }}></p>
      </div>
    </a>;
};

export const ExampleAppsCard = ({title, description, tags, openUrl, githubUrl, imageUrl}) => {
  return <div className="md:min-w-[280px] w-full relative overflow-hidden rounded-2xl bg-white dark:bg-transparent dark:hover:bg-[#0B0C0E] border border-[#d9e1ec] dark:border-gray-700 hover:bg-gray-50 transition-all flex flex-col">
      <div className="w-full h-[178px] bg-neutral-100 dark:bg-transparent dark:hover:bg-[#0B0C0E] flex items-center justify-center">
        <img src={imageUrl} noZoom className="w-fit h-[132px] rounded-lg object-cover border border-[#d9e1ec]" style={{
    boxShadow: "0px 2px 14px -2px rgba(0,0,0,0.05)"
  }} alt={title} />
      </div>
      <div className="flex-1 p-4 flex flex-col">
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-base font-medium text-black dark:text-white flex-1 line-clamp-1" title={title}>
            {title}
          </h3>
          <div className="flex gap-2 ml-2">
            {tags.map((tag, index) => <FeatureBadge key={index} {...tag} />)}
          </div>
        </div>
        <p className="text-sm text-neutral-600 dark:text-gray-400 mb-4 flex-1">
          {description}
        </p>
        <div className="flex items-center gap-4 mt-auto">
          <a href={openUrl} target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 text-sm text-neutral-900 dark:text-white hover:text-neutral-700 dark:hover:text-gray-100">
            <svg width={14} height={14} viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5">
              <path d="M2.625 11.375L11.375 2.625M11.375 2.625H4.8125M11.375 2.625V9.1875" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            Open
          </a>
          <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 text-sm text-neutral-900 dark:text-white hover:text-neutral-700 dark:hover:text-gray-100">
            <img noZoom src="/images/github.svg" alt="GitHub" className="w-3.5 h-3.5 dark:invert" />
            GitHub
          </a>
        </div>
      </div>
    </div>;
};

export const CookbookWideCard = ({title, description, tags, githubUrl}) => {
  return <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="lg:max-w-[699px] w-full flex bg-white dark:bg-transparent dark:hover:bg-[#0B0C0E] border border-neutral-300 dark:border-gray-700 rounded-2xl overflow-hidden hover:bg-gray-50 transition-all flex-col md:flex-row">
      <div className="flex-1 flex flex-col justify-start px-7 py-6">
        <div className="flex items-center gap-3 mb-2">
          <h3 className="text-xl font-medium text-black dark:text-white">
            {title}
          </h3>
          <div className="flex gap-2 flex-shrink-0">
            {tags && tags.length > 0 && <FeatureBadge {...tags[0]} />}
          </div>
        </div>
        <p className="text-sm text-neutral-600 dark:text-gray-400">
          {description}
        </p>
      </div>
      <div className="flex items-end gap-6 pr-6 px-7 py-6 pt-0 md:pt-4">
        <div className="flex items-center gap-2 text-sm text-neutral-700 dark:text-gray-400 hover:text-neutral-900 dark:hover:text-gray-300">
          <img noZoom src="/images/github.svg" alt="GitHub" className="w-3.5 h-3.5 dark:invert" />
          GitHub
        </div>
      </div>
    </a>;
};

export const FeatureBadge = ({label, bgColor, textColor}) => {
  return <div className="flex justify-center items-center flex-grow-0 flex-shrink-0 relative overflow-hidden gap-2.5 px-2 py-1 rounded-[100px] dark:invert" style={{
    backgroundColor: bgColor
  }}>
      <p className="flex-grow-0 flex-shrink-0 text-xs text-center" style={{
    color: textColor
  }}>
        {label}
      </p>
    </div>;
};

export const CookbookCard = ({title, description, tags, readUrl, githubUrl}) => {
  return <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="h-auto min-h-[116px] p-4 bg-white dark:bg-transparent dark:hover:bg-[#0B0C0E] border border-neutral-300 dark:border-gray-700 rounded-xl hover:bg-gray-50 transition-all">
      <div className="flex flex-col h-full">
        <div className="flex items-start justify-between mb-3">
          <h3 title={title} className="text-base font-medium text-black dark:text-white flex-1 mr-3 line-clamp-2">
            {title}
          </h3>
          <div className="flex gap-2 flex-shrink-0">
            {tags.map((tag, index) => <FeatureBadge key={index} {...tag} />)}
          </div>
        </div>
        <p className="text-sm text-neutral-600 dark:text-gray-400 mb-4 flex-1">
          {description}
        </p>
        <div className="flex items-center gap-4 mt-auto">
          <div className="flex items-center gap-2 text-sm text-neutral-700 dark:text-gray-400 hover:text-neutral-900 dark:hover:text-gray-300">
            <img noZoom src="/images/github.svg" alt="GitHub" className="w-3.5 h-3.5" />
            GitHub
          </div>
        </div>
      </div>
    </a>;
};

export const CookbookShowcase = () => {
  const cookbooks = [{
    title: "Serial Chain Agent",
    description: "Chain multiple LLM calls sequentially to process complex tasks.",
    tags: [{
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb"
  }, {
    title: "Conditional Router Agent Workflow",
    description: "Create an agent that routes tasks to specialized models.",
    tags: [{
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Conditional_Router_Agent_Workflow.ipynb"
  }, {
    title: "Parallel Agent Workflow",
    description: "Run multiple LLMs in parallel and aggregate their solutions.",
    tags: [{
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Parallel_Agent_Workflow.ipynb"
  }, {
    title: "Open Data Science Agent",
    description: "A guide on how to build an open source data science agent",
    tags: [{
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DataScienceAgent/Together_Open_DataScience_Agent.ipynb",
    featured: true
  }, {
    title: "Conversation Finetuning",
    description: "Fine-tuning LLMs on multi-step conversations.",
    tags: [{
      label: "Fine-tuning",
      bgColor: "#fef3f2",
      textColor: "#c1320b"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Multiturn_Conversation_Finetuning.ipynb"
  }, {
    title: "LoRA Inference and Fine-tuning",
    description: "Perform LoRA fine-tuning and inference on Together AI.",
    tags: [{
      label: "Fine-tuning",
      bgColor: "#fef3f2",
      textColor: "#c1320b"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/LoRA_Finetuning%26Inference.ipynb"
  }, {
    title: "Summarization Long Context Finetuning",
    description: "Long context fine-tuning to improve summarization capabilities.",
    tags: [{
      label: "Fine-tuning",
      bgColor: "#fef3f2",
      textColor: "#c1320b"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Summarization_LongContext_Finetuning.ipynb"
  }, {
    title: "Finetuning Cookbook",
    description: "A full guide on how to fine-tune an LLM in 5 mins",
    tags: [{
      label: "Fine-tuning",
      bgColor: "#f0fdf4",
      textColor: "#15803d"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb",
    featured: true
  }, {
    title: "Open Contextual RAG",
    description: "An implementation of Contextual Retrieval using open models.",
    tags: [{
      label: "RAG",
      bgColor: "#f0fdf4",
      textColor: "#15803d"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Open_Contextual_RAG.ipynb"
  }, {
    title: "Text RAG",
    description: "Implement text-based Retrieval-Augmented Generation",
    tags: [{
      label: "RAG",
      bgColor: "#f0fdf4",
      textColor: "#15803d"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Text_RAG.ipynb"
  }, {
    title: "Multimodal Search and Conditional Image Generation",
    description: "Text-to-image and image-to-image search and conditional image generation.",
    tags: [{
      label: "Search",
      bgColor: "#fef7ed",
      textColor: "#c2410c"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Multimodal_Search_and_Conditional_Image_Generation.ipynb"
  }, {
    title: "Search with Reranking",
    description: "Improve search results with rerankers",
    tags: [{
      label: "Search",
      bgColor: "#fef7ed",
      textColor: "#c2410c"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Search_with_Reranking.ipynb"
  }, {
    title: "Semantic Search",
    description: "Implement vector search with embedding models",
    tags: [{
      label: "Search",
      bgColor: "#fef7ed",
      textColor: "#c2410c"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Semantic_Search.ipynb"
  }, {
    title: "Structured Text Extraction from Images",
    description: "Extract structured text from images",
    tags: [{
      label: "Miscellaneous",
      bgColor: "#faf5ff",
      textColor: "#7c3aed"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Structured_Text_Extraction_from_Images.ipynb"
  }, {
    title: "Evaluating LLMs on SimpleQA",
    description: "Using our evals and batch APIs to evaluate LLMs on benchmarks",
    tags: [{
      label: "Batch & Evals",
      bgColor: "#faf5ff",
      textColor: "#7c3aed"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Batch_Inference_Evals.ipynb",
    featured: true
  }, {
    title: "Knowledge Graphs with Structured Outputs",
    description: "Get LLMs to generate knowledge graphs",
    tags: [{
      label: "Miscellaneous",
      bgColor: "#faf5ff",
      textColor: "#7c3aed"
    }],
    githubUrl: "https://github.com/togethercomputer/together-cookbook/blob/main/Knowledge_Graphs_with_Structured_Outputs.ipynb"
  }];
  const featuredCookbooks = cookbooks.filter(cook => cook.featured === true);
  const exampleApps = [{
    title: "EasyEdit",
    description: "Edit any images with a simple prompt using Flux Kontext",
    tags: [{
      label: "Image Generation",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }, {
      label: "Flux",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }],
    openUrl: "https://www.easyedit.io/",
    githubUrl: "https://github.com/Nutlope/easyedit",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/6864177bd0f8b8860ac25c54_og-image.png"
  }, {
    title: "Self.so",
    description: "Generate a personal website from your LinkedIn/Resume",
    tags: [{
      label: "Website Generator",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }, {
      label: "Next.js",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }],
    openUrl: "https://www.self.so/",
    githubUrl: "https://github.com/nutlope/self.so",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/68641974ad1129515a58ba21_og.png"
  }, {
    title: "BlinkShot",
    description: "A realtime AI image playground built with Flux Schnell on Together AI",
    tags: [{
      label: "Image Generation",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }, {
      label: "Realtime",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }],
    openUrl: "https://www.blinkshot.io/",
    githubUrl: "https://github.com/Nutlope/blinkshot",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095fce451e1cc6b5e282ec_demos_09.jpg"
  }, {
    title: "Llama-OCR",
    description: "A OCR tool that takes documents (like receipts, PDFs with tables/charts) and outputs markdown",
    tags: [{
      label: "OCR",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }, {
      label: "Document Processing",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }],
    openUrl: "https://llamaocr.com/",
    githubUrl: "https://github.com/Nutlope/llama-ocr",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/674e422e5c031a77f577de75_og-image.png"
  }, {
    title: "Open Deep Research",
    description: "Generate reports using our open source Deep Research implementation",
    tags: [{
      label: "Research",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }],
    openUrl: "https://www.opendeepresearch.dev/",
    githubUrl: "https://github.com/Nutlope/open-deep-research",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/686417ade85fee0a1605c96c_og.jpg"
  }, {
    title: "BillSplit",
    description: "An easy way to split restaurant bills with OCR using vision models on Together AI",
    tags: [{
      label: "OCR",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }, {
      label: "Vision",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }],
    openUrl: "https://www.usebillsplit.com/",
    githubUrl: "https://github.com/nutlope/billsplit",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/686418ffffc3ba614b0fae81_og.png"
  }, {
    title: "Smart PDF",
    description: "Summarize PDFs into beautiful sections with Llama 3.3 70B",
    tags: [{
      label: "PDF",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }, {
      label: "Summarization",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }],
    openUrl: "https://www.smartpdfs.ai/",
    githubUrl: "https://github.com/Nutlope/smartpdfs",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/68641880cf8bd0f76e967ed5_og.jpg"
  }, {
    title: "Agent Recipes",
    description: "Explore common agent recipes with ready to copy code to improve your LLM applications.",
    tags: [{
      label: "Agent",
      bgColor: "#f2f5fa",
      textColor: "#0b4fc1"
    }, {
      label: "Recipes",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }],
    openUrl: "https://www.agentrecipes.com/",
    githubUrl: "https://www.agentrecipes.com/",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/678e79483bbe41af95b3f3e2_opengraph-image.png"
  }, {
    title: "Napkins",
    description: "A wireframe to app tool that can take in a UI mockup of a site and give you React code.",
    tags: [{
      label: "Code Generation",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }, {
      label: "Design to Code",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }],
    openUrl: "https://www.napkins.dev/",
    githubUrl: "https://github.com/nutlope/napkins",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095fb902512aea09a3fe25_demos_10.jpg"
  }, {
    title: "Product Description Generator",
    description: "Upload a picture of any product and get descriptions for it in multiple languages",
    tags: [{
      label: "Vision",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "E-commerce",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }],
    openUrl: "https://product-descriptions.vercel.app/",
    githubUrl: "https://github.com/Nutlope/description-generator",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/6716ccd2cd9a652af7e08da7_OG%20(3).png"
  }, {
    title: "Which LLM",
    description: "Find the perfect LLM for your use case",
    tags: [{
      label: "Tool",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }, {
      label: "Discovery",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }],
    openUrl: "https://whichllm.together.ai/",
    githubUrl: "",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/68641701ffdd7e10ce044cbf_opengraph-image.png"
  }, {
    title: "TwitterBio",
    description: "An AI app that can generate your twitter/X bio for you",
    tags: [{
      label: "Social Media",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }, {
      label: "Content Generation",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }],
    openUrl: "https://www.twitterbio.io/",
    githubUrl: "https://github.com/Nutlope/twitterbio",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095f99d84fe251d183464e_demos_06.jpg"
  }, {
    title: "LogoCreator",
    description: "An logo generator that creates professional logos in seconds using Flux Pro 1.1",
    tags: [{
      label: "Image Generation",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }, {
      label: "Design",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }],
    openUrl: "https://www.logo-creator.io/",
    githubUrl: "https://github.com/Nutlope/logocreator",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/674e426eaa246fd6c4dee420_logocreatorog.jpeg"
  }, {
    title: "LlamaTutor",
    description: "A personal tutor that can explain any topic at any education level by using a search API along with Llama 3.1.",
    tags: [{
      label: "Education",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }, {
      label: "Search",
      bgColor: "#fef7ed",
      textColor: "#c2410c"
    }],
    openUrl: "https://llamatutor.together.ai/",
    githubUrl: "https://github.com/Nutlope/llamatutor",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095f536dbac55809321d56_demos_02.jpg"
  }, {
    title: "PicMenu",
    description: "A menu visualizer that takes a restaurant menu and generates nice images for each dish.",
    tags: [{
      label: "Image Generation",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "Restaurant",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }],
    openUrl: "https://www.picmenu.co/",
    githubUrl: "https://github.com/Nutlope/picMenu",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/674e41ad845f29355ec816cd_OG11.png"
  }, {
    title: "Loras.dev",
    description: "Explore and use Flux loras to generate images in different styles",
    tags: [{
      label: "Image Generation",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }, {
      label: "Flux",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }],
    openUrl: "https://www.loras.dev/",
    githubUrl: "https://github.com/Nutlope/loras-dev",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/68641ade6d39c3fa108678f9_opengraph-image.png"
  }, {
    title: "Code Arena",
    description: "Watch AI models compete in real-time & vote on the best one",
    tags: [{
      label: "Code Generation",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }, {
      label: "Comparison",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }],
    openUrl: "https://www.llmcodearena.com/",
    githubUrl: "https://github.com/Nutlope/codearena",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/678e79bb1f1de4f36c6f4414_og-image.png"
  }, {
    title: "Together Chatbot",
    description: "A simple Next.js chatbot that uses Together AI LLMs for inference",
    tags: [{
      label: "Chatbot",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }, {
      label: "Next.js",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }],
    openUrl: "https://together-solutions.vercel.app/",
    githubUrl: "https://github.com/Nutlope/together-chatbot",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/68641bc4068faf64fb2311b4_CleanShot%202025-07-01%20at%2013.32.19%402x.png"
  }, {
    title: "Sentiment Analysis",
    description: "A simple example app that shows how to use logprobs to get probabilities from LLMs",
    tags: [{
      label: "Analytics",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }, {
      label: "Demo",
      bgColor: "#faf5ff",
      textColor: "#000000"
    }],
    openUrl: "https://together-sentiment-analysis.vercel.app/",
    githubUrl: "https://github.com/Nutlope/sentiment-analysis",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/686420d720065babb9f9c07f_CleanShot%202025-07-01%20at%2013.27.21%402x.png"
  }, {
    title: "ExploreCareers",
    description: "Upload your resume, add your interests, and get personalized career paths with AI",
    tags: [{
      label: "Career",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "Resume",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }],
    openUrl: "https://explorecareers.vercel.app/",
    githubUrl: "https://github.com/Nutlope/ExploreCareers",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095f7c934e47e89292306f_demos_03.jpg"
  }, {
    title: "PDFtoChat",
    description: "Chat with your PDFs (blogs, textbooks, papers) with AI",
    tags: [{
      label: "PDF",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }, {
      label: "Chat",
      bgColor: "#fef3f2",
      textColor: "#000000"
    }],
    openUrl: "https://www.pdftochat.com/",
    githubUrl: "https://github.com/nutlope/pdftochat",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095f1b6dbac5580931e402_demos_04.jpg"
  }, {
    title: "TurboSeek",
    description: "An AI search engine inspired by Perplexity that can give you real-time answers",
    tags: [{
      label: "Search",
      bgColor: "#fef7ed",
      textColor: "#c2410c"
    }, {
      label: "AI Assistant",
      bgColor: "#f0fdf4",
      textColor: "#000000"
    }],
    openUrl: "https://www.turboseek.io/",
    githubUrl: "https://github.com/Nutlope/turboseek",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095f097551823f8d1f9cc6_demos_01.jpg"
  }, {
    title: "NotesGPT",
    description: "Record voice notes and get a transcript, summary, and action items with AI.",
    tags: [{
      label: "Voice",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }, {
      label: "Transcription",
      bgColor: "#fef7ed",
      textColor: "#000000"
    }],
    openUrl: "https://usenotesgpt.com/",
    githubUrl: "https://github.com/nutlope/notesgpt",
    imageUrl: "https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67095efcd84d1679d2c83e67_demos_08.jpg"
  }];
  const featuredApp = {
    title: "LlamaCoder",
    description: "An open source Claude Artifacts – generate small apps with one prompt. \n Powered by Llama 3 405B.",
    tags: [{
      label: "Next.js",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "Code Generation",
      bgColor: "#f2f5fa",
      textColor: "#000000"
    }, {
      label: "Featured",
      bgColor: "#fef3f2",
      textColor: "#c1320b"
    }],
    openUrl: "https://llamacoder.together.ai/",
    githubUrl: "https://github.com/nutlope/llamacoder",
    imageUrl: "/images/llama-coder-og.png"
  };
  const normalCookbooks = cookbooks.filter(cook => !cook.featured);
  return <div className="w-full max-w-8xl mx-auto px-4 sm:px-6 lg:px-8 py-8 bg-white dark:bg-[#13161A]">
      {}
      <div className="mb-12 flex flex-col gap-3">
        <h1 className="text-2xl font-medium text-left text-neutral-900 dark:text-white md:text-[28px]">
          Together cookbooks & example apps
        </h1>
        <p className="text-base text-left text-[#3e4146] dark:text-gray-400">
          Explore our vast library of open-source cookbooks & example apps.
        </p>
      </div>

      {}
      <section className="mb-16">
        <div className="flex flex-col lg:flex-row gap-8">
          {}
          <div className="w-full lg:w-1/2">
            <h2 className="text-base font-medium text-neutral-600 dark:text-gray-400 mb-4">
              Featured cookbooks
            </h2>
            <div className="grid grid-cols-1 gap-[17px]">
              {featuredCookbooks.map((cookbook, index) => {
    const {featured, ...cook} = cookbook;
    return <CookbookWideCard key={index} {...cook} />;
  })}
            </div>
          </div>

          {}
          <div className="w-full lg:w-1/2">
            <h2 className="text-base font-medium text-neutral-600 dark:text-gray-400 mb-3">
              Featured example app
            </h2>
            <div className="w-full mx-auto lg:mx-0">
              <FeaturedExampleAppCard {...featuredApp} />
            </div>
          </div>
        </div>
      </section>

      {}
      <section className="mb-16">
        <div className="mb-8 flex flex-col lg:flex-row justify-between gap-2.5">
          <h2 className="text-2xl font-medium text-neutral-900 dark:text-white">
            Example apps
          </h2>
          <p className="text-base text-[#3e4146] dark:text-gray-400 max-w-2xl">
            Explore all of our open source TypeScript example apps.
          </p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {exampleApps.slice(0, 7).map((app, index) => <ExampleAppsCard key={index} {...app} />)}
          <a href="https://www.together.ai/demos" target="_blank" rel="noopener noreferrer" className="flex-grow-0 flex-shrink-0 flex items-center justify-center bg-neutral-50 border border-[#d9e1ec] dark:border-gray-700 rounded-2xl hover:bg-gray-50 dark:bg-transparent dark:hover:bg-[#0B0C0E] transition-all min-h-[168px] md:min-h-auto">
            <div className="flex flex-row gap-2 items-center justify-center">
              <svg width={14} height={14} viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5 mx-auto" preserveAspectRatio="none">
                <path d="M2.625 11.375L11.375 2.625M11.375 2.625H4.8125M11.375 2.625V9.1875" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              <p className="text-base text-[#000000] dark:text-white">
                View all example apps
              </p>
            </div>
          </a>
        </div>
      </section>

      {}
      <section>
        <div className="mb-8 flex flex-col lg:flex-row justify-between gap-2.5">
          <h2 className="text-2xl font-medium text-neutral-900 dark:text-white">
            Cookbooks
          </h2>
          <p className="text-base text-[#3e4146] dark:text-gray-400 max-w-2xl">
            Explore all of our open source Python cookbooks.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {normalCookbooks.slice(0, 11).map((cookbook, index) => {
    const {featured, ...cook} = cookbook;
    return <CookbookCard key={index} {...cook} />;
  })}
          <a href="https://www.together.ai/cookbooks" target="_blank" rel="noopener noreferrer" className="flex-grow-0 flex-shrink-0 h-[168px] flex items-center justify-center bg-neutral-50 border border-[#d9e1ec] dark:border-gray-700 rounded-2xl hover:bg-gray-50 dark:bg-transparent dark:hover:bg-[#0B0C0E] transition-all">
            <div className="flex flex-row gap-2 items-center justify-center">
              <svg width={14} height={14} viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5 mx-auto" preserveAspectRatio="none">
                <path d="M2.625 11.375L11.375 2.625M11.375 2.625H4.8125M11.375 2.625V9.1875" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              <p className="text-base text-[#000000] dark:text-white">
                View all cookbooks
              </p>
            </div>
          </a>
        </div>
      </section>
    </div>;
};

export default CookbookShowcase;


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
