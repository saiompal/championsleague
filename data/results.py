import psycopg2
import requests
import json
from datetime import datetime
import requests # to get image from the web
import shutil # to save it locally
from urllib.request import urlopen as uReq
url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/530/last/23"

querystring = {"timezone":"Europe%2FLondon"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "423672ab56mshc8f8270f6c85ac6p10a188jsn2ee3b1e6bfca"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
matches = []
matchdt=[]
scores=[]
venue=[]
for i in data["api"]["fixtures"]:
    scores.append(str(i["goalsHomeTeam"])+" : "+str(i["goalsAwayTeam"]))
    matches.append([i["homeTeam"]["team_name"],i["homeTeam"]["logo"].split("/")[-1],i["awayTeam"]["team_name"],i["awayTeam"]["logo"].split("/")[-1]])
    dt=i["event_date"]
    matchdt.append(dt[0:10])
    venue.append(i["venue"])
    
conn = psycopg2.connect(
    database="championsleague",
    user = "postgres",
    password = "phoebes13",
    host="localhost",
    port="5432"
    )
cur = conn.cursor()
for k in range(0,23):
    cur.execute("INSERT INTO footballnews_results values('"+str(k)+"','"+matches[k][0]+"','"+matches[k][2]+"','"+scores[k]+"','"+matchdt[k]+
                "','"+matches[k][3]+"','"+matches[k][1]+"','"+venue[k]+"')")
conn.commit()

