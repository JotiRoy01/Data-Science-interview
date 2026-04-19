from flask import Flask, render_template, url_for, request, jsonify, flash, redirect

app = Flask(__name__)

app.secret_key = "secret key"

# URL => end point /, when the request reach the "/" then execute the function.
@app.route("/")
def hello_world() :
    flash("support timings are from 9-5")
    #return render_template("index2.html")
    return redirect(url_for("login"))

@app.route("/login") 
def login() :
    return "<p> Login Page </p>"


if __name__ == "__main__" :
    app.run(debug=True)