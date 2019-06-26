import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://www.urionlinejudge.com.br/judge/en/rank")
soup = BeautifulSoup(page.content, 'html.parser')

rank = soup.find(id="element")

users = rank.find_all('a')

for user in users:
    if re.search('/judge/en/profile', user.get('href'), re.IGNORECASE): 
        print(user.get_text())



