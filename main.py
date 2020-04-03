from bs4 import BeautifulSoup
from webbrowser import open_new_tab
from requests import get

args_object = argparse.ArgumentParser()
args_object.add_argument("update", type=int, default=0)

args = args_object.parser_args()

link_list = open("links.txt", "w")
