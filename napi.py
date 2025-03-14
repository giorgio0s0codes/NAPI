from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import json

newsapi = NewsApiClient(api_key='f860d73b9e554ef49696f6ec93350997')

data = newsapi.get_everything(q='Canva', language='en', page_size=20)

articles = data['articles']

#This loop actually displays the names of the articles it found.
for x, y in enumerate(articles):
    print(f'{x} {y["title"]}')