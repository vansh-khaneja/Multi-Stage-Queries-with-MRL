# Multi-Stage-Queries-with-MRL
This project implements multi-query retrieval using Matryoshka Representation Learning (MRL) embeddings with `text-embedding-3-small` and `text-embedding-3-large`. The embeddings are stored and queried using the Qdrant vector database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Steps](#steps)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction

In this project, we used Matryoshka Representation Learning embeddings for efficient multi-query retrieval. The embeddings are generated using `text-embedding-3-small` and `text-embedding-3-large` models and stored in the Qdrant vector database. This approach allows for scalable and accurate retrieval of relevant information from large datasets.

## Features

- Fast and efficient way for data retrieval
- Supports `text-embedding-3-small` and `text-embedding-3-large` models
- Two stage retrieval for better searching
- Scalable and high-performance retrieval system

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/vansh-khaneja/Multi-Stage-Queries-with-MRL
    cd Multi-Stage-Queries-with-MRL
    ```

2. Set up the Python environment and install dependencies:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Qdrant:

    Follow the [Qdrant documentation](https://qdrant.tech/documentation/) to install and configure Qdrant on your system.

## Major Steps

1.Get the data for this project [here](https://run.unl.pt/bitstream/10362/135618/1/TEGI0570.pdf) or you can try with your own dataset.


2. Performing multi-query retrieval:

    ```python
    result = client.query_points(
    collection_name= COLLECTION_NAME,
    prefetch=models.Prefetch(
        query=small_vector,
        using="small-embedding",
        limit=50,
    ),
    query=large_vector,
    using="large-embedding",
    limit=5,
    )

    ```



