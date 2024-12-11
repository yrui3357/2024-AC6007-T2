from flask import Flask
from flask import render_template,request
import textblob

app = Flask(__name__)

@app.route("/",methods=["GET","post"])
def index():
    return(render_template("index.html"))

@app.route("/SA",methods=["GET","post"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","post"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html", r=r))

if __name__ =="__main__":
    app.run()
