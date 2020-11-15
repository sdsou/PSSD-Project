import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time


def search(keyword):
    """Modify inputs to use in URL"""
    keyword = keyword.replace(" ", "%20")
    # location = location.replace(" ", "%20")
    # salary = salary.replace(",", "%2C")
    URL = f"https://babson.joinhandshake.com/postings?page=1&per_page=25&sort_direction=desc&sort_column=default&query={keyword}"
    return URL


URL = search("data scientist")

page = requests.get(URL, data)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
