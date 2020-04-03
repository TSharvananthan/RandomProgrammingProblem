import os
try:
    from bs4 import BeautifulSoup
    import argparse
    from webbrowser import open_new_tab
    from requests import get
    from time import sleep
    from tqdm import trange
    import sys
except ImportError:
    raise ImportError("Installing all required libraries for you")
    os.system("pip3 install bs4")
    os.system("pip3 install requests")
    os.system("pip3 install tqdm")

link_list = open("links.txt", "w")

class Update:
    def __init__(self):
        self.dmoj = "https://dmoj.ca/problems/?page="
        self.codeforces = "https://codeforces.com/problemset/page/"
        self.spoj = "https://www.spoj.com/problems/classical/sort=0,start="
        self.projecteuler = "https://projecteuler.net/archives;page="
        self.rosettacode = "http://rosettacode.org/wiki/Category:Programming_Tasks"

    def scrape_rc_links(self):
        links = []
        object = BeautifulSoup(get(self.rosettacode).content, "html.parser").find("div", "mw-category").find_all("a")
        for x in trange(len(object), file=sys.stdout, desc='Updating RosettaCode Links'):
            links.append("http://rosettacode.org{}".format(object[x]["href"]))
        return links

    def scrape_spoj_links(self):
        max_pages = int([x.text for x in BeautifulSoup(get("https://www.spoj.com/problems/classical").content, "html.parser").find_all("a", class_="pager_link")][-3])
        links = []
        for x in range(0, max_pages + 1):
            links.extend(["https://www.spoj.com{}".format(b.find("td", {"align":"left"}).find("a")["href"]) for b in BeautifulSoup(get("{}{}".format(self.spoj, str(x * 50))).content, "html.parser").find("table", class_="problems table table-condensed table-hover").find("tbody").find_all("tr")])
            sleep(2)

        return links

    def scarpe_projecteuler_links(self):
        last_page = "https://projecteuler.net/{}".format(BeautifulSoup(get("https://projecteuler.net/archives;page=1").content, "html.parser").find("div", class_="pagination noprint").find_all("a")[-1]["href"])
        total_problems = int(BeautifulSoup(get(last_page).content, "html.parser").find_all("td", class_="id_column")[-1].text)
        return ["https://projecteuler.net/problem={}".format(snoopdogg) for snoopdogg in range(1, total_problems + 1)]

    def scrape_codeforces_links(self):
        last_page = int(BeautifulSoup(get("https://codeforces.com/problemset/page/1").content, "html.parser").find_all("span", class_="page-index")[-1].text)
        links = []
        for flomilly in range(1, last_page + 1):
            links.extend(["https://codeforces.com{}".format(yerrr.find("a")["href"]) for yerrr in BeautifulSoup(get("https://codeforces.com/problemset/page/{}".format(flomilly)).content, "html.parser").find("div", {"style":"background-color: #E1E1E1; padding-bottom: 3px;"}).find("table", class_="problems").find_all("tr")[1::]])

        return links

    def scrape_dmoj_links(self):
        last_page = int(BeautifulSoup(get("https://dmoj.ca/problems/").content, "html.parser").find("ul", class_="pagination").find_all("a")[-2].text)
        links = []
        for epsteindidntkillhimself in range(1, last_page + 1):
            links.extend(["https://dmoj.ca{}".format(rickygervaisdidntkillhimself.find("a")["href"]) for rickygervaisdidntkillhimself in BeautifulSoup(get("https://dmoj.ca/problems/").content, "html.parser").find_all("td", class_="problem")])

        return links

u = Update()

def UpdateLinks():
    global u
    for a in u.scrape_rc_links(): link_list.write(a + "\n")
    for a in u.scrape_spoj_links(): link_list.write(a + "\n")
    for a in u.scarpe_projecteuler_links(): link_list.write(a + "\n")
    for a in u.scrape_codeforces_links(): link_list.write(a + "\n")
    for a in u.scrape_dmoj_links(): link_list.write(a + "\n")
    link_list.close()

UpdateLinks()
