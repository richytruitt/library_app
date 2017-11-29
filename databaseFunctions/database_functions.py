import pandas as pd
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from databaseFunctions.database_model import Student, Base, Book, create_database

class DbFunctions():

    def __init__(self):
        self.engine = create_engine('sqlite:///database/library.db')
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()


    def insert_student(self, student_name):
        new_student = Student(name=student_name)
        self.session.add(new_student)
        self.session.commit()


    def insert_book(self, book_name):
        new_book = Book(name=book_name)
        self.session.add(new_book)
        self.session.commit()


    def update_current_user(self, book_name, student_name):
        student = self.session.query(Student).filter_by(name=student_name).first()
        book = self.session.query(Book).filter_by(name = book_name).first()
        book.current_student = student.id
        self.session.add(book)
        self.session.commit()


    def populate_book_table(self):
        books=[]
        index=0

        df = pd.read_excel(os.path.join(os.path.dirname(__file__),'../files/books.xlsx'), sheetname='Sheet1')
        
        for i in df.index:
            books.append(df['Book Names'][i])
    

    def populate_student_table(self):
        students = []
        index=0

        df = pd.read_excel(os.path.join(os.path.dirname(__file__),'../files/students.xlsx'), sheetname='Sheet1')
        
        for i in df.index:
            students.append(df['Student Names'][i])
    

    def get_book_names(self):
        bookNames=[]

        for i in self.session.query(Book).all():
            bookNames.append(i.name)

        return bookNames


    def get_student_names(self):
        student_names=[]

        for i in self.session.query(Student).all():
            student_names.append(i.name)

        return student_names


    def get_name_of_owner(self, student_id):
        student = self.session.query(Student).filter_by(id = student_id).first()
        
        print("The owner is: {}".format(student.name))
    
    
    def query_books_database(self):
        display = []
        books = self.session.query(Book).all()
        students = self.session.query(Student).all()

        print("Printing books table")
        for i in books:
            if i.current_student == None:
                display.append( {"id": i.id, "name": i.name, "current_student": "No student Currently"} )

            else:
                display.append( {"id": i.id, "name": i.name, "current_student": students[i.current_student-1].name} )
        
        return display


    def get_session(self):
        return self.session


    def create_db(self):
        create_database(self)

    


