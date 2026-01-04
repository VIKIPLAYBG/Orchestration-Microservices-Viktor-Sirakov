from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_note, get_notes
from schemas import NoteCreate, NoteOut
from init_db import init_db  # call function explicitly

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8080"] for stricter control
    allow_methods=["*"],
    allow_headers=["*"],
)

# explicitly create tables
init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notes", response_model=NoteOut)
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)


@app.get("/notes", response_model=list[NoteOut])
def read_notes_endpoint(db: Session = Depends(get_db)):
    return get_notes(db)
