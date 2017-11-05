from databaseFunctions.database_functions import DbFunctions
import sys

from labelmaking.createlabels import Create_Labels

db = DbFunctions()


#------------------------------------------------Create------------------------------------------------------#
if sys.argv[1] == '1':
    db.create_db()

if sys.argv[1] == '2':
    db.insert_student("New Student")

if sys.argv[1] == '3':
    db.insert_book("Test Book")

if sys.argv[1] == '4':
    db.update_current_user("Title of the new book", "Richy Truitt")

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





