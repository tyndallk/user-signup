from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app. config['DEBUG'] = True
       

@app.route("/")
def index():
    return render_template('index.html', title= "Signup")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form ['password']
        verify = request.form['verify']
        

        if len(username) < 3 or len(username) > 20:
            username_error = 'Username not valid'
            return render_template('index.html', username_error = username_error)

        if len(password) < 3 or len(password) > 20:
            password_error = 'Password not valid'
            return render_template('index.html', password_error = password_error)

        if verify == '' or verify != password:
            verify_error = 'Verify password not valid'
            return render_template('index.html', verify_error = verify_error)

        if len(email) < 1:
            return render_template('welcome.html', username = username) 
        
        if len(email) < 3 or len(email) > 20:
           email_error = 'Invalid email'
           return render_template('index.html', email_error = email_error)
        
        if "@" not in email or "." not in email or " " in email:
            email_error = 'Email must contain no spaces and the following symbols: @ .'
            return render_template('index.html', email_error = email_error) 

    return render_template('welcome.html', username = username)   
  

app.run()