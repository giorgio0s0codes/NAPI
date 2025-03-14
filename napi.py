from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import json

newsapi = NewsApiClient(api_key='f860d73b9e554ef49696f6ec93350997')

data = newsapi.get_everything(q='jupyter lab', language='en', page_size=20)
type(data)
print(type(data))
#data.keys()
#data['status']
#data['totalResults']
#type[data['articles']]