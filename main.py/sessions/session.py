from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "secret123"   # required for session
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username   # ✅ store user
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials ❌"

    return render_template("sess/session.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("sess/dashboard.html", user=session["user"])
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)   # remove user
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)