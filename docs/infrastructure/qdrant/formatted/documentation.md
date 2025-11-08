---
title: Qdrant Documentation
description: Complete documentation for Qdrant vector database platform
service: qdrant
version: 1.0
last_updated: 2025-11-08
---

# Qdrant: Vector Database Overview

Qdrant is an open-source vector database platform specializing in similarity search for AI applications. Here's what defines it:

## Core Capabilities

Qdrant excels at "managing, searching, and retrieving high-dimensional vector data" essential for modern AI systems. The platform supports both dense and sparse vectors, enabling sophisticated search strategies including hybrid approaches that combine semantic understanding with keyword matching.

## Key Features

The platform offers:

- **Hybrid search**: Combining dense vectors for semantic similarity with sparse vectors for keyword precision
- **Retrieval-Augmented Generation (RAG)**: Efficient nearest neighbor search with payload filtering
- **Multivector representations**: Support for token-level embeddings enabling late interaction models like ColBERT
- **Advanced indexing**: HNSW-based indexing with configurable parameters for optimization

## Deployment Options

Qdrant provides multiple deployment models:

- **Managed Cloud**: SaaS solution eliminating infrastructure maintenance
- **Hybrid Cloud**: Runs on your Kubernetes clusters while using Qdrant's cloud console for management
- **Self-hosted**: Docker-based deployment for local or on-premises use

## Technical Highlights

Built in Rust, Qdrant prioritizes performance. The platform includes FastEmbed for efficient embedding generation and supports REST/gRPC APIs with official clients for Python, JavaScript, Rust, Go, Java, and .NET.

The system handles enterprise requirements including high availability, zero-downtime upgrades, and comprehensive monitoring—all while maintaining data sovereignty in hybrid deployments.

---

**Navigation**: [Documentation Index](index.md) | [Source](../llms-full.txt)
