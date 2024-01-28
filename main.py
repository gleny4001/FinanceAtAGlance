
from datetime import date
import requests
from datetime import timedelta
from fastapi import FastAPI
from xml.etree import cElementTree as ET
import requests
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

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

titles = []
for item in responses:
  if type(item) == dict:
    titles.append(item['title'])


x = sentiment_pipeline(titles)
# print(x)
pos = 0
neg = 0
for e in x:
  if e['label'] == 'POSITIVE':
    pos+=1
  else:
    neg+=1

print(pos,neg)

app = FastAPI()
@app.get("/titles")
def titles():
  result = {
    'positive': pos,
    'negitive': neg
  }
  return result



