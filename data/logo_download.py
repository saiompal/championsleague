import psycopg2
import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests # to get image from the web
import shutil # to save it locally

url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/530"

querystring = {"timezone":"Europe%2FLondon"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "423672ab56mshc8f8270f6c85ac6p10a188jsn2ee3b1e6bfca"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
image_url=''
filename=''
for i in data["api"]["teams"]:
    image_url = i["logo"]
    filename = image_url.split("/")[-1]
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



