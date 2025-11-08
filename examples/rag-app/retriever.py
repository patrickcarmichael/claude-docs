"""
RAG Retriever Module

Handles document retrieval and question-answering using LangChain,
Pinecone, and Anthropic Claude.

This module provides the core RAG functionality:
- Initialize vector store connection
- Create retrieval chains
- Execute queries with context
"""

import logging
from typing import List, Optional, Tuple

from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document, BaseRetriever
from langchain.vectorstores import Pinecone
from langchain_anthropic import ChatAnthropic
from langchain.embeddings.openai import OpenAIEmbeddings
from pinecone import Pinecone as PineconeClient

import config
from utils.prompt_templates import get_qa_prompt, get_condensed_question_prompt

logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class RAGRetriever:
    """
    Retrieval-Augmented Generation using LangChain, Pinecone, and Claude.

    This class manages:
    - Connection to Pinecone vector store
    - Document retrieval
    - LLM integration with Claude
    - Conversational memory management
    """

    def __init__(self):
        """Initialize the RAG retriever with vector store and LLM."""
        logger.info("Initializing RAG Retriever...")

        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            openai_api_key=config.OPENAI_API_KEY
        )

        # Initialize Pinecone client
        self.pc = PineconeClient(
            api_key=config.PINECONE_API_KEY,
            environment=config.PINECONE_ENVIRONMENT
        )

        # Get vector store
        self.vectorstore = Pinecone(
            index_name=config.PINECONE_INDEX_NAME,
            embedding_function=self.embeddings.embed_query
        )

        # Initialize Claude LLM
        self.llm = ChatAnthropic(
            model=config.CLAUDE_MODEL,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
            anthropic_api_key=config.ANTHROPIC_API_KEY
        )

        # Initialize retriever
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={
                "k": config.MAX_RETRIEVED_DOCS,
                "search_type": config.RETRIEVAL_SEARCH_TYPE
            }
        )

        logger.info("RAG Retriever initialized successfully")

    def query(
        self,
        question: str,
        return_source_documents: bool = True,
        verbose: bool = False
    ) -> dict:
        """
        Execute a single query against the knowledge base.

        Args:
            question: The user's question
            return_source_documents: Whether to return source documents
            verbose: Enable verbose output

        Returns:
            Dictionary with 'answer' and optionally 'source_documents'
        """
        logger.info(f"Processing query: {question}")

        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # Stuff all docs into one prompt
            retriever=self.retriever,
            return_source_documents=return_source_documents,
            verbose=verbose,
            chain_type_kwargs={
                "prompt": get_qa_prompt(),
            }
        )

        # Execute query
        result = qa_chain({"query": question})

        logger.info(f"Query processed successfully")
        return result

    def create_conversation_chain(self) -> ConversationalRetrievalChain:
        """
        Create a conversational retrieval chain with memory.

        Useful for multi-turn conversations where context is maintained.

        Returns:
            ConversationalRetrievalChain instance
        """
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            memory=memory,
            verbose=False,
            condense_question_prompt=get_condensed_question_prompt(),
            chain_type="stuff"
        )

        logger.info("Conversational chain created")
        return qa_chain

    def retrieve_documents(
        self,
        query: str,
        k: Optional[int] = None
    ) -> List[Document]:
        """
        Retrieve relevant documents without generating an answer.

        Useful for inspection and debugging.

        Args:
            query: Search query
            k: Number of documents to retrieve (uses config default if None)

        Returns:
            List of relevant Document objects
        """
        k = k or config.MAX_RETRIEVED_DOCS

        logger.info(f"Retrieving {k} documents for query: {query}")
        docs = self.retriever.get_relevant_documents(query)[:k]

        logger.info(f"Retrieved {len(docs)} documents")
        return docs

    def similarity_search(
        self,
        query: str,
        k: Optional[int] = None
    ) -> List[Tuple[Document, float]]:
        """
        Perform similarity search and return documents with scores.

        Args:
            query: Search query
            k: Number of results (uses config default if None)

        Returns:
            List of (Document, similarity_score) tuples
        """
        k = k or config.MAX_RETRIEVED_DOCS

        logger.info(f"Similarity search for query: {query}")
        results = self.vectorstore.similarity_search_with_score(query, k=k)

        return results

    def batch_query(
        self,
        questions: List[str],
        return_source_documents: bool = True
    ) -> List[dict]:
        """
        Process multiple queries in batch.

        Args:
            questions: List of questions to process
            return_source_documents: Whether to return source documents

        Returns:
            List of result dictionaries
        """
        logger.info(f"Processing {len(questions)} queries in batch")

        results = []
        for i, question in enumerate(questions, 1):
            logger.info(f"[{i}/{len(questions)}] Processing: {question}")
            result = self.query(question, return_source_documents)
            results.append(result)

        logger.info(f"Batch processing complete")
        return results

    def get_index_stats(self) -> dict:
        """
        Get statistics about the Pinecone index.

        Returns:
            Dictionary with index information
        """
        try:
            index = self.pc.Index(config.PINECONE_INDEX_NAME)
            stats = index.describe_index_stats()
            return {
                "index_name": config.PINECONE_INDEX_NAME,
                "dimension": stats.dimension,
                "index_fullness": stats.index_fullness,
                "total_vector_count": stats.total_vector_count
            }
        except Exception as e:
            logger.error(f"Error getting index stats: {e}")
            return {}


# Convenience functions

def create_retriever() -> RAGRetriever:
    """Factory function to create a RAGRetriever instance."""
    return RAGRetriever()


def quick_query(question: str) -> str:
    """
    Quick convenience function for single queries.

    Usage:
        answer = quick_query("What is Claude?")
        print(answer)
    """
    retriever = RAGRetriever()
    result = retriever.query(question, return_source_documents=False)
    return result["result"]


if __name__ == "__main__":
    # Example usage
    retriever = RAGRetriever()

    # Print index stats
    print("Index Stats:")
    print(retriever.get_index_stats())

    # Example query
    question = "What is Claude Code?"
    print(f"\nQuestion: {question}")
    result = retriever.query(question)
    print(f"Answer: {result['result']}")
    if result.get('source_documents'):
        print("\nSources:")
        for doc in result['source_documents']:
            print(f"  - {doc.metadata.get('source', 'Unknown')}")
