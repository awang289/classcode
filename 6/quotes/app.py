from flask import Flask,request,url_for,redirect,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")



if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=8000)
