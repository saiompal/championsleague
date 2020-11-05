import psycopg2
import requests
import json
from datetime import datetime
import requests # to get image from the web
import shutil # to save it locally
from urllib.request import urlopen as uReq
url = "https://api-football-v1.p.rapidapi.com/v2/topscorers/530"

querystring = {"timezone":"Europe%2FLondon"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "423672ab56mshc8f8270f6c85ac6p10a188jsn2ee3b1e6bfca"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
conn = psycopg2.connect(
    database="championsleague",
    user = "postgres",
    password = "phoebes13",
    host="localhost",
    port="5432"
    )
cur = conn.cursor()
team_id=''
player_name=''
team_name=''
goals_scored=''
k=0
for i in data["api"]["topscorers"]:
    team_id=i["team_id"]
    player_name=i["player_name"]
    team_name=i["team_name"]
    goals_scored=i["goals"]["total"]
    team_id=str(team_id)+'.png'
    cur.execute("INSERT INTO footballnews_topplayers values('"+str(k)+"','"+player_name+"','"+team_name+"','"+str(goals_scored)+"','"+team_id+"')")
    team_id=''
    player_name=''
    team_name=''
    goals_scored=''
    k=k+1
conn.commit()

