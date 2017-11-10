import os 
import sys

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    current_student = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)



def create_database(self):
    engine = create_engine('sqlite:///database/library.db')
    Base.metadata.create_all(engine)