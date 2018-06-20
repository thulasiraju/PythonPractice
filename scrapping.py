import requests
from bs4 import BeautifulSoup
import pandas as pd

names = []
years = []
names = []
imdb_ratings = []
metascores = []
votes = []

# Extract data from individual movie containers


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')

for containers in movie_containers:
    # If the movie has metascore then extract:
    if containers.find('div', class_='ratings-metascore') is not None:

        # Name of the movie
        name = containers.h3.a.text
        names.append(name)

        # The Year
        year = containers.h3.find('span', class_='lister-item-year text-muted unbold').text
        years.append(year)

        # IMDb  Ratings
        imdb_rating = float(containers.strong.text)
        imdb_ratings.append(imdb_rating)

        # The Meta Score
        metascore = containers.find('span', class_='metascore').text
        metascores.append(int(metascore))

        # Number of Votes
        vote = containers.find('span', attrs={'name': 'nv'})['data-value']
        votes.append(int(vote))

test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb_rating': imdb_ratings,
                       'metascore': metascores,
                       'votes': votes})
print(test_df.info())
print(test_df)



















