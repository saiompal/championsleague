import psycopg2
import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests # to get image from the web
import shutil # to save it locally
my_url='https://www.skysports.com/champions-league-news'
uClient = uReq(my_url)
news_html = uClient.read()
uClient.close()
page_soup = soup(news_html,"html.parser")
news = page_soup.findAll("div",{"class":"news-list__item news-list__item--show-thumb-bp30"})
newspro=[]
for i in range(len(news)):    
    ## Set up the image URL and filename
    image_url = news[i].img["data-src"]
    filename = image_url.split("?")[0].split("/")[-1]
    newspro.append([news[i].h4.a.text.strip().replace("'","''"),news[i].p.text.strip().replace("'","''"),filename])
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
print(newspro[2])
  
conn = psycopg2.connect(
    database="championsleague",
    user = "postgres",
    password = "phoebes13",
    host="localhost",
    port="5432"
    )
cur = conn.cursor()
for i in range(0,len(newspro)):
    cur.execute("INSERT INTO footballnews_news values("+str(i)+",'"+newspro[i][0]+"','"+newspro[i][1]+"','"+newspro[i][2]+"')")
    conn.commit()


