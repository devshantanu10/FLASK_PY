from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("form.html")

@app.route("/submit" , methods= ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")      # use name , define method , should match route 

    # if username == "shanta123" and password == "pass":
    #       return render_template("form_welcome.html" , name = username )
    # else:
    #      return "Invalid username or password"
    valid_users = {
        'admin': '123' , 
        'shantanu' : 'pass' , 
          'poudel' : "234"
    }
    

    if username in valid_users and password == valid_users[username]:
        return render_template("form_welcome" , name = username)
    else: 
        return "invalid vcrendentials"


if __name__ == '__main__':
    app.run(debug=True , port=5000) 