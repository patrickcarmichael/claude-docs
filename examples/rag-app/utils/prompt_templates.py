"""
Prompt Templates for RAG Application

Defines system prompts and templates used throughout the RAG system.
These can be customized for different use cases.
"""

from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema import SystemMessage

import config


def get_qa_prompt() -> PromptTemplate:
    """
    Get the main Q&A prompt template.

    This prompt is used when retrieving context and generating answers.
    It instructs Claude to use the provided context and cite sources.
    """
    template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Always cite your sources using the document metadata when relevant.

Context:
{context}

Question: {question}

Helpful Answer:"""

    return PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )


def get_condensed_question_prompt() -> PromptTemplate:
    """
    Get the prompt for condensing follow-up questions in conversations.

    In multi-turn conversations, this reformulates questions to include
    previous context so the retriever can find relevant documents.
    """
    template = """Given the following conversation and a follow up question,
rephrase the follow up question to be a standalone question, in its original language.

Chat History:
{chat_history}

Follow Up Input: {question}

Standalone question:"""

    return PromptTemplate(
        input_variables=["chat_history", "question"],
        template=template
    )


def get_system_prompt() -> SystemMessage:
    """Get the system message for Claude."""
    return SystemMessage(
        content="""You are a knowledgeable AI assistant with access to a comprehensive knowledge base.
Your role is to:
1. Answer user questions accurately using the provided context
2. Cite sources when you reference specific information
3. Acknowledge when you don't have relevant information
4. Provide clear, well-structured responses
5. Ask clarifying questions if the user's query is ambiguous

Always prioritize accuracy over completeness. If the context doesn't contain
relevant information, say so explicitly rather than speculating."""
    )


def get_document_qa_prompt() -> PromptTemplate:
    """
    Get a prompt specialized for document Q&A.

    Use this for detailed questions about documents with focus on
    extracting specific information rather than generating creative content.
    """
    template = """You are a document analysis expert. Based on the following context from documents,
answer the user's question with precision and cite specific locations in the documents.

Context:
{context}

Question: {question}

Detailed Answer with Citations:"""

    return PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )


def get_summarization_prompt() -> PromptTemplate:
    """
    Get a prompt for summarizing retrieved documents.

    Use this when you want to provide a summary rather than answer a specific question.
    """
    template = """Summarize the following context in a clear, concise manner.
Include key points and important details.

Context:
{context}

Summary:"""

    return PromptTemplate(
        input_variables=["context"],
        template=template
    )


def get_chat_prompt() -> ChatPromptTemplate:
    """
    Get a chat-based prompt template for conversational AI.

    This format is optimized for Claude's chat API.
    """
    system_message = SystemMessagePromptTemplate.from_template(
        """You are a helpful AI assistant with access to a knowledge base.
Use the provided context to answer questions accurately.
If context doesn't have relevant information, say so explicitly."""
    )

    human_message = HumanMessagePromptTemplate.from_template(
        """Context:
{context}

Question: {question}"""
    )

    return ChatPromptTemplate.from_messages([system_message, human_message])


def get_retrieval_prompt() -> PromptTemplate:
    """
    Get a prompt for improving retrieval relevance.

    This can be used with a reranker to improve document retrieval quality.
    """
    template = """Based on the following question, determine how relevant each document is.
Provide a relevance score from 0-10.

Question: {question}

Document:
{document}

Relevance Score (0-10):"""

    return PromptTemplate(
        input_variables=["question", "document"],
        template=template
    )


# Specialized templates for different domains

LEGAL_SYSTEM_PROMPT = """You are an AI legal assistant with access to legal documents and case law.
When answering legal questions:
1. Cite specific legal statutes and case law
2. Explain the applicability to the user's situation
3. Recommend consulting with a real attorney for specific legal advice
4. Always disclaim that you're not providing legal advice"""

MEDICAL_SYSTEM_PROMPT = """You are a medical information assistant with access to medical resources.
When providing medical information:
1. Always recommend consulting with healthcare professionals
2. Provide evidence-based information only
3. Clearly state this is for informational purposes only
4. Never provide diagnosis or treatment recommendations"""

TECHNICAL_SYSTEM_PROMPT = """You are a technical documentation expert with access to API docs and technical guides.
When answering technical questions:
1. Provide code examples when relevant
2. Link to official documentation
3. Explain concepts clearly for different skill levels
4. Suggest best practices and common pitfalls"""


def get_custom_system_prompt(domain: str = "general") -> SystemMessage:
    """
    Get a domain-specific system prompt.

    Args:
        domain: One of 'general', 'legal', 'medical', 'technical'

    Returns:
        SystemMessage with appropriate instructions
    """
    prompts = {
        "legal": LEGAL_SYSTEM_PROMPT,
        "medical": MEDICAL_SYSTEM_PROMPT,
        "technical": TECHNICAL_SYSTEM_PROMPT,
        "general": config.get_system_prompt()
    }

    prompt_text = prompts.get(domain.lower(), prompts["general"])
    return SystemMessage(content=prompt_text)


if __name__ == "__main__":
    # Example: Print available prompts
    print("Q&A Prompt:")
    print(get_qa_prompt().template)
    print("\n" + "="*60 + "\n")

    print("Condensed Question Prompt:")
    print(get_condensed_question_prompt().template)
    print("\n" + "="*60 + "\n")

    print("System Prompt:")
    print(get_system_prompt().content)
