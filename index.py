from flask import Flask, request, redirect, render_template, url_for
from jinja2 import Environment, FileSystemLoader

from databaseFunctions.database_functions import DbFunctions
app = Flask(__name__)

@app.route("/")
def index():
    # return redirect(url_for("update"))
    return render_template('index.html')


@app.route("/update")
def update():
    db = DbFunctions()
    students = db.get_student_names()
    books = db.get_book_names()

    return render_template('form.html', names = students, books = books)


@app.route('/checkout', methods=['POST'])
def checkout():
    db = DbFunctions()
    book_list = []
    student_name = request.form['student_name']
    book_names = request.form['book_names']
    
    split_list = book_names.split(',')
    
    for i in split_list:
        book_list.append(i.strip())

    for i in book_list:
        db.update_current_user(i, student_name)
    
    return redirect(url_for("update"))


@app.route('/ids')
def ids():
    db = DbFunctions()
    names = db.get_student_names()
    dictionary = []
    
    for i in names:
        case = {'link': 'labels/students/{}.png'.format(i), 'name': i}
        dictionary.append(case)
    
    print(dictionary)

    return render_template('ids.html', items=dictionary)


@app.route('/books')
def books():
    db = DbFunctions()
    books = db.get_book_names()
    dictionary = []
    
    for i in books:
        case = {'link': 'labels/books/{}.png'.format(i), 'name': i}
        dictionary.append(case)
    
    print(dictionary)

    return render_template('books.html', items=dictionary)


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555")