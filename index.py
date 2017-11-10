from flask import Flask, request, redirect, render_template, url_for

from databaseFunctions.database_functions import DbFunctions
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("update"))


@app.route("/update")
def update():
    return render_template('form.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    db = DbFunctions()
    student_name = request.form['student_name']

    db.update_current_user("Test Book", student_name)
    
    print("updated Test Book with student: {}".format(student_name))
    print(type(student_name))
    
    return redirect(url_for("update"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555")