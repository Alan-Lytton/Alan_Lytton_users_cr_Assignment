from flask import Flask, render_template, request, redirect, session
from users import User  #change this import line based on your extra .py file for generating OOP instances
app=Flask(__name__)
app.secret_key = "users816don't098qu1t"  # Change the secret key so each assignment is unique.

@app.route("/list-users")     # lines 6 through 11 can be changed depending on what we need server.py to do.
def r_list_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)

@app.route('/new')
def r_new_user():
    return render_template('create.html')

@app.route('/new_user', methods=['POST'])
def f_new_user():
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email']
    }
    User.add_user(data)
    return redirect('/list-users')


if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)
