from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    return "hello world! this is my first flask app "

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "this is contact page"



@app.route("/submit" , methods = ["GET" , "POST"])
def submit():
    if request.method == "POST":
        return "you sent data"
    else:
        return "You are only viewing the form"