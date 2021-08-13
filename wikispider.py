import requests
from bs4 import BeautifulSoup

start_urls = [
    'https://en.wikipedia.org/wiki/Frederiksen_Cabinet',
]

response = requests.get(start_urls[0])
soup = BeautifulSoup(response.content, 'html.parser')
relevant_links = []

for i in soup.select("td:nth-of-type(3) a"):
    print(i)
    if i[u'href'].startswith(u'/wiki/'):
        relevant_links.append(i.get('href'))

print(relevant_links)
