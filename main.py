try:
    from bs4 import BeautifulSoup
    import argparse
    from webbrowser import open_new_tab
    from requests import get
    from time import sleep
    from tqdm import trange
    import sys
    import argparse
    import src.getLinks as gL
    from random import choice
except ImportError:
    raise ImportError("Installing all required libraries for you")
    os.system("pip3 install bs4")
    os.system("pip3 install requests")
    os.system("pip3 install tqdm")
    os.system("pip3 install argparse")

args_object = argparse.ArgumentParser()
args_object.add_argument("--problems", type=int, default=1, help="How many problems would you like?")
args_object.add_argument("--update", type=bool, default=False, help="Would you like to update your links text file? Enter 1 to update your links file")
args = args_object.parse_args()

if args.update == 1: gL.UpdateLinks(open("src/links.txt", "w"))
elif not args.update == 1 and not args.update == 0: raise ValueError("Input Either 0 or 1")

links = open("src/links.txt", "r").read().split("\n")

for x in range(args.problems):
    chosen = choice(links)
    open_new_tab(chosen)
