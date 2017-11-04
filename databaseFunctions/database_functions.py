import pandas as pd
import sys, os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from databaseFunctions.database_model import Student, Base, Book, create_database



class DbFunctions():

    def __init__(self):
        sys.path.append('..')
        self.engine = create_engine('sqlite:///database/exampledb.db')
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
        print(student.id)
        book = self.session.query(Book).filter_by(name = book_name).first()
        book.current_student = student.id
        self.session.add(book)
        self.session.commit()

    def populate_student_table(self):
        students = []
        index=0

        q = 'SELECT * from student WHERE name = {}'.format

        df = pd.read_excel(os.path.join(os.path.dirname(__file__),'../files/students.xlsx'), sheetname='Sheet1')
        
        for i in df.index:
            students.append(df['Student Names'][i])

        for j in students:
            print('Adding Student: {}. type: {}'.format(students[index], type(students[index])))
            self.insert_student(students[index])
            index+=1
    
    
    
    def get_book_names(self):
        bookNames=[]

        for i in self.session.query(Book).all():
            bookNames.append(i.name)

        return bookNames

    
    
    
    def test_import(self):
        print("Able to import databaseFunctions properly")
        

    

    
    def create_db(self):
        create_database(self)

    


