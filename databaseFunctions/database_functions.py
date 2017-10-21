from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from databaseFunctions.database_model import Student, Base, Book, create_database



class DbFunctions():

    def __init__(self):
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

        

    def create_db(self):
        create_database(self)

