from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import json
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

#This is where the user places their api Key in ''.
newsapi = NewsApiClient(api_key='f860d73b9e554ef49696f6ec93350997')

data = newsapi.get_everything(q='Sol de Mexico', language='es', page_size=30)

articles = data['articles']

print(f"\nNúmero de artículos encontrados: {data['totalResults']} \n")

#This loop actually displays the names of the articles it found.
for x, y in enumerate(articles):
    print(f'{x+1} {y["title"]}')

# Choose which article to display more info about
article_index = 2
selected_article = articles[article_index]

# Display article details
for key, value in selected_article.items():
    print(f"\n{key.ljust(15)}{value}")


print(f"\n")

# Display the image from urlToImage
if selected_article['urlToImage']:
    try:
        # Get image from URL
        response = requests.get(selected_article['urlToImage'])
        img = Image.open(BytesIO(response.content))
        
        # Display image using matplotlib
        plt.figure(figsize=(10, 8))
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.title(selected_article['title'])
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")
else:
    print("No image URL available for this article")