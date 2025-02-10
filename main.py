from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Fake database
documents = [
    {"id": 1, "title": "FastAPI Tutorial", "content": "Learn FastAPI step by step."},
    {"id": 2, "title": "Python Tips", "content": "Best Python tricks for developers."},
]

@app.get("/")
def home():
    return {"message": "Welcome to the AI Search Engine!"}

@app.get("/search/")
def search(query: str):
    results = [doc for doc in documents if query.lower() in doc["title"].lower()]
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    return results

@app.post("/upload/")
def upload_document(title: str, content: str):
    new_doc = {"id": len(documents) + 1, "title": title, "content": content}
    documents.append(new_doc)
    return {"message": "Document uploaded successfully", "document": new_doc}
