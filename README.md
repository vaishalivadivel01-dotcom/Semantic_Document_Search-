
# Semantic Document Search

## Project Description
Semantic Document Search is a Python-based project that retrieves relevant documents based on the meaning of a user's search query.

## Technologies Used
- Python
- ChromaDB
- Pandas
- NumPy
- ONNX Embeddings

## Project Features
- Document loading and indexing
- Semantic search
- Similarity distance calculation
- Search results stored in CSV files
- Persistent vector database

## Project Structure
- dataset/documents - Text documents
- dataset/queries.csv - Search queries
- dataset/search_results.csv - Search results
- dataset/similarity_scores.csv - Similarity scores
- chroma_db - Vector database
- semantic_search.py - Main Python program
- notebook - Jupyter notebook

## How to Run
1. Install requirements:
   pip install -r requirements.txt

2. Run the project:
   python semantic_search.py

## Output
The project retrieves relevant documents and saves search results and similarity scores as CSV files.

