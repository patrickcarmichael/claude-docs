**Navigation:** [← Previous](./08-speech-to-text.md) | [Index](./index.md) | Next →

---

# Together Cookbooks & Example Apps
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


# How to build a real-time image generator with Flux and Together AI
Source: https://docs.together.ai/external-link-02





# Overview
Source: https://docs.together.ai/intro

Welcome to Together AI’s docs! Together makes it easy to run, finetune, and train open source AI models with transparency and privacy.

export const ModelGrid = () => {
  const modelGroups = [{
    title: "Chat models:",
    link: "/docs/serverless-models#chat-models",
    hasViewAll: true,
    items: [{
      name: "DeepSeek R1",
      icon: "/images/intro/deepseek.png",
      description: "Upgraded DeepSeek-R1 with better reasoning, function calling, and coding, using 23K-token thinking to score 87.5% on AIME.",
      link: "https://www.together.ai/models/deepseek-r1"
    }, {
      name: "DeepSeek V3.1",
      icon: "/images/intro/deepseek.png",
      description: "671B parameters (37B activated), 128K context, hybrid thinking/non-thinking modes, advanced tool calling, agent capabilities",
      link: "https://www.together.ai/models/deepseek-v3-1"
    }, {
      name: "GPT-OSS-120B",
      icon: "/images/intro/gpt.png",
      description: "120B parameters, 128K context, reasoning with chain-of-thought, MoE architecture, Apache 2.0 license",
      link: "https://www.together.ai/models/gpt-oss-120b"
    }, {
      name: "Llama 4 Maverick",
      icon: "/images/intro/meta.png",
      description: "SOTA 128-expert MoE powerhouse for multilingual image/text understanding, creative writing, and enterprise-scale applications.",
      link: "https://www.together.ai/models/llama-4-maverick"
    }, {
      name: "Qwen 3 Next 80B",
      icon: "/images/intro/qwen.png",
      description: "80B parameters (3B activated), instruction-tuned MoE, 10x faster inference, hybrid attention mechanisms",
      link: "https://www.together.ai/models/qwen3-next-80b-a3b-instruct"
    }, {
      name: "Kimi K2 0905",
      icon: "/images/intro/kimi.png",
      description: "Upgraded state-of-the-art mixture-of-experts agentic intelligence model with 1T parameters, 256K context, and native tool use",
      link: "https://www.together.ai/models/kimi-k2-0905"
    }]
  }, {
    title: "Image models:",
    link: "/docs/serverless-models#image-models",
    hasViewAll: true,
    items: [{
      name: "FLUX.1 [schnell]",
      icon: "/images/intro/flux.png",
      description: "Fastest available endpoint for the SOTA open-source image generation model by Black Forest Labs.",
      link: "https://www.together.ai/models/flux-1-schnell"
    }, {
      name: "FLUX 1.1 [pro]",
      icon: "/images/intro/flux.png",
      description: "Premium image generation model by Black Forest Labs.",
      link: "https://www.together.ai/models/flux1-1-pro"
    }]
  }, {
    title: "Vision models:",
    link: "/docs/serverless-models#vision-models",
    hasViewAll: true,
    items: [{
      name: "Llama 4 Scout",
      icon: "/images/intro/meta.png",
      description: "SOTA 109B model with 17B active params & large context, excelling at multi-document analysis, codebase reasoning, and personalized tasks.",
      link: "https://www.together.ai/models/llama-4-scout"
    }, {
      name: "Qwen2.5 VL 72B",
      icon: "/images/intro/qwen.png",
      description: "Vision-language model with advanced visual reasoning, video understanding, structured outputs, and agentic capabilities.",
      link: "https://www.together.ai/models/qwen2-5-vl-72b-instruct"
    }]
  }, {
    title: "Audio models:",
    link: "/docs/serverless-models#audio-models",
    hasViewAll: true,
    items: [{
      name: "Cartesia Sonic 2",
      icon: "/images/intro/cartesia.png",
      description: "Low-latency, ultra-realistic voice model, served in partnership with Cartesia.",
      link: "https://www.together.ai/models/cartesia-sonic"
    }, {
      name: "Whisper Large v3",
      icon: "/images/intro/gpt.png",
      description: "High-performance speech-to-text model delivering transcription 15x faster than OpenAI with support for 1GB+ files, 50+ languages, and production-ready infrastructure.",
      link: "https://www.together.ai/models/openai-whisper-large-v3"
    }]
  }, {
    title: "Embedding models:",
    link: "/docs/serverless-models#embedding-models",
    hasViewAll: false,
    items: [{
      name: "M2-BERT 80M 2K",
      icon: "/images/intro/bert.png",
      description: "An 80M checkpoint of M2-BERT, pretrained with sequence length 2048, and it has been fine-tuned for long-context retrieval.",
      link: "https://www.together.ai/models/m2-bert-80m-2k-retrieval"
    }, {
      name: "BGE-Base-EN",
      icon: "/images/intro/baai.png",
      description: "This model maps any text to a low-dimensional dense vector using FlagEmbedding.",
      link: "https://www.together.ai/models/bge-base-en-v1-5"
    }]
  }, {
    title: "Rerank models:",
    link: "/docs/serverless-models#rerank-models",
    hasViewAll: false,
    items: [{
      name: "Salesforce LlamaRank",
      icon: "/images/intro/salesforce.png",
      description: "Salesforce Research's proprietary fine-tuned rerank model with 8K context, outperforming Cohere Rerank for superior document retrieval.",
      link: "https://www.together.ai/models/salesforce-llamarank"
    }, {
      name: "Mxbai Rerank Large V2",
      icon: "/images/intro/mxbai.png",
      description: "1.5B-parameter RL-trained reranking model achieving state-of-the-art accuracy across 100+ languages with 8K context, outperforming Cohere and Voyage.",
      link: "https://www.together.ai/models/mxbai-rerank-large-v2"
    }]
  }];
  const getGridStyle = index => {
    const styles = [{
      gridRow: "span 4"
    }, {
      gridRow: "span 2"
    }, {
      gridRow: "span 2"
    }, {
      gridRow: "span 2"
    }, {
      gridRow: "span 1"
    }, {
      gridRow: "span 1"
    }];
    return styles[index] || ({});
  };
  return <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-2.5 lg:gap-4 max-w-[1080px] mx-auto mt-7">
      {modelGroups.map((group, index) => {
    const models = group.items;
    return <a href={group.link} key={index} className="rounded-xl bg-white dark:bg-[#13171B] border border-[#d9e1ec] dark:border-gray-700 overflow-hidden px-4 py-3 flex flex-row gap-0 justify-between" style={getGridStyle(index)}>
            <div className={"flex items-start flex-col  " + (group.hasViewAll ? "justify-between" : "justify-center")}>
              <h3 className="text-base text-left text-[#171a1e] dark:text-white font-normal my-0 leading-[24px]">
                {group.title}
              </h3>
              {group.hasViewAll && <div className="flex mt-4 flex-1 items-end">
                  <div className="flex items-center border-none">
                    <p className="text-sm font-light text-neutral-500 dark:text-gray-400 mr-2 whitespace-nowrap">
                      View all models
                    </p>
                    <svg width={5} height={8} viewBox="0 0 5 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1 1L4 4L1 7" stroke="currentColor" strokeLinecap="round" />
                    </svg>
                  </div>
                </div>}
            </div>
            <div className="flex flex-row gap-4 items-center self-baseline">
              <div className={"flex gap-1" + (group.hasViewAll ? " pb-4 flex-col" : "flex-row")}>
                {models.map((item, i) => <a key={i} href={item.link} target="_blank" rel="noopener noreferrer" className="flex items-center border-none gap-3 hover:bg-gray-50 dark:hover:bg-gray-700 transition-all rounded-md p-1" title={item.description}>
                    <img noZoom src={item.icon} className={"my-0 object-contain dark:invert " + (group.hasViewAll ? " min-w-5 h-5 " : " min-w-7 h-7")} alt="" />
                    {group.hasViewAll && <p className="text-sm text-left text-neutral-700 dark:text-gray-400 whitespace-nowrap font-normal leading-[26px]">
                        {item.name}
                      </p>}
                  </a>)}
              </div>

              {!group.hasViewAll && <svg width={5} height={8} viewBox="0 0 5 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M0.930237 1.11548L4.06977 4.00009L0.930237 6.88471" stroke="currentColor" strokeLinecap="round" />
                </svg>}
            </div>
          </a>;
  })}
    </div>;
};

