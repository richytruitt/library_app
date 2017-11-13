import pyqrcode
import os, sys
sys.path.append('..')

from databaseFunctions.database_functions import DbFunctions


class Create_Labels():

    def create_labels(self):
        db = DbFunctions()

        book_names = db.get_book_names()
        student_names = db.get_student_names()

        print("Beginning to create a label")

        for i in book_names:
            '''
                the pyqrcode.create() function takes the information that the qrcode will display as a parameter. Code.png depends on pypng in order to run
            '''
            code = pyqrcode.create(i)
            code.png('labelmaking/labels/books/{}.png'.format(i), scale=5)

        for i in student_names:

            code = pyqrcode.create(i)
            code.png('labelmaking/labels/students/{}.png'.format(i), scale=5)







