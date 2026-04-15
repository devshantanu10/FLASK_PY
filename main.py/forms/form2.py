from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return "Login Successful"
        else:
            return "Invalid Credentials"

    return render_template("form/form.html")   # ✅ FIXED

if __name__ == "__main__":
    app.run(debug=True, port=5000)