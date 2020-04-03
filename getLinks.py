import os
from bs4 import BeautifulSoup
from requests import get
from time import sleep
from tqdm import trange
import sys

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
        for x in trange(0, max_pages + 1, file=sys.stdout, desc='Updating SPOJ Links'):
            links.extend(["https://www.spoj.com{}".format(b.find("td", {"align":"left"}).find("a")["href"]) for b in BeautifulSoup(get("{}{}".format(self.spoj, str(x * 50))).content, "html.parser").find("table", class_="problems table table-condensed table-hover").find("tbody").find_all("tr")])
            sleep(2)

        return links

    def scarpe_projecteuler_links(self):
        last_page = "https://projecteuler.net/{}".format(BeautifulSoup(get("https://projecteuler.net/archives;page=1").content, "html.parser").find("div", class_="pagination noprint").find_all("a")[-1]["href"])
        total_problems = int(BeautifulSoup(get(last_page).content, "html.parser").find_all("td", class_="id_column")[-1].text)
        links = []
        for snoopdogg in trange(1, total_problems + 1, file=sys.stdout, desc='Updating ProjectEuler Links'):
            links.append("https://projecteuler.net/problem={}".format(snoopdogg))
        return links

    def scrape_codeforces_links(self):
        last_page = int(BeautifulSoup(get("https://codeforces.com/problemset/page/1").content, "html.parser").find_all("span", class_="page-index")[-1].text)
        links = []
        for flomilly in trange(1, last_page + 1, file=sys.stdout, desc='Updating CodeForces Links'):
            links.extend(["https://codeforces.com{}".format(yerrr.find("a")["href"]) for yerrr in BeautifulSoup(get("https://codeforces.com/problemset/page/{}".format(flomilly)).content, "html.parser").find("div", {"style":"background-color: #E1E1E1; padding-bottom: 3px;"}).find("table", class_="problems").find_all("tr")[1::]])

        return links

    def scrape_dmoj_links(self):
        last_page = int(BeautifulSoup(get("https://dmoj.ca/problems/").content, "html.parser").find("ul", class_="pagination").find_all("a")[-2].text)
        links = []
        for epsteindidntkillhimself in trange(1, last_page + 1, file=sys.stdout, desc='Updating DMOJ Links'):
            links.extend(["https://dmoj.ca{}".format(rickygervaisdidntkillhimself.find("a")["href"]) for rickygervaisdidntkillhimself in BeautifulSoup(get("https://dmoj.ca/problems/").content, "html.parser").find_all("td", class_="problem")])

        return links

u = Update()

def UpdateLinks():
    global u
    rc = u.scrape_rc_links()
    spoj = u.scrape_spoj_links()
    projecteuler = u.scarpe_projecteuler_links()
    codeforces = u.scrape_codeforces_links()
    dmoj = u.scrape_dmoj_links()
    for a in trange(len(rc), file=sys.stdout, desc="Writing All RosettaCode Links To Text File"): link_list.write(rc[a] + "\n")
    for a in trange(len(spoj), file=sys.stdout, desc="Writing All SPOJ Links To Text File"): link_list.write(spoj[a] + "\n")
    for a in trange(len(projecteuler), file=sys.stdout, desc="Writing All ProjectEuler Links To Text File"): link_list.write(projecteuler[a] + "\n")
    for a in trange(len(codeforces), file=sys.stdout, desc="Writing All CodeForces Links To Text File"): link_list.write(codeforces[a] + "\n")
    for a in trange(len(dmoj), file=sys.stdout, desc="Writing All DMOJ Links To Text File"): link_list.write(dmoj[a] + "\n")
    link_list.close()
