import requests as re
import pandas as pd
from bs4 import BeautifulSoup

top_stories = []
entertainment = []
latest_news = []
city_news = []
from_across_india = []
technology_news = []
sports = []
education = []
life_style = []

url = 'https://timesofindia.indiatimes.com/'
raw_page = re.get(url)
text = raw_page.text
news = BeautifulSoup(text, 'html.parser')
all_links = news.find_all('a')

for links in all_links:
    story = links.text
    if len(story) > 1 and story != 'more':
        city_news.append(story)

pd_def = pd.DataFrame({'Title': city_news})
print(pd_def.info())
pd_def.to_csv('Titles.csv')






