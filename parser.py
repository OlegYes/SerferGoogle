
import requests
import bs4
from bs4 import BeautifulSoup as BS
import re
URL = "https://www.google.com/search?q=chees"
def start_ref(q):
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

        print(inmenu)
        lincs = i.get("href")

    return 0


if __name__ == '__main__':
     start_ref(URL)