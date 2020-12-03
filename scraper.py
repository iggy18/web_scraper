from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Nardwuar"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.findAll("sup", "a")

print(results)
