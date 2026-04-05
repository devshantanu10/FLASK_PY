from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("Username")
    password = request.form.get("Password")

    valid_users = {
        'admin': '123',
        'santanu': '456'
    }

    
    if username in valid_users and password == valid_users[username]:
        return render_template("Welcome.html", name=username)
    else:
        return "Invalid credentials"


if __name__ == "__main__":
    app.run(debug=True)