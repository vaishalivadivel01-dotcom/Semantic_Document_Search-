
import chromadb
import os
import pandas as pd

DOCUMENTS_PATH = "dataset/documents"
DB_PATH = "chroma_db"

client = chromadb.PersistentClient(path=DB_PATH)

embedding_function = chromadb.utils.embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="documents",
    embedding_function=embedding_function
)

# Index documents
for filename in os.listdir(DOCUMENTS_PATH):
    if filename.endswith(".txt"):
        with open(os.path.join(DOCUMENTS_PATH, filename), "r", encoding="utf-8") as file:
            content = file.read()

        collection.upsert(
            ids=[filename],
            documents=[content],
            metadatas=[{"filename": filename}]
        )

print("Documents indexed successfully!")

# Read search queries
queries = pd.read_csv("dataset/queries.csv")

search_results = []
similarity_scores = []

for _, row in queries.iterrows():
    query_id = row["query_id"]
    query = row["query"]

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        search_results.append({
            "query_id": query_id,
            "query": query,
            "document_name": metadata["filename"],
            "document_content": document,
            "distance": distance
        })

        similarity_scores.append({
            "query_id": query_id,
            "document_name": metadata["filename"],
            "distance": distance,
            "similarity_score": 1 / (1 + distance)
        })

# Save results
pd.DataFrame(search_results).to_csv(
    "dataset/search_results.csv", index=False
)

pd.DataFrame(similarity_scores).to_csv(
    "dataset/similarity_scores.csv", index=False
)

print("Search results saved successfully!")
print("Similarity scores saved successfully!")
