from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import json
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

#mJiXIlQA6ShuQAafQ12m1GbtO5Ve5k4OAPqeP0Uu

#This is where the user places their api Key in ''.
newsapi = NewsApiClient(api_key='f860d73b9e554ef49696f6ec93350997')

data = newsapi.get_everything(
    q='Yolanda Ordaz de la Cruz', 
    language='es', 
    page_size=30,
    #from_param='2011-07-06',
    #to='2011-08-17',
    #sort_by='relevancy' #relevancy means articles more closely related to q come first.
)

articles = data['articles']

print(f"\nNúmero de artículos encontrados: {data['totalResults']} \n")

#This loop actually displays the names of the articles it found.
for x, y in enumerate(articles):
    print(f'{x+1} {y["title"]}')

user_input = input("You'd like to see any article in specific? (y/n): ")

if user_input.lower() == "y":
    # Choose which article to display more info about
    article_index = int(input("\nEnter the number of the article you want to view: ")) - 1
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

elif user_input.lower() == "n":
    print("Thanks. Bye!")

else:
    print("Invalid input. Please type 'y' or 'n'.")