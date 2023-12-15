# CSV File Uploader and Query Interface

## Overview

Welcome to [CSV File Uploader and Query Interface]! This web application allows users to seamlessly upload a CSV file, convert its data into vector embeddings using Hugging Face models, and store these embeddings in a Faiss database. Users can then query the database using Google Palm models with the ability to retrieve relevant information.

## Features

- **CSV File Upload:** Users can easily upload a CSV file containing their data.
- **Vector Embedding:** The application utilizes Hugging Face models to convert CSV data into vector embeddings.
- **Faiss Database:** Vector embeddings are stored in a Faiss database for efficient querying.
- **Interactive Querying:** Users can submit queries to the database using Google Palm models for accurate and contextual results.

## Prerequisites

Before running the application, ensure you have the following:

- [Python](https://www.python.org/) installed on your system.
- API keys for [Google Cloud](https://cloud.google.com/) and [Hugging Face](https://huggingface.co/) added to the `.env` file.

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone [https://github.com/MuhammedAjmalG/llm_langchain_learning/tree/main/llm_lang_csv_retrieval]
    ```

2. Navigate to the project directory:

    ```bash
    cd your_application
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    streamlit run main.py
    ```

5. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).

## Configuration

Make sure to add your Google Cloud and Hugging Face API keys to the `.env` file.


## Contributors

- [Muhammed Ajmal G] - [aju09896@gmail.com]
