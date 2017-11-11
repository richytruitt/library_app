import sys

from databaseFunctions.database_functions import DbFunctions
from labelmaking.createlabels import Create_Labels
from main_functions.main_functions import MainFunctions

db = DbFunctions()


#------------------------------------------------Create------------------------------------------------------#
if sys.argv[1] == '1':
    db.create_db()

if sys.argv[1] == '2':
    db.insert_student("Richy Truitt")

if sys.argv[1] == '3':
    db.insert_book("Test Book 3")

if sys.argv[1] == '4':
    db.update_current_user("Test Book", "Richy Truitt")

if sys.argv[1] == '5':
    db.populate_student_table()

if sys.argv[1] == '6':
    db.populate_book_table()

if sys.argv[1] == '7':
    labelmaker = Create_Labels()
    labelmaker.create_labels()

if sys.argv[1] == '8':
    db.get_book_names()
    #get all books from the database, and place into list. 

if sys.argv[1] == '9':
    db.get_name_of_owner(sys.argv[2])

if sys.argv[1] == 'checkout':
    student_name = input('What is the name of the student: ')
    book_name = input('What is the name of the book: ')


    mainFunc = MainFunctions(book_name, student_name, db.get_session())

    mainFunc.checkout()





