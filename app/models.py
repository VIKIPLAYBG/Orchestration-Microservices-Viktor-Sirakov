from sqlalchemy import Column, Integer, Text
from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