export const WideCtaCard = ({title, description, iconUrl, href}) => {
  const cardContent = <div className="w-full lg:max-w-[400px] min-h-[200px] flex flex-col items-center p-2">
      {iconUrl && <img noZoom src={iconUrl} alt="" className="w-6 h-6 flex-shrink-0 mb-4 dark:invert" />}
      <div className="flex flex-col items-center text-center">
        <p className="text-base text-center text-[#0a0a0a] dark:text-white">
          {title}
        </p>
        <p className="text-sm text-center text-[#3e4146] dark:text-gray-400 mt-2 max-w-[208px]">
          {description}
        </p>
      </div>
    </div>;
  return href ? <a href={href} className="border-none flex font-normal hover:bg-gray-50 dark:hover:bg-[#0B0C0E] transition-all rounded-2xl">
      {cardContent}
    </a> : cardContent;
};

export const CtaCard = ({title, description, border = true, iconUrl, href}) => {
  const cardContent = <div className={`w-full lg:max-w-[344px] relative flex items-start gap-4 p-5 rounded-2xl hover:bg-gray-50 dark:hover:bg-[#0B0C0E] transition-all ${border ? "border border-[#d9e1ec] dark:border-gray-700 bg-[url('/images/intro/bg-card.png')] dark:bg-none" : ""}`} style={border ? {
    backgroundSize: "cover"
  } : {}}>
      {iconUrl ? <img noZoom src={iconUrl} alt="" className="w-10 h-10 flex-shrink-0 my-0 dark:invert" /> : <svg width={42} height={42} viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-10 h-10 flex-shrink-0" preserveAspectRatio="none">
          <rect x="0.5" y="0.5" width={41} height={41} rx="20.5" fill="#FAFCFF" />
          <rect x="0.5" y="0.5" width={41} height={41} rx="20.5" stroke="#E2E8F0" />
          <path fill-rule="evenodd" clip-rule="evenodd" d="M18.5 14.75C18.6358 14.75 18.7679 14.7943 18.8763 14.8761C18.9847 14.9579 19.0635 15.0728 19.1008 15.2033L19.7783 17.575C19.9242 18.0858 20.1978 18.5509 20.5735 18.9265C20.9491 19.3021 21.4142 19.5758 21.925 19.7217L24.2966 20.3992C24.4271 20.4366 24.5419 20.5154 24.6236 20.6238C24.7053 20.7322 24.7495 20.8643 24.7495 21C24.7495 21.1357 24.7053 21.2678 24.6236 21.3762C24.5419 21.4846 24.4271 21.5635 24.2966 21.6008L21.925 22.2783C21.4142 22.4242 20.9491 22.6979 20.5735 23.0735C20.1978 23.4491 19.9242 23.9142 19.7783 24.425L19.1008 26.7967C19.0634 26.9272 18.9846 27.0419 18.8762 27.1236C18.7678 27.2054 18.6357 27.2496 18.5 27.2496C18.3642 27.2496 18.2322 27.2054 18.1238 27.1236C18.0154 27.0419 17.9365 26.9272 17.8991 26.7967L17.2216 24.425C17.0758 23.9142 16.8021 23.4491 16.4265 23.0735C16.0509 22.6979 15.5857 22.4242 15.075 22.2783L12.7033 21.6008C12.5728 21.5635 12.458 21.4846 12.3763 21.3762C12.2946 21.2678 12.2504 21.1357 12.2504 21C12.2504 20.8643 12.2946 20.7322 12.3763 20.6238C12.458 20.5154 12.5728 20.4366 12.7033 20.3992L15.075 19.7217C15.5857 19.5758 16.0509 19.3021 16.4265 18.9265C16.8021 18.5509 17.0758 18.0858 17.2216 17.575L17.8991 15.2033C17.9364 15.0728 18.0153 14.9579 18.1237 14.8761C18.2321 14.7943 18.3642 14.75 18.5 14.75ZM26 12.25C26.1394 12.2499 26.2749 12.2965 26.3848 12.3822C26.4947 12.468 26.5728 12.5881 26.6066 12.7233L26.8216 13.5867C27.0183 14.37 27.63 14.9817 28.4133 15.1783L29.2766 15.3933C29.4122 15.4269 29.5325 15.5049 29.6186 15.6148C29.7046 15.7248 29.7514 15.8604 29.7514 16C29.7514 16.1396 29.7046 16.2752 29.6186 16.3852C29.5325 16.4951 29.4122 16.5731 29.2766 16.6067L28.4133 16.8217C27.63 17.0183 27.0183 17.63 26.8216 18.4133L26.6066 19.2767C26.5731 19.4122 26.4951 19.5326 26.3851 19.6186C26.2752 19.7047 26.1396 19.7514 26 19.7514C25.8604 19.7514 25.7248 19.7047 25.6148 19.6186C25.5049 19.5326 25.4269 19.4122 25.3933 19.2767L25.1783 18.4133C25.0822 18.0287 24.8833 17.6774 24.6029 17.3971C24.3226 17.1167 23.9713 16.9178 23.5866 16.8217L22.7233 16.6067C22.5878 16.5731 22.4674 16.4951 22.3814 16.3852C22.2953 16.2752 22.2486 16.1396 22.2486 16C22.2486 15.8604 22.2953 15.7248 22.3814 15.6148C22.4674 15.5049 22.5878 15.4269 22.7233 15.3933L23.5866 15.1783C23.9713 15.0822 24.3226 14.8833 24.6029 14.6029C24.8833 14.3226 25.0822 13.9713 25.1783 13.5867L25.3933 12.7233C25.4271 12.5881 25.5052 12.468 25.6152 12.3822C25.7251 12.2965 25.8605 12.2499 26 12.25ZM24.75 23.5C24.8812 23.4999 25.0092 23.5412 25.1157 23.6179C25.2222 23.6946 25.3018 23.803 25.3433 23.9275L25.6716 24.9133C25.7966 25.2858 26.0883 25.5792 26.4616 25.7033L27.4475 26.0325C27.5716 26.0742 27.6795 26.1538 27.756 26.2601C27.8324 26.3664 27.8736 26.4941 27.8736 26.625C27.8736 26.7559 27.8324 26.8836 27.756 26.9899C27.6795 27.0962 27.5716 27.1758 27.4475 27.2175L26.4616 27.5467C26.0891 27.6717 25.7958 27.9633 25.6716 28.3367L25.3425 29.3225C25.3008 29.4466 25.2212 29.5546 25.1149 29.631C25.0086 29.7075 24.8809 29.7486 24.75 29.7486C24.619 29.7486 24.4914 29.7075 24.3851 29.631C24.2788 29.5546 24.1992 29.4466 24.1575 29.3225L23.8283 28.3367C23.7669 28.1527 23.6636 27.9856 23.5265 27.8485C23.3894 27.7114 23.2222 27.6081 23.0383 27.5467L22.0525 27.2175C21.9283 27.1758 21.8204 27.0962 21.744 26.9899C21.6675 26.8836 21.6264 26.7559 21.6264 26.625C21.6264 26.4941 21.6675 26.3664 21.744 26.2601C21.8204 26.1538 21.9283 26.0742 22.0525 26.0325L23.0383 25.7033C23.4108 25.5783 23.7041 25.2867 23.8283 24.9133L24.1575 23.9275C24.1989 23.8031 24.2784 23.6949 24.3848 23.6182C24.4911 23.5414 24.6189 23.5001 24.75 23.5Z" fill="#0F172B" />
        </svg>}
      <div className="flex flex-col flex-1">
        <p className="text-base text-left text-[#0a0a0a] dark:text-white">
          {title}
        </p>
        <p className="text-sm font-light text-left text-neutral-700 dark:text-gray-400 mt-2">
          {description}
        </p>
      </div>
    </div>;
  return href ? <a href={href} className="border-none flex font-normal">
      {cardContent}
    </a> : cardContent;
};

