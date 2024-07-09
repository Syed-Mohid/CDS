import httpx
from bs4 import BeautifulSoup
import urllib3
import wget




def find_img_links(list_links,empty_list):
    for result in list_links:

        temp = result.find('img').attrs['src']

        empty_list.append(temp)



def find_img_name(list_name,empty_list):
    for result in list_name:

        temp = result.text

        temp = temp[7:]

        empty_list.append(temp)



def save_img(list_link,list_name):
    for i in range(0,len(list_link)):

        img_url= list_link[i]

        img_name = list_name[i]

        img_name = img_name + ".jpg"
        
        wget.download(img_url,'C:\\Users\\syedm\\Desktop\\CDS\\All cats\\'+img_name)
        




# 1. Find image links on the website
# Scrape the first 4 pages
url = f"https://ottawahumane.ca/adopt/cats-for-adoption/"

response = httpx.get(url)
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all('div',{"class":"info-card__image"})
names = soup.find_all('div',{"class":"info-card__title"})


text = []
link =[]

find_img_links(results,link)
find_img_name(names,text)


save_img(link,text)

