import psycopg2
import requests
import json
from datetime import datetime

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
venues=[]
for i in data["api"]["fixtures"]:
    venues.append(i["venue"])
    matches.append([i["homeTeam"]["team_name"],i["homeTeam"]["logo"].split("/")[-1],i["awayTeam"]["team_name"],i["awayTeam"]["logo"].split("/")[-1]])
    dt=i["event_date"]
    matchdt.append(dt[0:10])

conn = psycopg2.connect(
    database="championsleague",
    user = "postgres",
    password = "phoebes13",
    host="localhost",
    port="5432"
    )
cur = conn.cursor()
for k in range(0,23):
    cur.execute("INSERT INTO footballnews_schedule values('"+str(k)+"','"+matches[k][0]+"','"+matches[k][2]+"','"+venues[k]+"','"+matchdt[k]+
                "','"+matches[k][3]+"','"+matches[k][1]+"')")
    conn.commit()


