import os
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    linkedin_url = Column(String, unique=True)
    tags = Column(String)
    hotness = Column(Integer, default=2)
    fit = Column(Integer, default=2)

class Touch(Base):
    __tablename__ = "touches"
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    channel = Column(String)
    time = Column(String)
    note = Column(Text)
    outcome = Column(String)
    next_time = Column(String)

Base.metadata.create_all(bind=engine)
