import pandas as pd
import requests as re
from bs4 import BeautifulSoup


story = []
url = 'http://www.cricbuzz.com/live-cricket-scores/18873/eng-vs-aus-3rd-odi-australia-tour-of-england-2018'
raw_page = re.get(url)
text = BeautifulSoup(raw_page.text, 'html.parser')
commentary = text.find_all('p')

for paragraphs in commentary:
    para = paragraphs.text
    story.append(para)

pd_story = pd.DataFrame({'Title': story})
print(pd_story.info())
pd_story.to_csv('Commentary.csv')
