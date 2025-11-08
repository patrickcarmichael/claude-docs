---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

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
```python
  from together import Together
  client = Together()

  completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "What are the top 3 things to do in New York?"}],
  )

  print(completion.choices[0].message.content)
```
```typescript
  import Together from 'together-ai';
  const together = new Together();

  const completion = await together.chat.completions.create({
    model: 'openai/gpt-oss-20b',
    messages: [{ role: 'user', content: 'Top 3 things to do in New York?' }],
  });

  console.log(completion.choices[0].message.content);
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "openai/gpt-oss-20b",
       	"messages": [
            {"role": "user", "content": "What are the top 3 things to do in New York?"}
       	]
  }'
```typescript

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


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
