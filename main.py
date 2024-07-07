import httpx
from bs4 import BeautifulSoup


# 1. Find image links on the website
# Scrape the first 4 pages
url = f"https://ottawahumane.ca/adopt/cats-for-adoption/"

response = httpx.get(url)
soup = BeautifulSoup(response.text, "html.parser")

divs = soup.find_all('div', class_='example-class')
for div in divs:
     
