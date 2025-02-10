from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Document
from pydantic import BaseModel

app = FastAPI()

# Pydantic Schema
class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Search Engine!"}

# ✅ Get all documents
@app.get("/documents/", response_model=List[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()

# ✅ Search documents by title
@app.get("/search/")
def search(
    query: str,
    limit: int = Query(10, ge=1, le=100),  # Default limit: 10, min: 1, max: 100
    offset: int = Query(0, ge=0),  # Default offset: 0
    db: Session = Depends(get_db),
):
    results = (
        db.query(Document)
        .filter(Document.title.ilike(f"%{query}%"))
        .offset(offset)
        .limit(limit)
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    return results


# ✅ Upload a new document
@app.post("/upload/", response_model=DocumentResponse)
def upload_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    new_doc = Document(title=doc.title, content=doc.content)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

# ✅ Get a document by ID
@app.get("/documents/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

# ✅ Update a document
@app.put("/documents/{doc_id}", response_model=DocumentResponse)
def update_document(doc_id: int, updated_doc: DocumentCreate, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    doc.title = updated_doc.title
    doc.content = updated_doc.content
    db.commit()
    return doc

# ✅ Delete a document
@app.delete("/documents/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(doc)
    db.commit()
    return {"message": "Document deleted successfully"}
