from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
newsapi = NewsApiClient(api_key='4926113a9e0340849310e63eba424fa5')

# Set the news sources you want to retrieve headlines from
bbc = 'bbc-news'
cnn = 'cnn'
wallstreet = 'the-wall-street-journal'
reuters = 'reuters'
bloomberg = 'bloomberg'


bbc_headline = []
cnn_headline = []
wallstreet_headline = []
reuters_headline = []
bloomberg_headline = []

# Use the get_top_headlines method to retrieve the latest headlines
top_bbc = newsapi.get_top_headlines(sources=bbc)
top_cnn = newsapi.get_top_headlines(sources=cnn)
top_wallstreet = newsapi.get_top_headlines(sources=wallstreet)
top_reuters = newsapi.get_top_headlines(sources=reuters)
top_bloomberg = newsapi.get_top_headlines(sources=bloomberg)

# Print the title of each article
for article in top_bbc['articles']:
    bbc_headline.append(article['title'])

for article in top_cnn['articles']:
    cnn_headline.append(article['title'])

for article in top_bloomberg['articles']:
    bloomberg_headline.append(article['title'])

for article in top_wallstreet['articles']:
    wallstreet_headline.append(article['title'])

for article in top_reuters['articles']:
    reuters_headline.append(article['title'])
