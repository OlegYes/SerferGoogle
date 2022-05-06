from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as BS

app = Flask(__name__)
def start_ref(q):
    global data
    data = {}
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    req = requests.get(q, headers=headers)
    src = req.text
    with open('indextest.html', 'w') as f:
        f.write(src)
    soup = BS(src, "lxml")
#    menu = soup.find("h3").find_parents("div", id="search").
    menu = soup.find_all("h3")


    q=0
    for i in menu:
        q = q+1
        inmenu = i.find_parent().find_parent().find_parent().find_parent()
        inmenu_lincs = inmenu.find("a")
        lincs = inmenu_lincs.get("href")
        h3 = inmenu.find("h3")
        lincs_rev = str(lincs)
        cite = inmenu.find("cite")

        text_stat = inmenu.find("div", {"data-content-feature" : 1})   #data-content-feature="1"
#        print(text_stat)

        data[q] = [lincs_rev, h3,  cite, text_stat]
    #print(data)     color A1C2F9
    head = """{% extends "baseform.html" %}
{% block header %}
        <a href="index.html"><button style="width:100px; height:40px;" type="submit">На головну</button></a>
        <a href="index1.html"><button style="width:100px; height:40px;" type="submit">Зображення</button></a>
        <a href="index2.html"><button style="width:170px; height:40px;" type="submit">Розширений пошук</button></a>
<div id="my_search_item">
<h2>Результати пошуку</h2>

"""
    work_hes_done = """{% endblock %}"""
    bodey = "<div></div>"
    for z in data:
        bodey = bodey + f"""<div><a href="{data[z][0]}"> {data[z][1]}{data[z][2]}</a>{data[z][3]}</div>"""
    end_work =head+bodey+work_hes_done
    with open("./templates/formsearch.html", 'w') as f:
        f.write(end_work)


@app.route("/", methods=["POST", "GET"])
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
        start_ref(URL)
    return render_template("formsearch.html")



#https://www.google.com/search?as_q=q&as_epq=w&as_oq=e&as_eq=r

@app.route("/form2", methods=["POST", "GET"])
def form2():
    if request.method == 'POST':
        print(request.form)
        URL = "https://www.google.com/search?as_q=" + request.form['as_q']+'&'+ request.form['as_epq']+'&'+ request.form['as_oq']+'&'+ request.form['as_eq']
        start_ref(URL)
    return render_template("formsearch.html")

if __name__ == "__main__":
    app.run(debug=True)