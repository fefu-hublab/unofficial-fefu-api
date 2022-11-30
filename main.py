"""API для \"Мой Универ\" ДВФУ"""

from bs4 import BeautifulSoup

import requests

LOGIN = "redrov.iy"
PASSWORD = "D1g1t4l.DVFU.Sh4d0w"
ESA_LOGIN_URL = "https://esa.dvfu.ru/"
UNIVER_URL = "https://univer.dvfu.ru"


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

session = requests.Session()
session.headers = headers

response = session.get(ESA_LOGIN_URL)

soup = BeautifulSoup(response.content, "lxml")

csrf_token = soup.find("meta", {"name": "csrf-token-value"})["content"]
csrf_univer = soup.find("meta", {"name": "csrf-token"})["content"]

response = session.post(
    ESA_LOGIN_URL,
    {
        "_csrf_univer": csrf_univer,
        "csrftoken": csrf_token,
        "username": LOGIN,
        "password": PASSWORD,
        "rememberMe": "0",
        "bu": UNIVER_URL
    },
    allow_redirects=True
)

soup = BeautifulSoup(response.content, "lxml")
print(soup.find("span", {"class": "user-profile-name"})["title"])
print(soup.find("span", {"id": "coin-balance"}).text)
