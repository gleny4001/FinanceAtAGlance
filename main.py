
from datetime import date
import requests
from datetime import timedelta
from fastapi import FastAPI
from xml.etree import cElementTree as ET
import requests

#API requests
url = 'https://newsapi.org/v2/everything?'
api_key = 'e71718aef8dc469f9dd05d860721ab3a'
today = date.today()- timedelta(days = 1)

parameters_headlines = {
    'q': 'finance',
    'sortBy':'popularity',
    'pageSize': 100,
    'apiKey': api_key,
    'language': 'en',
    'from' : today   
}

response = requests.get(url, params=parameters_headlines)

responses = ''
response_json_headline = ''
if response.status_code == 200:
  response_json_headline = response.json()
  responses = response_json_headline["articles"]
else:
  print(f"Failed to retrieve data. Status code: {response.status_code}")


result = {}
for item in responses:
  if type(item) == dict:
    result[str(item['title'])] =  str(item['description'])



app = FastAPI()

@app.get("/titles")
def titles():
  return result



