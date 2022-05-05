from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/index.html", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        print(request.form)
    return render_template("index.html")


@app.route("/index1.html", methods=["POST", "GET"])
def index1():
    if request.method == 'POST':
        print(request.form)

    return render_template("index1.html")


@app.route("/index2.html", methods=["POST", "GET"])
def index2():
    if request.method == 'POST':
        print(request.form)
    return render_template("index2.html")


@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == 'POST':
        print(request.form)
        print(request.form['q'])
        URL = "https://www.google.com/search?q=" + request.form['q']
    return '0'


@app.route("/form1", methods=["POST", "GET"])
def form1():
    if request.method == 'POST':
        print(request.form)
        print(request.form['q'])
        URL = "https://www.google.com/images?q=" + request.form['q']
    return '0'
#https://www.google.com/search?as_q=q&as_epq=w&as_oq=e&as_eq=r

@app.route("/form2", methods=["POST", "GET"])
def form2():
    if request.method == 'POST':
        print(request.form)
        URL = "https://www.google.com/search?as_q=" + request.form['as_q']+'&'+ request.form['as_epq']+'&'+ request.form['as_oq']+'&'+ request.form['as_eq']
    return '0'

if __name__ == "__main__":
    app.run(debug=True)