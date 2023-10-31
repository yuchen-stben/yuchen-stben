import requests
from bs4 import BeautifulSoup

def get_latest_spiderman():
    response = requests.get("https://www.imdb.com/find?q=Spider-man&s=tt&ttype=ft&ref_=fn_ft")
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_spiderman = soup.find('table', {'class': 'findList'}).find('td', {'class': 'result_text'}).get_text(strip=True)
    print(latest_spiderman)

get_latest_spiderman()