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

    
    username_error = ''
    email_error = ''
    password_error = ''
    verify_error = ''
        
        else:
            if len(username) < 3 or len(username) > 20:
                username_error = 'Username not valid'
                return render_template('index.html', username_error = username_error)

        return  render_template('welcome.html', username = username)

   

    

app.run()