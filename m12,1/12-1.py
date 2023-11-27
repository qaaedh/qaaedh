



import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.chucknorris.io/jokes/random" + hakusana
vastaus = requests.get(pyyntö).json()
print(vastaus)