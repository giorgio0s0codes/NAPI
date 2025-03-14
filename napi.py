from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import json

newsapi = NewsApiClient(api_key='f860d73b9e554ef49696f6ec93350997')

data = newsapi.get_everything(q='Canva', language='en', page_size=20)

#This will return dict, wich I've read that means the info is in type dictionary.
#print(type(data))
type(data)

#This returns dict_keys(['status', 'totalResults', 'articles']), which gives structure to the data.
data.keys()

#This returns the status of the request to the news.
#data['status']

#This returns the number of articles you actually found, not the number of the ones you asked for.
#data['totalResults']

#I used this to discover what was 'articles', it's a list.
#print(type(data['articles']))

#print(data['articles'][0])

for article in data['articles']:
    print(article['title'])