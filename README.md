# Multi-Stage-Queries-with-MRL
This project implements multi-query retrieval using Matryoshka Representation Learning (MRL) embeddings with `text-embedding-3-small` and `text-embedding-3-large`. The embeddings are stored and queried using the Qdrant vector database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction

In this project, we leverage Matryoshka Representation Learning embeddings for efficient multi-query retrieval. The embeddings are generated using `text-embedding-3-small` and `text-embedding-3-large` models and stored in the Qdrant vector database. This approach allows for scalable and accurate retrieval of relevant information from large datasets.

## Features

- Multi-query retrieval with MRL embeddings
- Supports `text-embedding-3-small` and `text-embedding-3-large` models
- Uses Qdrant for efficient storage and retrieval of embeddings
- Scalable and high-performance retrieval system

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Set up the Python environment and install dependencies:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Qdrant:

    Follow the [Qdrant documentation](https://qdrant.tech/documentation/) to install and configure Qdrant on your system.

## Usage

1. Prepare your data and generate embeddings using the `text-embedding-3` models.

2. Store the embeddings in Qdrant:

    ```python
    from qdrant_client import QdrantClient
    from your_project.embedding import generate_embeddings

    client = QdrantClient("http://localhost:6333")
    embeddings = generate_embeddings(data)
    client.upsert(embeddings)
    ```

3. Perform multi-query retrieval:

    ```python
    from your_project.retrieval import multi_query_retrieval

    results = multi_query_retrieval(client, queries)
    for result in results:
        print(result)
    ```

## Configuration

Configuration options can be set in the `config.py` file. This includes settings for the embedding models, Qdrant connection, and other parameters.

```python
# config.py

QDRANT_HOST = 'localhost'
QDRANT_PORT = 6333

EMBEDDING_MODEL_SMALL = 'text-embedding-3-small'
EMBEDDING_MODEL_LARGE = 'text-embedding-3-large'
