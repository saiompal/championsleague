import psycopg2
import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests # to get image from the web
import shutil # to save it locally
my_url='https://www.youtube.com/channel/UC1ooLVWqFW-UH5xmUYW0xgA/featured'
uClient = uReq(my_url)
news_html = uClient.read()
uClient.close()
page_soup = soup(news_html,"html.parser")
news=page_soup.findAll("div")
print(news)
