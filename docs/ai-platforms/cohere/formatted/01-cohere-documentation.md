---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

# Cohere Documentation

> Cohere's API documentation helps developers easily integrate natural language processing and generation into their products.

export const LandingPageCard = ({ href, title, imgSrc, description }) => (
  <div className="rounded-lg bg-[#F5F4F2] dark:bg-[#0F0F0F] px-6 py-5 hover:bg-[#E9E6DE] dark:hover:bg-[#292929] md:p-8">
    <a
      href={href}
      target="_self"
      className="flex h-full flex-col justify-between"
      style={{ textDecoration: 'none' }}
    >
      <div className="mb-5 flex flex-col justify-between gap-5">
        <h2 className="lg:min-h-20 [@media(min-width:1181px)]:min-h-0">
          {title}
        </h2>
        <img src={imgSrc} alt={title} />
        <p className="p-lg">{description}</p>
      </div>
      <div className="mt-2 text-sm text-[#2D4CB9] dark:text-[#4C6EE6] md:mt-0 md:self-end">
        {"GET STARTED"}
        <div className="ml-2 inline-block group-hover:no-underline">
          <svg
            width="12"
            height="11"
            viewBox="0 0 12 11"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            style={{ transform: "rotate(-90deg)" }}
          >
            <path
              d="M6 10.75L0.75 5.31686L1.74907 4.27907L5.2556 8.00291L5.2556 0.25L6.7444 0.25L6.7444 8.00291L10.2509 4.27907L11.25 5.31686L6 10.75Z"
              fill="currentColor"
            ></path>
          </svg>
        </div>
      </div>
    </a>
  </div>
);

export const EndpointLink = ({ href, title }) => (
  <a
    href={href}
    className="group flex cursor-pointer flex-row text-sm !font-normal text-[#2D4CB9] dark:text-[#4C6EE6]"
    rel="noreferrer"
    target="_self"
  >
    {title}
    <span className="duration-400 flex items-center transition-all ease-in-out group-hover:pl-1 group-hover:pr-2">
      <div className="ml-2 inline-block text-sm !text-[#2D4CB9] group-hover:no-underline">
        <svg
          width="12"
          height="11"
          viewBox="0 0 12 11"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          style={{ transform: "rotate(-90deg)" }}
        >
          <path
            d="M6 10.75L0.75 5.31686L1.74907 4.27907L5.2556 8.00291L5.2556 0.25L6.7444 0.25L6.7444 8.00291L10.2509 4.27907L11.25 5.31686L6 10.75Z"
            fill="currentColor"
          ></path>
        </svg>
      </div>
    </span>
  </a>
);

export const cards = [
  {
    href: "/docs",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8da77c9-Frame_138972.png",
    title: "Guides and concepts",
    description:
      "Understand how to use our API on a deeper level. Train and customize the model to work for you.",
  },
  {
    href: "/reference/about",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8ff146a-Group_138977.png",
    title: "API reference",
    description:
      "Integrate natural language processing and generation into your products with a few lines of code.",
  },
  {
    href: "/release-notes",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d51d176-Group_138977_1.png",
    title: "Release notes",
    description:
      "Keep up with the latest releases and platform updates from Cohere.",
  },
  {
    href: "/page/cookbooks",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/7fca92c-Group_138977_2.png",
    title: "Cookbooks",
    description:
      "A collection of resources to help developers get up and running with Cohere.",
  },
];

export const endpoints = [
  {
    href: "/reference/chat",
    title: "/CHAT",
  },
  {
    href: "/reference/embed",
    title: "/EMBED",
  },
  {
    href: "/reference/rerank",
    title: "/RERANK",
  },
];

<div>
  <div>
    {cards.map((card) => (
          <LandingPageCard
            key={card.href}
            href={card.href}
            imgSrc={card.imgSrc}
            title={card.title}
            description={card.description}
          />
        ))}

    <div>
      <div>
        <div>
          <h2>
            Endpoints
          </h2>

          <p>
            Our endpoints offer different ways to interact with our models and
            offer additional value on top of them
          </p>
        </div>

        <div>
          {endpoints.map((endpoint) => (
                      <EndpointLink key={endpoint.href} {...endpoint} />
                    ))}
        </div>
      </div>

      <div>
        <a href="https://cohere.com/llmu" target="_blank">
          <div>
            <div>
              <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/9d0694c-Symbol.svg" alt="" />

              <h2>
                LLM University
              </h2>
            </div>

            <p>
              Join our learning hub to master Enterprise AI with expert-led
              courses and step-by-step guides
            </p>
          </div>

          <div>
            <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/64d7b4f-Group_138975.png" alt="" />
          </div>
        </a>
      </div>
    </div>
  </div>

  <div>
    <a href="https://cohere.com/llmu" target="_blank">
      <div>
        <div>
          <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/9d0694c-Symbol.svg" alt="" />

          <h2>
            LLM University
          </h2>
        </div>

        <p>
          New to NLP? Learn about Natural Language processing and Large Language
          Models through our structured curriculum.
        </p>
      </div>
    </a>
  </div>
</div>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
