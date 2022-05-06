
import requests
import bs4
from bs4 import BeautifulSoup as BS
import re
URL = "https://www.google.com/search?q=chees"
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


    for i in menu:

        inmenu = i.find_parent().find_parent().find_parent().find_parent()
        for q in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12:
            lincs = inmenu.get("href")
            h3 = inmenu.find("h3").text
            span = inmenu.find("span")

            data = {q: [lincs, h3, span]}
            print(data)


    return 0


if __name__ == '__main__':
     start_ref(URL)