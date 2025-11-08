---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Style Guide

Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""
        self.n_jobs=10 #number of parallel processes to run summarization of chunks
        self.extract_images_in_pdf=False
        self.infer_table_structure=True
        self.chunking_strategy="by_title"
        self.max_characters=4000
        self.new_after_n_chars=3800
        self.combine_text_under_n_chars=2000
        self.image_output_dir_path='.'
        self.paths = paths
        self.parse_and_build_retriever()

    def parse_and_build_retriever(self,):
        #step1, parse pdfs
        # if condition just for debugging since perf_audit.pdf is parsed in the prev step, no need to rerun

        parsed_pdf_list=self.parse_pdfs(self.paths)
        #separate tables and text
        extracted_tables, extracted_text = self.extract_text_and_tables(parsed_pdf_list)
        #generate summaries for everything
        tables, table_summaries, texts, text_summaries=self.generate_summaries(extracted_tables,extracted_text)
        self.tables = tables
        self.table_summaries = table_summaries
        self.texts = texts
        self.text_summaries=text_summaries
        #setup the multivector retriever
        self.make_retriever(tables, table_summaries, texts, text_summaries)

    def extract_text_and_tables(self,parsed_pdf_list):
        # extract table and textual objects from parser

        # Categorize by type

        all_table_elements = []
        all_text_elements = []
        for raw_pdf_elements in parsed_pdf_list:
            categorized_elements = []
            for element in raw_pdf_elements:
                if "unstructured.documents.elements.Table" in str(type(element)):
                    categorized_elements.append(Element(type="table", text=str(element)))
                elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
                    categorized_elements.append(Element(type="text", text=str(element)))

            # Tables

            table_elements = [e for e in categorized_elements if e.type == "table"]
            print(len(table_elements))

            # Text

            text_elements = [e for e in categorized_elements if e.type == "text"]
            print(len(text_elements))
            all_table_elements.extend(table_elements)
            all_text_elements.extend(text_elements)

        return all_table_elements, all_text_elements

    def parse_pdfs(self, paths):

        path_raw_elements = []
        for path in paths:
            raw_pdf_elements = partition_pdf(
            filename=path,
            # Unstructured first finds embedded image blocks

            extract_images_in_pdf=self.extract_images_in_pdf,
            # Use layout model (YOLOX) to get bounding boxes (for tables) and find titles

            # Titles are any sub-section of the document

            infer_table_structure=self.infer_table_structure,
            # Post processing to aggregate text once we have the title

            chunking_strategy=self.chunking_strategy,
            # Chunking params to aggregate text blocks

            # Attempt to create a new chunk 3800 chars

            # Attempt to keep chunks > 2000 chars

            max_characters=self.max_characters,
            new_after_n_chars=self.new_after_n_chars,
            combine_text_under_n_chars=self.combine_text_under_n_chars,
            image_output_dir_path=self.image_output_dir_path,
            )
            path_raw_elements.append(raw_pdf_elements)
        print('PDFs parsed')
        return path_raw_elements


    def get_chat_output(self,message, preamble, model, temp):
        # print("**message")

        # print(message)

        response=co.chat(
            message=message,
            preamble=preamble,
            model=model,
            temperature=temp
            ).text
        # print("**output")

        # print(response)

        return response

    def parallel_proc_chat(self,prompts,preamble,model,temp,n_jobs):
        """Parallel processing of chat endpoint calls."""
        responses = Parallel(n_jobs=n_jobs, prefer="threads")(delayed(self.get_chat_output)(prompt,preamble,model,temp) for prompt in prompts)
        return responses

    def rerank_cohere(self,query, returned_documents,model, top_n):
        response = co.rerank(
            query=query,
            documents=returned_documents,
            top_n=top_n,
            model=model,
            return_documents=True
        )
        top_chunks_after_rerank = [results.document.text for results in response.results]
        return top_chunks_after_rerank

    def generate_summaries(self,table_elements,text_elements):
        # generate table and text summaries

        summarize_prompt = """You are an assistant tasked with summarizing tables and text. \
        Give a concise summary of the table or text. Table or text chunk: {element}. Only provide the summary and no other text."""

        table_prompts = [summarize_prompt.format(element=i.text) for i in table_elements]
        table_summaries = self.parallel_proc_chat(table_prompts,self.preamble,self.summary_model,self.temperature,self.n_jobs)
        text_prompts = [summarize_prompt.format(element=i.text) for i in text_elements]
        text_summaries = self.parallel_proc_chat(text_prompts,self.preamble,self.summary_model,self.temperature,self.n_jobs)
        tables = [i.text for i in table_elements]
        texts = [i.text for i in text_elements]
        print('summaries generated')
        return tables, table_summaries, texts, text_summaries

    def make_retriever(self,tables, table_summaries, texts, text_summaries):
        # The vectorstore to use to index the child chunks

        vectorstore = Chroma(collection_name="summaries", embedding_function=CohereEmbeddings())
        # The storage layer for the parent documents

        store = InMemoryStore()
        id_key = "doc_id"
        # The retriever (empty to start)

        retriever = MultiVectorRetriever(
            vectorstore=vectorstore,
            docstore=store,
            id_key=id_key,
            search_kwargs={"k": self.num_docs_to_retrieve}
        )
        # Add texts

        doc_ids = [f'text_{i}' for i in range(len(texts))]#[str(uuid.uuid4()) for _ in texts]
        summary_texts = [
            Document(page_content=s, metadata={id_key: doc_ids[i]})
            for i, s in enumerate(text_summaries)
        ]
        retriever.vectorstore.add_documents(summary_texts,ids=doc_ids)
        retriever.docstore.mset(list(zip(doc_ids, texts)))
        # Add tables

        table_ids = [f'table_{i}' for i in range(len(texts))]#[str(uuid.uuid4()) for _ in tables]
        summary_tables = [
            Document(page_content=s, metadata={id_key: table_ids[i]})
            for i, s in enumerate(table_summaries)
        ]
        retriever.vectorstore.add_documents(summary_tables,ids=table_ids)
        retriever.docstore.mset(list(zip(table_ids, tables)))
        self.retriever = retriever
        print('retriever built')

    def process_query(self,query):
        """Runs query augmentation, retrieval, rerank and generation in one call."""
        augmented_queries=co.chat(message=query,model=self.generation_model,temperature=self.temperature, search_queries_only=True)
        #augment queries
        if augmented_queries.search_queries:
            reranked_docs=[]
            for itm in augmented_queries.search_queries:
                docs=self.retriever.invoke(itm.text)
                temp_rerank = self.rerank_cohere(itm.text,docs,model=self.rerank_model,top_n=self.top_k_rerank)
                reranked_docs.extend(temp_rerank)
            documents = [{"title": f"chunk {i}", "snippet": reranked_docs[i]} for i in range(len(reranked_docs))]
        else:
            documents = None

        response = co.chat(
          message=query,
          documents=documents,
          preamble=self.preamble,
          model=self.generation_model,
          temperature=self.temperature
        )

        final_answer_docs="""The final answer is from the documents below:

        {docs}""".format(docs=str(response.documents))

        final_answer = response.text
        return final_answer, final_answer_docs
```
```python PYTHON
rag_object=RAG_pipeline(paths=["city_ny_popular_fin_report.pdf"])
```
This function will be deprecated in a future release and `unstructured` will simply use the DEFAULT\_MODEL from `unstructured_inference.model.base` to set default model name
```txt title="Output"
PDFs parsed
14
24
summaries generated
retriever built
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
