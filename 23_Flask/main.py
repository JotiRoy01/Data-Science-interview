from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__, static_folder="assets")

# URL => end point /, when the request reach the "/" then execute the function.
@app.route("/")
def hello_world() :
    # static file => dynamic generate the url
    print(url_for("static", filename="style2.css"))
    name = request.args.get("name")
    subject = request.args.get("subject")
    data = {
        "message": "welcome to the platform"
    }
    return jsonify(data)
    # return render_template("index.html", name=name, sub=subject)
 
# @app.route("/login")
# def login() :
#     if request.method == "POST" :
#         #return "<p>POST request</p>"
#         print(request.form)
#         name = request.form["username"]
#         password = request.form["password"]
#         return f"<p>Welcome {name} and your password is: {password}"
#     else :
#         return render_template("login.html")

@app.route("/login")
def login() :
    if request.method == "POST" :
        #return "<p>POST request</p>"
        print(request.form)
        name = request.form["username"]
        password = request.form["password"]

        friend = ["Adam", "Bob", "Charlie", "Dan"]
        header = "<header>ABC Website</header>"

        return render_template("welcome.html", name=name, password=password, header = header)
    else :
        return render_template("login.html")

@app.route("/handle-login", methods=["GET", "POST"]) 
def handle_login() :
    if request.method == "POST" :
        #return "<p>POST request</p>"
        print(request.form)
        name = request.form["username"]
        password = request.form["password"]
        return f"<p>Welcome {name} and your password is: {password}"
    if request.method == "GET" :
        return "<p>GET request</p>"

    return "<p>This page is to handle login</p>"

if __name__ == "__main__" :
    app.run(debug = True)