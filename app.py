from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/1")
def index1():
    return render_template("index1.html")


@app.route("/2")
def index2():
    return render_template("index2.html")



if __name__ == "__main__":
    app.run(debug=True)