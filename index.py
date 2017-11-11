from flask import Flask, request, redirect, render_template, url_for

from databaseFunctions.database_functions import DbFunctions
app = Flask(__name__)

@app.route("/")
def index():
    # return redirect(url_for("update"))
    return render_template('index.html')


@app.route("/update")
def update():
    return render_template('form.html')

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555")