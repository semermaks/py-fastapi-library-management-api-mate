from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class DBAuthors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(511), nullable=False)


class DBBooks(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    summary = Column(String(511), nullable=False)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship(DBAuthors)
