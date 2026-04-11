from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/user/<username>")
def profile(username):
    return f"<h1>Hello, {username}!</h1>"

@app.route("/post/<int:post_id>")
def post(post_id):
    if post_id < 1:
        return "<h1>404 - Post not found</h1>", 404
    return f"<h1>Showing post number {post_id}</h1>"

if __name__ == '__main__':
    app.run(debug=True)