export const GridCards = ({children}) => {
  return <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 md:gap-4 xl:gap-6">
      {children}
    </div>;
};

export const Quickstart = ({}) => {
  return <div className="w-[1081px] h-[307px] relative overflow-hidden rounded-[20px] bg-white border border-[#d9e1ec]">
      <div className="flex justify-start items-center absolute left-[377px] top-4 gap-[3px]">
        <div className="flex justify-center items-center flex-grow-0 flex-shrink-0 relative gap-2.5 px-2 py-0.5 rounded-[100px] bg-slate-100">
          <p className="flex-grow-0 flex-shrink-0 text-xs font-medium text-center text-[#1d293d]">
            python
          </p>
        </div>
        <div className="flex justify-center items-center flex-grow-0 flex-shrink-0 relative gap-2.5 px-2 py-0.5">
          <p className="flex-grow-0 flex-shrink-0 text-xs text-center text-[#707377]">
            typescript
          </p>
        </div>
        <div className="flex flex-col justify-center items-center flex-grow-0 flex-shrink-0 relative gap-2.5 px-2 py-0.5">
          <p className="flex-grow-0 flex-shrink-0 text-xs text-center text-[#707377]">
            curL
          </p>
        </div>
      </div>
      <svg width={26} height={26} viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-[26px] h-[26px] absolute left-[1007px] top-[18px]" preserveAspectRatio="none">
        <foreignobject x={-8} y={-8} width={42} height={42}>
          <div xmlns="http://www.w3.org/1999/xhtml" style={{
    backdropFilter: "blur(4px)",
    clipPath: "url(#bgblur_0_1_167_clip_path)",
    height: "100%",
    width: "100%"
  }} />
        </foreignobject>
        <g data-figma-bg-blur-radius={8}>
          <path d="M17.668 9.66602H11.4457C10.4639 9.66602 9.66797 10.462 9.66797 11.4438V17.666C9.66797 18.6479 10.4639 19.4438 11.4457 19.4438H17.668C18.6498 19.4438 19.4457 18.6479 19.4457 17.666V11.4438C19.4457 10.462 18.6498 9.66602 17.668 9.66602Z" stroke="#9EA1A6" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M7.49078 15.6652L6.57611 9.51052C6.43211 8.53896 7.10233 7.63497 8.073 7.49097L14.2276 6.5763C15.057 6.45274 15.8365 6.92296 16.137 7.66785" stroke="#9EA1A6" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <defs>
          <clippath id="bgblur_0_1_167_clip_path" transform="translate(8 8)">
            <rect width={26} height={26} rx={6} />
          </clippath>
        </defs>
      </svg>
      <svg width={26} height={26} viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-[26px] h-[26px] absolute left-[1039px] top-[18px]" preserveAspectRatio="none">
        <foreignobject x={-8} y={-8} width={42} height={42}>
          <div xmlns="http://www.w3.org/1999/xhtml" style={{
    backdropFilter: "blur(4px)",
    clipPath: "url(#bgblur_0_1_171_clip_path)",
    height: "100%",
    width: "100%"
  }} />
        </foreignobject>
        <g data-figma-bg-blur-radius={8}>
          <path d="M8.1211 6.33486L8.48481 7.42513L8.55512 7.6352L9.88846 8.07965L8.76693 8.45378L8.556 8.52409L8.48568 8.73502L8.11155 9.85568L8.11068 9.85742L7.66536 8.52409L6.33203 8.07965L7.66536 7.6352L7.73568 7.42513L8.09853 6.33486C8.10209 6.33438 8.10646 6.33398 8.11068 6.33398C8.1144 6.334 8.11788 6.33446 8.1211 6.33486Z" stroke="#9EA1A6" stroke-width="0.888889" />
          <path d="M13.4453 7.44434L15.1449 11.7439L19.4453 13.4443L15.1449 15.1448L13.4453 19.4443L11.7449 15.1448L7.44531 13.4443L11.7449 11.7439L13.4453 7.44434Z" stroke="#9EA1A6" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <defs>
          <clippath id="bgblur_0_1_171_clip_path" transform="translate(8 8)">
            <rect width={26} height={26} rx={6} />
          </clippath>
        </defs>
      </svg>
      <div className="w-[688px] h-[228px] absolute left-[377px] top-[57px] overflow-hidden">
        <div className="w-[698px] h-[228px] absolute left-0 top-0 overflow-hidden rounded-lg bg-white">
          <div className="w-[577px] h-[216px] absolute left-[43px] top-[13px]">
            <p className="w-[243.82px] h-[42px] absolute left-2.5 top-[3px] text-sm text-left">
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#cf222e]">
                from
              </span>
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#1f2328]">
                {" "}
                together{" "}
              </span>
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#cf222e]">
                import
              </span>
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#1f2328]">
                {" "}
                Together
              </span>
              <br />
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#1f2328]">
                client{" "}
              </span>
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#cf222e]">
                =
              </span>
              <span className="w-[243.82px] h-[42px] text-sm text-left text-[#1f2328]">
                {" "}
                Together()
              </span>
            </p>
            <p className="w-[625px] absolute left-2.5 top-[72px] text-sm text-left">
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                completion{" "}
              </span>
              <span className="w-[625px] text-sm text-left text-[#cf222e]">
                =
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                {" "}
                client.chat.completions.create(
              </span>
              <br />
              <span className="w-[625px] text-sm text-left text-[#953800]">
                {" "}
                model
              </span>
              <span className="w-[625px] text-sm text-left text-[#cf222e]">
                =
              </span>
              <span className="w-[625px] text-sm text-left text-[#0a3069]">
                "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                ,
              </span>
              <br />
              <span className="w-[625px] text-sm text-left text-[#953800]">
                {" "}
                messages
              </span>
              <span className="w-[625px] text-sm text-left text-[#cf222e]">
                =
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                [{"{"}
              </span>
              <span className="w-[625px] text-sm text-left text-[#0a3069]">
                "role"
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                :{" "}
              </span>
              <span className="w-[625px] text-sm text-left text-[#0a3069]">
                "user"
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                ,{" "}
              </span>
              <span className="w-[625px] text-sm text-left text-[#0a3069]">
                "content"
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                :{" "}
              </span>
              <span className="w-[625px] text-sm text-left text-[#0a3069]">
                "What are the top 3 things to do in New York?"
              </span>
              <span className="w-[625px] text-sm text-left text-[#1f2328]">
                {"}"}],)
              </span>
            </p>
            <p className="w-[369.95px] h-[18px] absolute left-2.5 top-[195px] text-sm text-left">
              <span className="w-[369.95px] h-[18px] text-sm text-left text-[#0550ae]">
                print
              </span>
              <span className="w-[369.95px] h-[18px] text-sm text-left text-[#1f2328]">
                (completion.choices[
              </span>
              <span className="w-[369.95px] h-[18px] text-sm text-left text-[#0550ae]">
                0
              </span>
              <span className="w-[369.95px] h-[18px] text-sm text-left text-[#1f2328]">
                ].message.content)
              </span>
            </p>
          </div>
          <div className="flex flex-col justify-center items-center w-[29px] absolute left-2 top-[3px] gap-2.5 p-2.5">
            <p className="self-stretch flex-grow-0 flex-shrink-0 w-[9px] opacity-20 text-sm text-left text-black">
              123456789
            </p>
          </div>
        </div>
      </div>
      <div className="w-[356px] h-[307px] absolute left-0 top-0 bg-white border-t-0 border-r border-b-0 border-l-0 border-[#d9e1ec]">
        <p className="absolute left-7 top-6 text-base font-medium text-left text-[#171a1e]">
          Developer Quickstart
        </p>
        <p className="w-[293px] absolute left-7 top-[58px] text-sm text-left">
          <span className="w-[293px] text-sm text-left text-[#3e4146]">
            Copy this snippet to get started with our inference API. See our{" "}
          </span>
          <span className="w-[293px] text-sm font-medium text-left text-black">
            full quickstart
          </span>
          <span className="w-[293px] text-sm text-left text-[#3e4146]">
            for more details.
          </span>
        </p>
      </div>
    </div>;
};

