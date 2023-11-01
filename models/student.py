from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    StudentID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Email = Column(String)
    Password = Column(String)