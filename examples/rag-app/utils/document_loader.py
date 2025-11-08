"""
Document Loader Utilities

Handles loading documents from various file formats (PDF, MD, TXT, DOCX)
and preparing them for ingestion into the vector store.
"""

import os
import logging
from pathlib import Path
from typing import List, Optional

from langchain.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
)
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

import config

logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """
    Handles loading, splitting, and preprocessing documents.

    Supports multiple file formats:
    - PDF (.pdf)
    - Markdown (.md)
    - Plain text (.txt)
    - Word documents (.docx)
    """

    def __init__(
        self,
        chunk_size: int = config.CHUNK_SIZE,
        chunk_overlap: int = config.CHUNK_OVERLAP
    ):
        """
        Initialize document processor.

        Args:
            chunk_size: Size of text chunks in characters
            chunk_overlap: Overlap between chunks in characters
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

        logger.info(f"DocumentProcessor initialized (chunk_size={chunk_size})")

    def load_from_directory(
        self,
        directory_path: str,
        extensions: Optional[List[str]] = None,
        glob_pattern: str = "**/*"
    ) -> List[Document]:
        """
        Load documents from a directory recursively.

        Args:
            directory_path: Path to directory containing documents
            extensions: List of file extensions to include (e.g., ['.pdf', '.md'])
            glob_pattern: Glob pattern for file matching

        Returns:
            List of loaded Document objects
        """
        if extensions is None:
            extensions = config.SUPPORTED_EXTENSIONS

        logger.info(f"Loading documents from {directory_path}")
        documents = []

        # Load each file type
        for ext in extensions:
            if ext.lower() == ".pdf":
                docs = self._load_pdf_directory(directory_path, glob_pattern)
                documents.extend(docs)

            elif ext.lower() == ".md":
                docs = self._load_markdown_directory(directory_path, glob_pattern)
                documents.extend(docs)

            elif ext.lower() == ".txt":
                docs = self._load_text_directory(directory_path, glob_pattern)
                documents.extend(docs)

            elif ext.lower() == ".docx":
                docs = self._load_docx_directory(directory_path, glob_pattern)
                documents.extend(docs)

        logger.info(f"Loaded {len(documents)} documents")
        return documents

    def load_single_file(self, file_path: str) -> List[Document]:
        """
        Load a single document file.

        Args:
            file_path: Path to the file

        Returns:
            List of Document objects (may be chunked)
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.info(f"Loading file: {file_path}")

        ext = file_path.suffix.lower()

        if ext == ".pdf":
            loader = PyPDFLoader(str(file_path))
        elif ext in [".md", ".txt"]:
            loader = TextLoader(str(file_path), encoding="utf-8")
        elif ext == ".docx":
            loader = Docx2txtLoader(str(file_path))
        else:
            raise ValueError(f"Unsupported file format: {ext}")

        documents = loader.load()
        return self.split_documents(documents)

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into chunks.

        Args:
            documents: List of Document objects to split

        Returns:
            List of split Document objects
        """
        logger.info(f"Splitting {len(documents)} documents into chunks")
        split_docs = self.splitter.split_documents(documents)
        logger.info(f"Created {len(split_docs)} chunks")
        return split_docs

    def _load_pdf_directory(
        self,
        directory_path: str,
        glob_pattern: str = "**/*"
    ) -> List[Document]:
        """Load all PDF files from a directory."""
        loader = DirectoryLoader(
            directory_path,
            glob=f"{glob_pattern}.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True
        )
        docs = loader.load()
        return self.split_documents(docs)

    def _load_markdown_directory(
        self,
        directory_path: str,
        glob_pattern: str = "**/*"
    ) -> List[Document]:
        """Load all Markdown files from a directory."""
        loader = DirectoryLoader(
            directory_path,
            glob=f"{glob_pattern}.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=True
        )
        docs = loader.load()
        return self.split_documents(docs)

    def _load_text_directory(
        self,
        directory_path: str,
        glob_pattern: str = "**/*"
    ) -> List[Document]:
        """Load all text files from a directory."""
        loader = DirectoryLoader(
            directory_path,
            glob=f"{glob_pattern}.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=True
        )
        docs = loader.load()
        return self.split_documents(docs)

    def _load_docx_directory(
        self,
        directory_path: str,
        glob_pattern: str = "**/*"
    ) -> List[Document]:
        """Load all DOCX files from a directory."""
        loader = DirectoryLoader(
            directory_path,
            glob=f"{glob_pattern}.docx",
            loader_cls=Docx2txtLoader,
            show_progress=True
        )
        docs = loader.load()
        return self.split_documents(docs)

    def preprocess_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Preprocess documents (clean up metadata, normalize text, etc.).

        Args:
            documents: List of Document objects

        Returns:
            List of preprocessed Document objects
        """
        for doc in documents:
            # Add metadata if missing
            if "source" not in doc.metadata:
                doc.metadata["source"] = "unknown"

            # Clean up page numbers
            if "page" in doc.metadata:
                doc.metadata["page"] = int(doc.metadata["page"])

            # Normalize whitespace
            doc.page_content = " ".join(doc.page_content.split())

        return documents


def load_documents(
    directory_path: str,
    chunk_size: int = config.CHUNK_SIZE,
    chunk_overlap: int = config.CHUNK_OVERLAP
) -> List[Document]:
    """
    Convenience function to load and split documents.

    Args:
        directory_path: Path to directory containing documents
        chunk_size: Size of chunks
        chunk_overlap: Overlap between chunks

    Returns:
        List of processed documents
    """
    processor = DocumentProcessor(chunk_size, chunk_overlap)
    documents = processor.load_from_directory(directory_path)
    return processor.preprocess_documents(documents)


if __name__ == "__main__":
    # Example: Load documents from sample directory
    processor = DocumentProcessor()

    # Create sample documents if they don't exist
    sample_dir = config.DOCUMENTS_DIR
    if not os.listdir(sample_dir):
        sample_file = os.path.join(sample_dir, "sample.txt")
        with open(sample_file, "w") as f:
            f.write("""Claude is an AI assistant created by Anthropic.

Key Features:
- Advanced reasoning capabilities
- Multi-modal understanding
- Constitutional AI training
- Long context window

Claude can help with:
- Writing and editing
- Analysis and research
- Problem solving
- Creative projects""")
        print(f"Created sample document: {sample_file}")

    # Load documents
    documents = processor.load_from_directory(sample_dir)
    print(f"Loaded and split {len(documents)} document chunks")

    for i, doc in enumerate(documents[:3]):
        print(f"\nChunk {i+1}:")
        print(f"  Source: {doc.metadata.get('source')}")
        print(f"  Content: {doc.page_content[:100]}...")
