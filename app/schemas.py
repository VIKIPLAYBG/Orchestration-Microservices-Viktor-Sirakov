from pydantic import BaseModel


class NoteCreate(BaseModel):
    content: str


class NoteOut(NoteCreate):
    id: int

    class Config:
        from_attributes = True
