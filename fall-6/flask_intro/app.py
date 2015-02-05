from flask import Flask,render_template


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/about")
def about():
    #s = "<h1>this is the about page</h1>"
    s = """
    <h1>Awesome Flask Web Site</h1>
    <ul>
    <li>item 1</li>
    <li>item 2</li>
    <li>item 3</li>
    </ul>
"""
    return s


@app.route("/p")
@app.route("/p/<lastname>")
@app.route("/p/<lastname>/<firstname>")
def person(lastname=None,firstname=None):
    return render_template("person.html"
                           ,lastname=lastname
                           ,firstname=firstname)

@app.route("/random")
def randomnumber():
    import random
    num = random.randrange(0,100)
    
    return render_template("random.html",
                           num=num,
                           name="Mr. T",
                           l=[1,2,3,4,5],
                           d={'a':1,'two':2,3:'hello'})


@app.route("/home")
@app.route("/") 
def home():
    return "<h1>This is the home page</h1>"

if __name__=="__main__":
    app.debug=True
    app.run() 

    
