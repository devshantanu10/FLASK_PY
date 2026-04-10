from flask import Flask , render_template



app = Flask(__name__)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/user/<username>")
def profile(username):
    return f"<h1>Hello, {username}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
