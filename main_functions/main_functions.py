import os, sys
sys.path.append('..')

from databaseFunctions.database_functions import DbFunctions
from databaseFunctions.database_model import Student, Base, Book, create_database

class MainFunctions():
        
        def __init__(self, book_name, student_name, session):
            self.student_name = student_name
            self.book_name = book_name
            self.session = session
            self.db = DbFunctions()
        
        def checkout(self):
            print("Updating the book: {} with the new student: {}".format(self.book_name, self.student_name))
            book = self.session.query(Book).filter_by(name = self.book_name).first()
            student = self.session.query(Student).filter_by(name = self.student_name).first()

            if book != None and student != None:
                self.db.update_current_user(self.book_name, self.student_name)
            else:
                print("Check inputs")