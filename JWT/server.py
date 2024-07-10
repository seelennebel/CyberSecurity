from flask import Flask
from flask import (request, render_template, make_response)
from flask_cors import CORS, cross_origin

import jwt

app = Flask(__name__, template_folder = "templates")
CORS(app, supports_credentials=True)

@app.route("/", methods = ["GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
@cross_origin()
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        user = request.args.get("user")
        if user == None:
            return("Internal Server Error")
        
        if user == "admin":
            payload = {"exp" : "Session", "username" : user, "admin" : True}
            payload_str = str(payload).replace(" ", "")
            token = jwt.generate_JWT(payload_str, "ADMIN")
            res = make_response()
            res.set_cookie("token", token)

            return res

        if user != "admin":
            payload = {"exp" : "Session", "username" : user, "admin" : False}
            payload_str = str(payload).replace(" ", "")
            token = jwt.generate_JWT(payload_str, "USER")
            res = make_response()
            res.set_cookie("token", token)

            return res

@app.route("/secretpage", methods = ["GET"])
def validate():
    if request.method == "GET":
        token = request.cookies.get("token")
        if jwt.validate_JWT(token, "ADMIN"):
            return "ACCES GRANTED"
        else:
            return "ACCESS PROHIBITED!!!!"
    
app.run(port = 8000)
