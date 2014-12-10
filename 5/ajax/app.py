from flask import Flask,request,url_for,redirect,render_template
import time
from flask_debugtoolbar import DebugToolbarExtension
import json

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getstuff")
def getstuff():
    print "In getstuff"
    time.sleep(5)
    print "Returning from getstuff"
    return "stuff"

@app.route("/getslow")
def getslow():
    print "In getslow"
    time.sleep(10)
    print "Returning from slow"
    return "returning slow"

@app.route("/getfast")
def getfast():
    print "In getfast"
    print "Returning from fast"
    return "returning fast"

@app.route("/upcase")
def upcase():
    data = request.args.get('data',"there was no data")
    data = data
    result = {"original":data,
              "result": data.upper()}
    return json.dumps(result)

if __name__=="__main__":
   app.debug=True
   app.config['SECRET_KEY'] = '<replace with a secret key>'
   toolbar = DebugToolbarExtension(app)
   app.run(host="0.0.0.0",port=8000)
