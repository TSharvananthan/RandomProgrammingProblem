try:
    from bs4 import BeautifulSoup
    import argparse
    from webbrowser import open_new_tab
except ImportError:
    

args_object = argparse.ArgumentParser()
args_object.add_argument("update", type=int, default=0)

args = args_object.parser_args()
