#!/usr/bin/env python3
"""
Document Ingestion Script

Loads documents from a directory, generates embeddings,
and stores them in Pinecone vector database.

Usage:
    python ingest.py --path ./data/documents
    python ingest.py --path ./data --clear  # Clear and reingest
"""

import argparse
import logging
from pathlib import Path

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from pinecone import Pinecone as PineconeClient

import config
from utils.document_loader import DocumentProcessor

logging.basicConfig(
    level=config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def initialize_pinecone_index(dimension: int = config.PINECONE_DIMENSION):
    """
    Initialize Pinecone index if it doesn't exist.

    Args:
        dimension: Dimension of embeddings
    """
    pc = PineconeClient(
        api_key=config.PINECONE_API_KEY,
        environment=config.PINECONE_ENVIRONMENT
    )

    # Check if index exists
    indexes = [index.name for index in pc.list_indexes()]

    if config.PINECONE_INDEX_NAME not in indexes:
        logger.info(f"Creating Pinecone index: {config.PINECONE_INDEX_NAME}")
        pc.create_index(
            name=config.PINECONE_INDEX_NAME,
            dimension=dimension,
            metric="cosine",
            spec={
                "serverless": {
                    "cloud": "aws",
                    "region": config.PINECONE_ENVIRONMENT
                }
            }
        )
        logger.info("Index created successfully")
    else:
        logger.info(f"Index {config.PINECONE_INDEX_NAME} already exists")


def clear_index():
    """Delete all vectors from the Pinecone index."""
    pc = PineconeClient(
        api_key=config.PINECONE_API_KEY,
        environment=config.PINECONE_ENVIRONMENT
    )

    index = pc.Index(config.PINECONE_INDEX_NAME)
    logger.info(f"Clearing index: {config.PINECONE_INDEX_NAME}")
    index.delete(delete_all=True)
    logger.info("Index cleared")


def ingest_documents(documents_path: str, clear: bool = False):
    """
    Load documents and ingest them into Pinecone.

    Args:
        documents_path: Path to documents directory
        clear: Whether to clear existing vectors first
    """
    # Validate path
    path = Path(documents_path)
    if not path.exists():
        logger.error(f"Path does not exist: {documents_path}")
        return

    if not path.is_dir():
        logger.error(f"Path is not a directory: {documents_path}")
        return

    # List files to ingest
    files = list(path.rglob("*"))
    doc_files = [f for f in files if f.suffix in config.SUPPORTED_EXTENSIONS]

    if not doc_files:
        logger.warning(f"No documents found in {documents_path}")
        return

    logger.info(f"Found {len(doc_files)} documents to ingest")

    # Clear existing data if requested
    if clear:
        clear_index()

    # Load documents
    logger.info(f"Loading documents from {documents_path}")
    processor = DocumentProcessor(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    documents = processor.load_from_directory(documents_path)
    documents = processor.preprocess_documents(documents)

    logger.info(f"Loaded {len(documents)} document chunks")

    # Initialize embeddings
    logger.info(f"Initializing embeddings: {config.EMBEDDING_MODEL}")
    embeddings = OpenAIEmbeddings(
        model=config.EMBEDDING_MODEL,
        openai_api_key=config.OPENAI_API_KEY
    )

    # Create and store vectors in Pinecone
    logger.info("Storing documents in Pinecone...")
    try:
        vectorstore = Pinecone.from_documents(
            documents=documents,
            embedding=embeddings,
            index_name=config.PINECONE_INDEX_NAME,
            namespace=None
        )
        logger.info(f"Successfully ingested {len(documents)} documents")

        # Print index stats
        pc = PineconeClient(
            api_key=config.PINECONE_API_KEY,
            environment=config.PINECONE_ENVIRONMENT
        )
        index = pc.Index(config.PINECONE_INDEX_NAME)
        stats = index.describe_index_stats()
        logger.info(f"Index stats: {stats.total_vector_count} vectors")

    except Exception as e:
        logger.error(f"Error ingesting documents: {e}")
        raise


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Ingest documents into Pinecone vector database"
    )
    parser.add_argument(
        "--path",
        required=True,
        help="Path to documents directory"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear existing vectors before ingesting"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=config.CHUNK_SIZE,
        help=f"Document chunk size (default: {config.CHUNK_SIZE})"
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=config.CHUNK_OVERLAP,
        help=f"Chunk overlap (default: {config.CHUNK_OVERLAP})"
    )

    args = parser.parse_args()

    # Update config if provided
    if args.chunk_size:
        config.CHUNK_SIZE = args.chunk_size
    if args.chunk_overlap:
        config.CHUNK_OVERLAP = args.chunk_overlap

    logger.info("=" * 60)
    logger.info("Document Ingestion Started")
    logger.info("=" * 60)
    logger.info(f"Path: {args.path}")
    logger.info(f"Clear: {args.clear}")
    logger.info(f"Chunk Size: {config.CHUNK_SIZE}")
    logger.info(f"Chunk Overlap: {config.CHUNK_OVERLAP}")
    logger.info(f"Embedding Model: {config.EMBEDDING_MODEL}")
    logger.info(f"Index: {config.PINECONE_INDEX_NAME}")
    logger.info("=" * 60)

    try:
        # Initialize index
        initialize_pinecone_index()

        # Ingest documents
        ingest_documents(args.path, clear=args.clear)

        logger.info("=" * 60)
        logger.info("Ingestion completed successfully!")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        exit(1)


if __name__ == "__main__":
    main()