export const SubHeading = ({heading, description}) => {
  return <div className="flex flex-col gap-4 xl:flex-row xl:gap-10 mt-16">
      <p className="text-[20px] font-normal text-left text-[#111827] dark:text-white whitespace-nowrap">
        {heading}
      </p>
      <p style={{
    marginTop: "-2px"
  }} className="max-w-[900px] text-base font-light text-left text-[#3e4146] dark:text-gray-400">
        {description}
      </p>
    </div>;
};

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  client = Together()

  completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "What are the top 3 things to do in New York?"}],
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const completion = await together.chat.completions.create({
    model: 'openai/gpt-oss-20b',
    messages: [{ role: 'user', content: 'Top 3 things to do in New York?' }],
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "openai/gpt-oss-20b",
       	"messages": [
            {"role": "user", "content": "What are the top 3 things to do in New York?"}
       	]
  }'
  ```
</CodeGroup>

<GridCards>
  <CtaCard iconUrl="/images/intro/spark.svg" href="/docs/quickstart" title="Run AI models" description="Run leading open source AI models (across chat, image, vision, ect...) with our OpenAI-compatible API." />

  <CtaCard iconUrl="/images/intro/fine-tune.svg" href="/docs/fine-tuning-quickstart" title="Fine-tune models" description="Finetune models on your own data (or bring your own model) and run inference for them on Together" />

  <CtaCard iconUrl="/images/intro/gpu-cluster.svg" href="/docs/instant-clusters" title="Launch a GPU cluster" description="Instantly spin up H100 and B200 clusters with attached storage for training or large batch jobs." />
</GridCards>

<SubHeading heading="Our models:" description="Together hosts many popular models via our serverless endpoints and dedicated endpoints. On serverless, you’ll be charged based on the tokens you use and size of the model. On dedicated, you’ll be charged based on GPU hours." />

<ModelGrid />

<SubHeading heading="Build AI apps and agents with Together:" description="" />

<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 mt-4 ml-[-22px] gap-4">
  {" "}

  <CtaCard iconUrl="/images/intro/agent.svg" href="/docs/how-to-build-coding-agents" title="Build an agent" description="Build agent workflows to solve real use cases with Together" border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/chatbot.svg" href="/docs/nextjs-chat-quickstart" title="Build a Next.js chatbot" description="Spin up a production-ready chatbot using Together + Next.js." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/rag.svg" href="/docs/building-a-rag-workflow" title="Build RAG apps" description="Combine retrieval and generation to build grounded RAG apps." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/image-app.svg" href="https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai?_gl=1*1o6bci4*_gcl_au*MTgxMTcxNDI4OS4xNzQyOTc3MTMx" title="Build a real-time image app" description="Stream real-time image generations with Flux Schnell on Together." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/text-to-app.svg" href="/docs/how-to-build-a-claude-artifacts-clone-with-llama-31-405b" title="Build a text → app workflow" description="Turn natural language into interactive apps with Together + CodeSandbox." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/search-engine.svg" href="/docs/ai-search-engine" title="Build an AI search engine" description="Ship a simplified Perplexity-style search using Together models." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/structured-inputs.svg" href="/docs/json-mode" title="Use structured inputs with LLM’s" description="Get reliable JSON by defining schemas and using structured outputs." border={false} />

  {" "}

  <CtaCard iconUrl="/images/intro/reasoning-models.svg" href="/docs/reasoning-models-guide#reasoning-models-guide" title="Working with reasoning models" description="Use open reasoning models (e.g., DeepSeek-R1) for logic-heavy, multi-step tasks." border={false} />
</div>

<SubHeading heading="Explore our services:" description="" />

<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 mt-4 ml-[-22px] gap-4">
  <CtaCard iconUrl="/images/intro/batch-job.svg" href="/docs/batch-inference" title="Spin up a batch job" description="Queue async generations and fetch results later." border={false} />

  <CtaCard iconUrl="/images/intro/dedicated-instance.svg" href="/docs/dedicated-endpoints-1" title="Run a dedicated instance" description="Provision single-tenant GPUs for predictable, isolated latency." border={false} />

  <CtaCard iconUrl="/images/intro/evals-api.svg" href="/docs/ai-evaluations" title="Use our evals API" description="Automate scoring with LLM judges and reports." border={false} />

  <CtaCard iconUrl="/images/intro/code-execution.svg" href="/docs/code-execution" title="Do code execution with together code sandbox" description="Run Python safely alongside model calls." border={false} />

  <CtaCard iconUrl="/images/intro/byom.svg" href="/docs/custom-models" title="Bring your own model" description="Upload weights and serve them via our API." border={false} />
</div>

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-12">
  <WideCtaCard iconUrl="/images/intro/cookbook.svg" href="https://github.com/togethercomputer/together-cookbook" title="Cookbook" description="Open-source collection of examples and guides." />

  <WideCtaCard iconUrl="/images/intro/example-apps.svg" href="https://together.ai/demos" title="Example apps" description="Full-stack open source Next.js apps built on Together." />

  <WideCtaCard iconUrl="/images/intro/playground.svg" href="https://api.together.xyz/playground" title="Playground" description="Experiment with models and export code." />

  <WideCtaCard iconUrl="/images/intro/models-library.svg" href="/docs/serverless-models" title="Models Library" description="Browse supported models" />
</div>


# Python Library
Source: https://docs.together.ai/python-library





# Create Audio Generation Request
Source: https://docs.together.ai/reference/audio-speech

POST /audio/speech
Generate audio from input text



# Create realtime text-to-speech
Source: https://docs.together.ai/reference/audio-speech-websocket

GET /audio/speech/websocket
Establishes a WebSocket connection for real-time text-to-speech generation. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/audio/speech/websocket) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, voice, max_partial_length)

**Client Events:**
- `tts_session.updated`: Update session parameters like voice
  ```json
  {
    "type": "tts_session.updated",
    "session": {
      "voice": "tara"
    }
  }
  ```
- `input_text_buffer.append`: Send text chunks for TTS generation
  ```json
  {
    "type": "input_text_buffer.append",
    "text": "Hello, this is a test."
  }
  ```
- `input_text_buffer.clear`: Clear the buffered text
  ```json
  {
    "type": "input_text_buffer.clear"
  }
  ```
- `input_text_buffer.commit`: Signal end of text input and process remaining text
  ```json
  {
    "type": "input_text_buffer.commit"
  }
  ```

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "event_id": "evt_123456",
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.tts.session",
      "modalities": ["text", "audio"],
      "model": "hexgrad/Kokoro-82M",
      "voice": "tara"
    }
  }
  ```
- `conversation.item.input_text.received`: Acknowledgment that text was received
  ```json
  {
    "type": "conversation.item.input_text.received",
    "text": "Hello, this is a test."
  }
  ```
- `conversation.item.audio_output.delta`: Audio chunks as base64-encoded data
  ```json
  {
    "type": "conversation.item.audio_output.delta",
    "item_id": "tts_1",
    "delta": "<base64_encoded_audio_chunk>"
  }
  ```
- `conversation.item.audio_output.done`: Audio generation complete for an item
  ```json
  {
    "type": "conversation.item.audio_output.done",
    "item_id": "tts_1"
  }
  ```
- `conversation.item.tts.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.tts.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Text Processing:**
- Partial text (no sentence ending) is held in buffer until:
  - We believe that the text is complete enough to be processed for TTS generation
  - The partial text exceeds `max_partial_length` characters (default: 250)
  - The `input_text_buffer.commit` event is received

**Audio Format:**
- Format: WAV (PCM s16le)
- Sample Rate: 24000 Hz
- Encoding: Base64
- Delivered via `conversation.item.audio_output.delta` events

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Invalid text format errors (400)




# Create an Audio Transcription
Source: https://docs.together.ai/reference/audio-transcriptions

POST /audio/transcriptions
Transcribes audio into text



# Create a realtime audio transcription
Source: https://docs.together.ai/reference/audio-transcriptions-realtime

GET /realtime
Establishes a WebSocket connection for real-time audio transcription. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/realtime) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, input_audio_format)

**Client Events:**
- `input_audio_buffer.append`: Send audio chunks as base64-encoded data
  ```json
  {
    "type": "input_audio_buffer.append",
    "audio": "<base64_encoded_audio_chunk>"
  }
  ```
- `input_audio_buffer.commit`: Signal end of audio stream
  ```json
  {
    "type": "input_audio_buffer.commit"
  }
  ```

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.session",
      "modalities": ["audio"],
      "model": "openai/whisper-large-v3"
    }
  }
  ```
- `conversation.item.input_audio_transcription.delta`: Partial transcription results
  ```json
  {
    "type": "conversation.item.input_audio_transcription.delta",
    "delta": "The quick brown"
  }
  ```
- `conversation.item.input_audio_transcription.completed`: Final transcription
  ```json
  {
    "type": "conversation.item.input_audio_transcription.completed",
    "transcript": "The quick brown fox jumps over the lazy dog"
  }
  ```
- `conversation.item.input_audio_transcription.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.input_audio_transcription.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Unsupported audio format errors (400)




# Create an Audio Translation
Source: https://docs.together.ai/reference/audio-translations

POST /audio/translations
Translates audio into English



# Authentication
Source: https://docs.together.ai/reference/authentication-1



## Creating an Account

Creating an account is a simple process, just head to our [homepage](https://www.together.ai/) and click the **Get Started** button in the top right.

You will then be taken to our sign in page, where you can choose to sign in using Google or Github.

Once you've selected your login provider, you will be prompted to log in using your username/email and password. Then, you'll be taken straight to your [together.ai](http://together.ai/) dashboard!

[together.ai](http://together.ai/) accounts use OAuth (Open Authorisation) for authentication instead of a traditional username/password system. This not only helps keep your account more secure, but means you have one less password to remember!

**Important:** Once you create your account using one of these OAuth providers (Google or GitHub), you must continue using the same provider for all future logins. If you try to sign in with a different provider than the one you originally used, you'll receive an error message stating "This email is already linked to another sign-in method." Make sure to remember which provider you used when first creating your account.

**Note:** LinkedIn authentication was previously available but has been discontinued. If you previously signed up using LinkedIn, you can now access your account by signing in with Google or GitHub using the same email address.

## Getting Your API Key

1. Create an account at [api.together.ai](https://api.together.ai/) or log in if you have one already
2. Tap on the person icon at the top right corner, and click `Settings`
3. On the left side bar, navigate to `API Keys`
4. Copy your API key, and you're ready to go!

## API Key Security

Together does not put any restrictions on what you can do with the API keys assigned to/created by your account.

We recommend that you do not publish your key on any publicly accessible repository or site.

Exercise care when choosing to enter your key on any website or service and only share keys with people that you trust.

Each key generated by your account (and your generated main account key) give you and anybody with those keys full access to your accounts resources, including any available credits, which will top up if you have a recharge mechanism set, and your \$100 negative balance.

If your key is leaked or shared with somebody who uses it beyond the guidelines you set out, Together takes no responsibility for any additional charges or balance due on your account unless our systems are found to be at fault.

If you suspect your API key has been leaked, or want to block an existing key from being used you can rotate your main account key and delete additional keys in your [account settings](https://api.together.ai/settings/api-keys).

### Regenerating Your API Key

If your API key is compromised or you need to change it:

1. Go to your [API Keys settings](https://api.together.xyz/settings/api-keys)
2. Click the triple dot button next to your key
3. Select "Regenerate API key"

This will immediately cancel the existing key and display a new one to use moving forward.

## Inviting Others to Use Your Account

At the moment Together AI only has User Management features available to our GPU Cluster customers.

We can offer username/password logins to our Scale and Enterprise customers as a way of allowing multiple individuals to work from the same account.

If you're on a Build plan, or don't wish to share your credentials you can allow others to use Together AI services via your account by creating and then sharing additional API keys through your account settings.

## Changing Your Email Address

Due to our OAuth authentication system, email addresses cannot be changed directly on existing accounts. However, you can transfer your account to a new email address by following these steps:

1. **Create a new account** using your preferred email address at our sign-up page

2. **Contact our Support team** from your current account email address and provide the new email address

3. **Old account deactivation** - Your original account will be blocked to prevent any confusion

4. **Update integrations** - Make sure to update any API integrations to use your new account's API key

When contacting support, please include your new email address and any relevant account details to help verify your identity.

Once the transfer is complete, you'll be able to access all your previous account features and credits using your new email address.

## Deleting Your Account

You can delete your Together AI account and associated data through our self-service process. This process ensures compliance with data protection regulations including GDPR.

### Steps to Delete Your Account

1. Log in to your Together AI account

2. Navigate to your profile settings at [api.together.xyz/settings/profile](https://api.together.xyz/settings/profile)

3. Scroll down to the "Privacy and Security" section

4. Click the "delete your account" link at the bottom of the page

5. Follow the prompts to confirm account deletion

**Important:** Account deletion will remove all your personal data from our systems and unsubscribe you from all mailing lists. This action cannot be undone. Additionally, due to OAuth authentication, you cannot create a new account using the same email address after deletion - you would need to use a different email address to sign up again.

If you experience any issues with the account deletion process, please contact our support team through the platform and we will assist you promptly.


# Create a batch job
Source: https://docs.together.ai/reference/batch-create

POST /batches
Create a new batch job with the given input file and endpoint



# Get a batch job
Source: https://docs.together.ai/reference/batch-get

GET /batches/{id}
Get details of a batch job by ID



# List all batch jobs
Source: https://docs.together.ai/reference/batch-list

GET /batches
List all batch jobs for the authenticated user



# Chat
Source: https://docs.together.ai/reference/chat



## Query a chat model

To query a chat model, use the `together chat.completions` method.

Use the `--model` option to choose your model, and the `--message` option to pass in a message's role and text:

```sh Shell theme={null}
together chat.completions \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --message "user" "What's 1 + 1?"
```

You can also pass in multiple messages:

```sh Shell theme={null}
together chat.completions \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --message "system" "You are a helpful assistant named Together" \
  --message "user" "What is your name?"
```

## Start an interactive chat

You can start an interactive chat with the `together chat.interactive` method.

Pass in the model using the `--model` option to kick off a new chat:

```sh Shell theme={null}
together chat.interactive \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

## View all commands

To see all the available chat completions commands, run:

```sh Shell theme={null}
together chat.completions --help
```

To see all the available chat interactive commands, run:

```sh Shell theme={null}
together chat.interactive --help
```

***


# Create Chat Completion
Source: https://docs.together.ai/reference/chat-completions-1

POST /chat/completions
Query a chat model.



# Completions
Source: https://docs.together.ai/reference/complete-1



## Run a completion

To run a completion for a language or code model, use the `together completions` method.

Pass the prompt in as the first argument, and use the `--model` option to choose your model:

```sh Shell theme={null}
together completions "Large language models are " \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

## View all commands

To see all the available completions commands, run:

```sh Shell theme={null}
together completions --help
```

***


# Create Completion
Source: https://docs.together.ai/reference/completions-1

POST /completions
Query a language, code, or image model.



# Create Video
Source: https://docs.together.ai/reference/create-videos

POST /videos
Create a video



# Create A Dedicated Endpoint
Source: https://docs.together.ai/reference/createendpoint

POST /endpoints
Creates a new dedicated endpoint for serving models. The endpoint will automatically start after creation. You can deploy any supported model on hardware configurations that meet the model's requirements.



# Delete A File
Source: https://docs.together.ai/reference/delete-files-id

DELETE /files/{id}
Delete a previously uploaded data file.



# Delete A Fine-tuning Event
Source: https://docs.together.ai/reference/delete-fine-tunes-id

DELETE /fine-tunes/{id}
Delete a fine-tuning job.



# Delete Endpoint
Source: https://docs.together.ai/reference/deleteendpoint

DELETE /endpoints/{endpointId}
Permanently deletes an endpoint. This action cannot be undone.



# Create Embedding
Source: https://docs.together.ai/reference/embeddings-2

POST /embeddings
Query an embedding model for a given string of text.



# Endpoints
Source: https://docs.together.ai/reference/endpoints-1

Create, update and delete endpoints via the CLI

## Create

Create a new dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints create [MODEL] [GPU] [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints create \
--model mistralai/Mixtral-8x7B-Instruct-v0.1 \
--gpu h100 \
--gpu-count 2 \
--display-name "My Endpoint" \
--wait
```

### Options

| Options                                             | Description                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| `--model`- TEXT                                     | (required) The model to deploy                                   |
| `--gpu` \[ h100 \| a100 \| l40 \| l40s \| rtx-6000] | (required) GPU type to use for inference                         |
| `--min-replicas`- INTEGER                           | Minimum number of replicas to deploy                             |
| `--max-replicas`- INTEGER                           | Maximum number of replicas to deploy                             |
| `--gpu-count` - INTEGER                             | Number of GPUs to use per replica                                |
| `--display-name`- TEXT                              | A human-readable name for the endpoint                           |
| `--no-prompt-cache`                                 | Disable the prompt cache for this endpoint                       |
| `--no-speculative-decoding`                         | Disable speculative decoding for this endpoint                   |
| `--no-auto-start`                                   | Create the endpoint in STOPPED state instead of auto-starting it |
| `--wait`                                            | Wait for the endpoint to be ready after creation                 |

## Hardware

List all the hardware options, optionally filtered by model.

### Usage

```sh Shell theme={null}
together endpoints hardware [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

### Options

| Options         | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| `--model`- TEXT | Filter hardware options by model                                               |
| `--json`        | Print output in JSON format                                                    |
| `--available`   | Print only available hardware options (can only be used if model is passed in) |

## Get

Print details for a specific endpoint.

### Usage

```sh Shell theme={null}
together endpoints get [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints get endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                 |
| -------- | --------------------------- |
| `--json` | Print output in JSON format |

## Update

Update an existing endpoint by listing the changes followed by the endpoint ID.

You can find the endpoint ID by listing your dedicated endpoints.

### Usage

```sh Shell theme={null}
together endpoints update [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints update --min-replicas 2 --max-replicas 4 endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

Note: Both `--min-replicas` and `--max-replicas` must be specified together

| Options                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| `--display-name` - TEXT    | A new human-readable name for the endpoint    |
| `--min-replicas` - INTEGER | New minimum number of replicas to maintain    |
| `--max-replicas` - INTEGER | New maximum number of replicas to scale up to |

## Start

Start a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints start [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints start endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                    |
| -------- | ------------------------------ |
| `--wait` | Wait for the endpoint to start |

## Stop

Stop a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints stop [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints stop endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                   |
| -------- | ----------------------------- |
| `--wait` | Wait for the endpoint to stop |

## Update

### Usage

Update an existing endpoint by listing the changes followed by the endpoint ID.

You can find the endpoint ID by listing your dedicated endpoints

```sh Shell theme={null}
together endpoints update [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints update --min-replicas 2 --max-replicas 4 endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

Note: Both `--min-replicas` and `--max-replicas` must be specified together

| Options                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| `--display-name` - TEXT    | A new human-readable name for the endpoint    |
| `--min-replicas` - INTEGER | New minimum number of replicas to maintain    |
| `--max-replicas` - INTEGER | New maximum number of replicas to scale up to |

## Delete

Delete a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints delete [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints delete endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

## List

### Usage

```sh Shell theme={null}
together endpoints list [FLAGS]
```

### Example

```sh Shell theme={null}
together endpoints list --type dedicated
```

### Options

| Options                           | Description                 |
| --------------------------------- | --------------------------- |
| `--json`                          | Print output in JSON format |
| `type` \[dedicated \| serverless] | Filter by endpoint type     |

## Help

See all commands with

```sh Shell theme={null}
together endpoints --help
```


# Files
Source: https://docs.together.ai/reference/files



## Upload

To upload a new data file:

```sh Shell theme={null}
together files upload <FILENAME>
```

Here's a sample output:

```sh Shell theme={null}
$ together files upload example.jsonl
Uploading example.jsonl: 100%|██████████████████████████████| 5.18M/5.18M [00:01<00:00, 4.20MB/s]
{
    "filename": "example.jsonl",
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "object": "file"
}
```

The `id` field in the response will be the assigned `file-id` for this file object.

## List

To list previously uploaded files:

```sh Shell theme={null}
together files list
```

## Retrieve

To retrieve the metadata of a previously uploaded file:

```sh Shell theme={null}
together files retrieve <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files retrieve file-d931200a-6b7f-476b-9ae2-8fddd5112308
{
    "filename": "example.jsonl",
    "bytes": 5433223,
    "created_at": 1690432046,
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "purpose": "fine-tune",
    "object": "file",
    "LineCount": 0,
    "Processed": true
}
```

## Retrieve content

To download a previously uploaded file:

```sh Shell theme={null}
together files retrieve-content <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files retrieve-content file-d931200a-6b7f-476b-9ae2-8fddd5112308
Downloading file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl: 100%|██████████| 5.43M/5.43M [00:00<00:00, 10.0MiB/s]
file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl
```

You can specify the output filename with `--output FILENAME` or `-o FILENAME`. By default, the dataset is saved to `<FILE-ID>.jsonl`.

## Delete

To delete a previously uploaded file:

```sh Shell theme={null}
together files delete <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files delete file-d931200a-6b7f-476b-9ae2-8fddd5112308
{
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "object": "file",
    "deleted": "true"
}
```

## Check

To check that a file is in the correct format, you can do this:

Python

```
from together.utils import check_file

report = check_file(file)

print(report)

assert report["is_check_passed"] == True
```

## Help

See all commands with:

```sh Shell theme={null}
together files --help
```

***


# Fine Tuning
Source: https://docs.together.ai/reference/finetune

The  function of the Together Python Library is used to create, manage, and monitor fine-tune jobs.

## Help

See all commands with:

<CodeGroup>
  ```shell shell theme={null}
  together fine-tuning --help
  ```
</CodeGroup>

## Create

To start a new fine-tune job:

<CodeGroup>
  ```shell shell theme={null}
  together fine-tuning create --training-file <FILE-ID> -m <MODEL>
  ```
</CodeGroup>

Other arguments:

* `--model`,`-m` (string, *required*) -- Specifies the base model to fine-tune. (See [the model page](/docs/fine-tuning-models))
* `--training-file`,`-t` (string, *required*) -- Specifies a training file with the file-id of a previously uploaded file (See [Files](/docs/python-files)). The maximum allowed file size is 25GB.
* `--validation-file`,`-t` (string, *optional*) -- Specifies a validation file with the file-id of a previously uploaded file (See [Files](/docs/python-files)). The maximum allowed file size is 25GB.
* `--suffix`,`-s` (string, *optional*) -- Up to 40 characters that will be added to your fine-tuned model name. It is recommended to add this to differentiate fine-tuned models. Default: None.
* `--n-epochs`, `-ne` (integer, *optional*) -- Number of epochs to fine-tune on the dataset. Default: 4, Min: 1, Max: 20.
* `--n-evals` (integer, *optional*) -- Number of evaluations to be run on a given validation set during training. Default: 0, Min: 0, Max: 100.
* `--n-checkpoints`, `-c` (integer, *optional*) -- The number of checkpoints to save during training. Default: 1 One checkpoint is always saved on the last epoch for the trained model. The number of checkpoints must be larger than 0, and equal to or less than the number of epochs (1 \<= n-checkpoints \<= n-epochs). If a larger number is given, the number of epochs will be used for the number of checkpoints.
* `--batch-size`,`-b` (integer, *optional*) -- The batch size to use for each training iteration. The batch size is the number of training samples/examples used in a batch. See [the model page](/docs/fine-tuning-models) for min and max batch sizes for each model. By default `--batch-size max` is used by default when not specified.
* `--learning-rate`, `-lr` (float *optional*) -- The learning rate multiplier to use for training. Default: 0.00001, Min: 0.00000001, Max: 0.01
* `--lr-scheduler-type`, (string, *optional*) -- The learning rate scheduler type. One of `"linear"` or `"cosine"`. Defaults to `"linear"`.
* `--min-lr-ratio`, (float, *optional*) -- The ratio of the final learning rate to the peak learning rate. Default: 0.0, Min: 0.0, Max: 1.0.
* `--scheduler-num-cycles`, (float, *optional*) -- The number or fraction of cycles for the cosine learning rate scheduler. Must be non-negative. Default: 0.5
* `--warmup-ratio` (float, *optional*) -- The percent of steps at the start of training to linearly increase the learning rate. Default 0.0, Min: 0.0, Max: 1.0
* `--max-grad-norm` (float, *optional*) -- Max gradient norm to be used for gradient clipping. Set to 0 to disable. Default: 1.0, Min: 0.0
* `--weight-decay` (float, *optional*) -- Weight Decay parameter for the optimizer. Default: 0.0, Min: 0.0.
* `--wandb-api-key` (string, *optional*) -- Your own Weights & Biases API key. If you provide the key, you can monitor your job progress on your Weights & Biases page. If not set WANDB\_API\_KEY environment variable is used.
* `--wandb-base-url` (string, *optional*) -- The base URL of a dedicated Weights & Biases instance. Leave empty if not using your own Weights & Biases instance.
* `--wandb-project-name` (string, *optional*) -- The Weights & Biases project for your run. If not specified, will use `together` as the project name.
* `--wandb-name` (string, *optional*) -- The Weights & Biases name for your run.
* `--train-on-inputs` (bool or 'auto') -- Whether to mask the user messages in conversational data or prompts in instruction data. `'auto'` will automatically determine whether to mask the inputs based on the data format. For datasets with the `"text"` field (general format), inputs will not be masked. For datasets with the `"messages"` field (conversational format) or `"prompt"` and `"completion"` fields (Instruction format), inputs will be masked. Defaults to "auto".
* `--from-checkpoint` (str, *optional*) -- The checkpoint identifier to continue training from a previous fine-tuning job. The format: `{$JOB_ID/$OUTPUT_MODEL_NAME}:{$STEP}`. The step value is optional, without it the final checkpoint will be used.
* `--from-hf-model` (str, *optional*) -- The Hugging Face Hub repository to start training from. Should be as close as possible to the base model (specified by the `model` argument) in terms of architecture and size
* `--hf-model-revision` (str, *optional*) -- The revision of the Hugging Face Hub model to continue training from. Example: hf\_model\_revision=None (defaults to the latest revision in `main`) or hf\_model\_revision='607a30d783dfa663caf39e06633721c8d4cfcd7e' (specific commit).
* `--hf-api-token` (str, *optional*) -- Hugging Face API token for uploading the output model to a repository on the Hub or using a model from the Hub as initialization.
* `--hf-output-repo-name` (str, *optional*) -- HF repository to upload the fine-tuned model to.

(LoRA arguments are supported with `together >= 1.2.3`)

* `--lora` (bool, *optional*) -- Whether to enable LoRA training. If not provided, full fine-tuning will be applied. Default: False.

* `--lora-r` (integer, *optional*) -- Rank for LoRA adapter weights. Default: 8, Min: 1, Max: 64.

* `--lora-alpha` (integer, *optional*) -- The alpha value for LoRA adapter training. Default: 8. Min: 1. If a value less than 1 is given, it will default to `--lora-r` value to follow the recommendation of 1:1 scaling.

* `--lora-dropout` (float, *optional*) -- The dropout probability for Lora layers. Default: 0.0, Min: 0.0, Max: 1.0.

* `--lora-trainable-modules` (string, \_*optional*) -- A list of LoRA trainable modules, separated by a comma. Default: `all-linear`(using all trainable modules). Trainable modules for each model are:

  * Mixtral 8x7B model family: `k_proj`, `w2`, `w1`, `gate`, `w3`, `o_proj`, `q_proj`, `v_proj`
  * All other models: `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`

The `id` field in the JSON response contains the value for the fine-tune job ID (ft-id) that can be used to get the status, retrieve logs, cancel the job, and download weights.

## List

To list past and running fine-tune jobs:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning list
  ```
</CodeGroup>

The jobs will be sorted oldest-to-newest with the newest jobs at the bottom of the list.

## Retrieve

To retrieve metadata on a job:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning retrieve <FT-ID>
  ```
</CodeGroup>

## Monitor Events

To list events of a past or running job:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning list-events <FT-ID>
  ```
</CodeGroup>

## Cancel

To cancel a running job:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning cancel <FT-ID>
  ```
</CodeGroup>

## Status

To get the status of a job:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning status <FT-ID>
  ```
</CodeGroup>

## Checkpoints

To list saved-checkpoints of a job:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning list-checkpoints <FT-ID>
  ```
</CodeGroup>

## Download Model and Checkpoint Weights

To download the weights of a fine-tuned model, run:

<CodeGroup>
  ```shell Shell theme={null}
  together fine-tuning download <FT-ID>
  ```
</CodeGroup>

This command will download ZSTD compressed weights of the model. To extract the weights, run `tar -xf filename`.

Other arguments:

* `--output`,`-o` (filename, *optional*) -- Specify the output filename. Default: `<MODEL-NAME>.tar.zst`
* `--step`,`-s` (integer, *optional*) -- Download a specific checkpoint's weights. Defaults to download the latest weights. Default: `-1`


# Get Evaluation
Source: https://docs.together.ai/reference/get-evaluation

GET /evaluation/{id}
Get details of a specific evaluation job



# Get Evaluation Status
Source: https://docs.together.ai/reference/get-evaluation-status

GET /evaluation/{id}/status
Get the status and results of a specific evaluation job



# List All Files
Source: https://docs.together.ai/reference/get-files

GET /files
List the metadata for all uploaded data files.



# List File
Source: https://docs.together.ai/reference/get-files-id

GET /files/{id}
List the metadata for a single uploaded data file.



# Get File Contents
Source: https://docs.together.ai/reference/get-files-id-content

GET /files/{id}/content
Get the contents of a single uploaded data file.



# List All Jobs
Source: https://docs.together.ai/reference/get-fine-tunes

GET /fine-tunes
List the metadata for all fine-tuning jobs. Returns a list of FinetuneResponseTruncated objects.



# List Job
Source: https://docs.together.ai/reference/get-fine-tunes-id

GET /fine-tunes/{id}
List the metadata for a single fine-tuning job.



# List checkpoints
Source: https://docs.together.ai/reference/get-fine-tunes-id-checkpoint

GET /fine-tunes/{id}/checkpoints
List the checkpoints for a single fine-tuning job.



# List Job Events
Source: https://docs.together.ai/reference/get-fine-tunes-id-events

GET /fine-tunes/{id}/events
List the events for a single fine-tuning job.



# Download Model
Source: https://docs.together.ai/reference/get-finetune-download

GET /finetune/download
Download a compressed fine-tuned model or checkpoint to local disk.



# Get Video
Source: https://docs.together.ai/reference/get-videos-id

GET /videos/{id}
Fetch video metadata



# Get Endpoint By ID
Source: https://docs.together.ai/reference/getendpoint

GET /endpoints/{endpointId}
Retrieves details about a specific endpoint, including its current state, configuration, and scaling settings.



# Images
Source: https://docs.together.ai/reference/image-1



## Generate an image

To generate an image, use the `together images generate` method.

Pass the prompt in as the first argument, and use the `--model` option to choose your model:

```sh Shell theme={null}
together images generate \
  "space robots" \
  --model black-forest-labs/FLUX.1-dev
```

The image is opened in the default image viewer by default. To disable this, use `--no-show`.

## View all commands

To see all the available images commands, run:

```sh Shell theme={null}
together images generate --help
```

***


# Installation
Source: https://docs.together.ai/reference/installation



The Together Python library comes with a command-line interface you can use to query Together's open-source models, upload new data files to your account, or manage your account's fine-tune jobs.

## Prerequisites

* Make sure your local machine has [Python](https://www.python.org/) installed.
* If you haven't already, [register for a Together account](https://api.together.xyz/settings/api-keys) to get an API key.

## Install the library

Launch your terminal and install or update the Together CLI with the following command:

```sh Shell theme={null}
pip install --upgrade together
```

## Authenticate your shell

The CLI relies on the `TOGETHER_API_KEY` environment variable being set to your account's API token to authenticate requests. You can find your API token in your [account settings](https://api.together.xyz/settings/api-keys).

Tocreate an environment variable in the current shell, run:

```sh Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

You can also add it to your shell's global configuration so all new sessions can access it. Different shells have different semantics for setting global environment variables, so see your preferred shell's documentation to learn more.

## Next steps

If you know what you're looking for, find your use case in the sidebar to learn more! The CLI is primarily used for fine-tuning so we recommend visiting **[Files](/reference/files)** or **[Fine-tuning](/reference/finetune)**.

To see all commands available in the CLI, run:

```sh Shell theme={null}
together --help
```


# List Evaluation Models
Source: https://docs.together.ai/reference/list-evaluation-models

GET /evaluations/model-list
Get the list of models that are allowed for evaluation



# List All Evaluations
Source: https://docs.together.ai/reference/list-evaluations

GET /evaluations
Get a list of evaluation jobs with optional filtering



# List All Endpoints
Source: https://docs.together.ai/reference/listendpoints

GET /endpoints
Returns a list of all endpoints associated with your account. You can filter the results by type (dedicated or serverless).



# List Available Hardware Configurations
Source: https://docs.together.ai/reference/listhardware

GET /hardware
Returns a list of available hardware configurations for deploying models. When a model parameter is provided, it returns only hardware configurations compatible with that model, including their current availability status.




# List All Models
Source: https://docs.together.ai/reference/models-1

GET /models
Lists all of Together's open-source models



# Models
Source: https://docs.together.ai/reference/models-5



## List all models

To list all the available models, run `together models list`:

```sh Bash theme={null}
# List models
together models list
```

## View all commands

To see all the available chat commands, run:

```sh Shell theme={null}
together models --help
```


# Abort multipart upload
Source: https://docs.together.ai/reference/post-files-multipart-abort

POST /files/multipart/abort
Abort a multipart upload and clean up any uploaded parts.



# Complete multipart upload
Source: https://docs.together.ai/reference/post-files-multipart-complete

POST /files/multipart/complete
Complete a multipart upload by providing ETags for all uploaded parts.



# Initiate multipart upload
Source: https://docs.together.ai/reference/post-files-multipart-initiate

POST /files/multipart/initiate
Initiate a multipart upload for large files (>5GB) with presigned URLs for each part.



# Create Job
Source: https://docs.together.ai/reference/post-fine-tunes

POST /fine-tunes
Create a fine-tuning job with the provided model and training data.



# Cancel Job
Source: https://docs.together.ai/reference/post-fine-tunes-id-cancel

POST /fine-tunes/{id}/cancel
Cancel a currently running fine-tuning job. Returns a FinetuneResponseTruncated object.



# Create Image
Source: https://docs.together.ai/reference/post-images-generations

POST /images/generations
Use an image model to generate an image for a given prompt.



# Create A Rerank Request
Source: https://docs.together.ai/reference/rerank-1

POST /rerank
Query a reranker model



# /tci/execute
Source: https://docs.together.ai/reference/tci-execute

POST /tci/execute
Executes the given code snippet and returns the output. Without a session_id, a new session will be created to run the code. If you do pass in a valid session_id, the code will be run in that session. This is useful for running multiple code snippets in the same environment, because dependencies and similar things are persisted
between calls to the same session.




# /tci/sessions
Source: https://docs.together.ai/reference/tci-sessions

GET /tci/sessions
Lists all your currently active sessions.




# Update, Start or Stop Endpoint
Source: https://docs.together.ai/reference/updateendpoint

PATCH /endpoints/{endpointId}
Updates an existing endpoint's configuration. You can modify the display name, autoscaling settings, or change the endpoint's state (start/stop).



# Upload a file
Source: https://docs.together.ai/reference/upload-file

POST /files/upload
Upload a file with specified purpose, file name, and file type.



# Upload a custom model or adapter
Source: https://docs.together.ai/reference/upload-model

POST /models
Upload a custom model or adapter from Hugging Face or S3



# TypeScript Library
Source: https://docs.together.ai/typescript-library






---

**Navigation:** [← Previous](./08-speech-to-text.md) | [Index](./index.md) | Next →
