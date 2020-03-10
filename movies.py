
import urllib.request
import requests
import json

def getMovieTitles(substr):

    url= 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr
    x = requests.get(url)
    x = x.text
    y = json.loads(x)
    pages = y["total_pages"]
    movies = []
    for page in range(1,pages+1):
        x = requests.get(url + '&page='+ str(page))
        x = x.text
        y = json.loads(x)
        for i in range(len(y['data'])):
            movies.append(y['data'][i]['Title'])
    movies = sorted(movies)
    for movie in movies:
        print(movie)

getMovieTitles('Spiderman')