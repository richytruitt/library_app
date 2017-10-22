from databaseFunctions.database_functions import DbFunctions
import sys

db = DbFunctions()


#------------------------------------------------Create------------------------------------------------------#
if sys.argv[1] == '1':
    db.create_db()

if sys.argv[1] == '2':
    db.insert_student("New Student")

if sys.argv[1] == '3':
    db.insert_book("Title of the new book")

if sys.argv[1] == '4':
    db.update_current_user("Title of the new book", "Richy Truitt")

if sys.argv[1] == '5':
    db.populate_student_table()

