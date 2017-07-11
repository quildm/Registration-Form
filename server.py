from flask import Flask, render_template, request, redirect, flash
import re
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_result():
    name = request.form['first']
    last = request.form['last']
    email = request.form['email']
    password1 = request.form['password']
    passCode = request.form['confirm password']


    if len(request.form['first']) < 1:
        flash("Name field cannot be blank!",'firstNameError')
    elif any(char.isdigit() for char in request.form['first']) == True:
        flash('Name cannot have numbers', 'firstNameError')

    if len(request.form['last']) < 1:
        flash("Name field cannot be blank!",'lastNameError')
    elif any(char.isdigit() for char in request.form['last']) == True:
        flash('Name cannot have numbers', 'lastNameError')

    if len(request.form['email']) == 0:
        flash("email field cannot be blank!",'emailError')
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')

    if request.form['confirm password'] == '':
        flash("password not be blank",'passwordError')
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
    elif request.form['password'] != request.form['confirm password']:
        flash('password does not match','passwordError')
    
     
    return render_template("result.html", firstNamed = name, lastNamed = last, emailEd = email, passWorded = passCode)

app.run(debug=True) # run our server