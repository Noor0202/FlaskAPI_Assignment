# Document Summarization API

## Overview

This project contains two versions of a document summarization service built using FastAPI and Hugging Face's transformers library for model-based text summarization.

- **Document_Summarization.zip**: Contains fully functioning code that uses the T5 summarization model.
- **Document_Summarization_Take_Time_to_Run.zip**: Contains multiple summarization models including BART, T5, and Pegasus. This version requires more time to run due to model training and downloading.

## Project Structure

document_summarization_api/
│
├── app/
│ ├── main.py # The main FastAPI app.
│ ├── models/ # Directory to store summarization logic.
│ │ ├── summarization.py # Summarization function and model.
│ ├── routes/ # Directory to store API route logic.
│ │ ├── summary_routes.py # Routes related to summarization endpoints.
│ ├── services/ # Services for fetching and validating content.
│ │ ├── fetch_document.py # Fetches and validates document content.
│ ├── storage/ # In-memory storage handling for summaries.
│ │ ├── summary_store.py # Logic for storing summaries in memory.
│ ├── utils/ # Utility functions such as URL validation.
│ │ ├── validators.py # URL validation logic.
│
├── README.md # Project documentation and instructions.
├── requirements.txt # Dependencies for the project.

## Running the API

### Step 1: Install Dependencies

Ensure all dependencies are installed:

pip install -r requirements.txt

### Step 2: Run the Application

Use the following command to run the FastAPI application:

uvicorn app.main:app --reload

### Step 3: Summarize a Document

To summarize a document from a URL, use the following `curl` command:

curl -X POST "http://127.0.0.1:8000/summarize" \ -H "Content-Type: application/json" \ -d "{\"url\":\"https://www.gutenberg.org/files/1342/1342-0.txt\"}"

**Sample Response:**

{
"id": "b4fd8b7d-5eaf-4db9-9cbb-3f37de2e148b"
}

### Step 4: Retrieve Summary

Use the `id` from the previous response to get the summary:

curl -X GET "http://127.0.0.1:8000/summary/{id}"

Replace `{id}` with the actual ID.

## Document_Summarization_Take_Time_to_Run (Takes Time to Run)

For the **Document_Summarization_Take_Time_to_Run.zip** file, the code trains additional models such as BART and Pegasus, and involves dataset processing with Hugging Face. It requires more time to execute due to model training and downloading large datasets.

### Sample Models in Use:

- **T5-Base**
- **Pegasus**
- **BART**
